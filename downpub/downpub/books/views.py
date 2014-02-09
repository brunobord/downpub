# -*- coding: utf-8 -*-
#!/usr/bin/env python

# Import the subprocess module to launch/communicate with the pandoc tool used to generate export files
import subprocess
import os
from datetime import datetime

from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from flask.ext.babel import gettext, Babel
from werkzeug.utils import secure_filename

from downpub import db, babel
from downpub.books.forms import AddForm, EditForm, AddPartForm, EditPartForm
from downpub.books.models import Book, Part
from downpub.books.decorators import requires_login
from downpub.users.models import User

from config import EXPORT_DIR

mod = Blueprint('books', __name__, url_prefix='/books')


@mod.before_request
def before_request():
    """
    pull user's profile from the database before every request are treated
    """
    g.user = None
    if 'user_id' in session:
        g.user = User.query.get(session['user_id'])


@mod.route('/list/')
@requires_login
def list():
    """
    List the books the actual user created
    """
    books = Book.query.filter_by(user_id=session['user_id']).order_by(Book.modified_at.desc()).all()
    return render_template("books/list.html",
        books=books,
        user=g.user)


@mod.route('/add/', methods=['GET', 'POST'])
@requires_login
def add():
    """
    Add the book
    """
    form = AddForm(request.form)
    if form.validate_on_submit():

        title = form.title.data
        if form.cover.data:
            cover = form.cover.data
        else:
            cover = None

        # create an user instance not yet stored in the database
        book = Book(title=title, user_id=session['user_id'],
            cover=cover, creation_date=None, modified_at=None)
        print(book)
        # Insert the record in our database and commit it
        db.session.add(book)
        db.session.commit()

        # flash will display a message to the user
        flash(gettext('That book has been created !'))
        # redirect user to the 'home' method of the user module.
        return redirect(url_for('books.list'))

    return render_template("books/add.html",
        form=form, user=g.user)


@mod.route('/<book_id>/edit/', methods=['GET', 'POST'])
@requires_login
def edit(book_id):
    """
    Edit the book with book_id
    """
    form = EditForm(request.form)
    book = Book.query.get(book_id)

    if not form.validate_on_submit():
        # form initializing when we first show the edit page
        form.title.data = book.title

    if form.validate_on_submit():
        # get an user instance not yet stored in the database
        book = Book.query.get(book_id)

        # set the new values
        book.title = form.title.data
        book.modified_at = datetime.utcnow()

        # commit
        db.session.commit()

        # flash will display a message to the user
        flash(gettext('That book has been edited !'))

        # redirect user to the 'home' method of the user module.
        return redirect(url_for('books.list', book_id=book_id))

    return render_template("books/edit.html",
        form=form, book=book, user=g.user)


@mod.route('/<book_id>/delete/', methods=['GET', 'POST'])
@requires_login
def delete(book_id):
    """
    Delete the book with book_id
    """

    # We get the part to deleter
    book = Book.query.get(book_id)
    db.session.delete(book)
    # commit
    db.session.commit()

    # flash will display a message to the user
    flash(gettext('That book has been deleted !'))

    # redirect user to the list of parts method of the user module.
    return redirect(url_for('books.list', book_id=book_id))


@mod.route('/<book_id>/export/<export_format>', methods=['GET', 'POST'])
@requires_login
def export(book_id, export_format):
    """
    Export the book with book_id
    """

    # We get all the data we have to pass to pandoc
    book = Book.query.get(book_id)
    parts = Part.query.filter_by(book_id=book_id).order_by(Part.order).all()

    # Now we check if all needed directories exists, and if it doesn't we create them
    if not os.path.isdir(EXPORT_DIR + "/" + book_id):
        subprocess.Popen(['mkdir -p', EXPORT_DIR + "/" + book_id])
    if not os.path.isdir(EXPORT_DIR + "/" + book_id + "/export"):
        subprocess.Popen(['mkdir -p', EXPORT_DIR + "/" + book_id + "/export"])

    # we generate the files we'll pass to pandoc, starting with the book
    # composed of the title, the author, then each part in the right order
    export_file = open(EXPORT_DIR + "/" + book_id + "/export/" + book_id + '.md', 'w')

    export_file.write('% ' + book.title + '\n')
    export_file.write('% ' + book.author + '\n')

    for the_part in parts:
        export_file.write(the_part.content + '\n')

    # When we wrote everything, we close the file
    export_file.close()

    # Set up the echo command and direct the output to a pipe
    p1 = subprocess.Popen(['pandoc -S', EXPORT_DIR + "/" + book_id + "/export/" + book_id + '.md',
                            '-o ', EXPORT_DIR + "/" + book_id + "/export/book-" + book_id + ".epub",
                            '-f markdown',
                            '-t ', export_format,
                            ], stdout=subprocess.PIPE)

    # Run the pandoc command
    output = p1.communicate()[0]

    # flash will display a message to the user
    flash(gettext('That book has been exported !'))

    # redirect user to the result page with a link if the export was successful
    return redirect(url_for('books.export', output=output, book=book))


@mod.route('/<book_id>/parts/', methods=['GET', 'POST'])
@requires_login
def parts_list(book_id):
    """
    List the parts (ordered by order field) from the book with book_id
    """
    parts = Part.query.filter_by(book_id=book_id).order_by(Part.order).all()
    book = Book.query.get(book_id)
    return render_template("books/parts_list.html",
        parts=parts, session=session, user=g.user, book=book)


@mod.route('/<book_id>/add_part/', methods=['GET', 'POST'])
@requires_login
def add_part(book_id):
    """
    Add a part to the book with book_id
    """
    form = AddPartForm(request.form)
    book = Book.query.get(book_id)

    if form.validate_on_submit():
        # create an user instance not yet stored in the database
        part = Part(book_id=book_id, title=form.title.data,
        content=form.content.data, order=form.order.data)
        # Insert the record in our database and commit it
        db.session.add(part)
        db.session.commit()

        # flash will display a message to the user
        flash(gettext('That part has been added !'))

        # redirect user to the 'home' method of the user module.
        return redirect(url_for('books.parts_list', book_id=book_id))

    return render_template("books/add_part.html",
        form=form, session=session, book=book, user=g.user)


@mod.route('/<book_id>/edit_part/<part_id>/', methods=['GET', 'POST'])
@requires_login
def edit_part(book_id, part_id):
    """
    Edit the part with part_id in the book with book_id
    """
    form = EditPartForm(request.form)
    book = Book.query.get(book_id)
    part = Part.query.get(part_id)

    if not form.validate_on_submit():
        # form initializing when we first show the edit page
        form.title.data = part.title
        form.content.data = part.content
        form.order.data = part.order

    if form.validate_on_submit():
        # get an user instance not yet stored in the database
        part = Part.query.get(part_id)

        # set the new values
        part.title = form.title.data
        part.content = form.content.data
        part.order = form.order.data

        # commit
        db.session.commit()

        # flash will display a message to the user
        flash(gettext('That part has been edited !'))

        # redirect user to the 'home' method of the user module.
        return redirect(url_for('books.parts_list', book_id=book_id))

    return render_template("books/edit_part.html",
        form=form, part=part, book=book, session=session, user=g.user)


@mod.route('/<book_id>/del_part/<part_id>/', methods=['GET', 'POST'])
@requires_login
def del_part(book_id, part_id):
    """
    Delete the part with part_id in the book with book_id
    """

    # We get the part to delete
    part = Part.query.get(part_id)
    db.session.delete(part)
    db.session.commit()

    # flash will display a message to the user
    flash(gettext('That part has been deleted !'))

    parts = Part.query.filter_by(book_id=book_id).all()
    book = Book.query.get(book_id)
    # redirect user to the list of parts method of the user module.
    return redirect(url_for('books.parts_list',
        parts=parts, session=session, user=g.user, book=book))


@mod.route('/<book_id>/export_part/<part_id>/format/<export_format>', methods=['GET', 'POST'])
@requires_login
def export_part(book_id, part_id, export_format):
    """
    Export the part with part_id from its book
    """

    # We get all the data we have to pass to pandoc
    book = Book.query.get(book_id)
    part = Part.query.get(part_id)

    # Now we check if all needed directories exists, and if it doesn't we create them
    if not os.path.isdir(EXPORT_DIR + "/" + book_id):
        subprocess.Popen(['mkdir -p', EXPORT_DIR + "/" + book_id])
    if not os.path.isdir(EXPORT_DIR + "/" + book_id + "/export"):
        subprocess.Popen(['mkdir -p', EXPORT_DIR + "/" + book_id + "/export"])

    # we generate the files we'll pass to pandoc, starting with the book
    # composed of the title, the author, then each part in the right order
    export_file = open(EXPORT_DIR + "/" + book_id + "/export/" + book_id + '-part-' + part_id + '.md', 'w')

    export_file.write('% ' + book.title + '\n')
    export_file.write('% ' + book.author + '\n')

    export_file.write(part.content + '\n')

    # When we wrote everything, we close the file
    export_file.close()

    # Set up the echo command and direct the output to a pipe
    p1 = subprocess.Popen(['pandoc -S', EXPORT_DIR + "/" + book_id + "/export/" + book_id + '-part-' + part_id + '.md',
                           '-o ', EXPORT_DIR + "/" + book_id + "/export/book-" + book_id + '-part-' + part_id + "." + export_format,
                           '-f markdown',
                           '-t ', export_format,
                           ], stdout=subprocess.PIPE)

    # Run the pandoc command
    output = p1.communicate()[0]

    # flash will display a message to the user
    flash(gettext('That book has been exported !'))

    # redirect user to the result page with a link if the export was successful
    return redirect(url_for('books.export_part', output=output, book=book, part=part))


@mod.route('/<book_id>/get/<export_format>', methods=['GET', 'POST'])
@requires_login
def get_book(book_id, export_format):
    """
    Get the chosen book in <export_format> format.
    """

    book = Book.query.get(book_id)

    # we now send the correct file to the user
    file_path = EXPORT_DIR + "/" + book_id + "/export/book-" + book_id + "." + export_format


@mod.route('/<book_id>/get_part/<part_id>/format/<export_format>', methods=['GET', 'POST'])
@requires_login
def get_part(part_id, book_id, export_format):
    """
    Get the chosen book in <export_format> format.
    """

    # we now send the correct file to the user
    file_path = EXPORT_DIR + "/" + book_id + "/export/book-" + book_id + '-part-' + part_id + "." + export_format


def allowed_file(filename):
    """
    Check if the uploaded fiel has the right extension
    """
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS