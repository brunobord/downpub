from flask import Blueprint, request, render_template, \
    flash, g, session, redirect, url_for
from flask.ext.babel import gettext
from flask.ext.babel import gettext, Babel

from downpub import db
from downpub.books.forms import AddForm, EditForm, AddPartForm, EditPartForm
from downpub.books.models import Book, Part
from downpub.books.decorators import requires_login
from downpub.users.models import User

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
    books = Book.query.filter_by(user_id=session['user_id']).all()
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

        title=form.title.data
        if form.cover.data:
            cover = form.cover.data
        else:
            cover = None

        # create an user instance not yet stored in the database
        book = Book(title=title, user_id=session['user_id'],
            cover=cover, creation_date=None)
        print(book)
        # Insert the record in our database and commit it
        db.session.add(book)
        db.session.commit()

        # flash will display a message to the user
        flash(gettext('That book has been created !'))
        # redirect user to the 'home' method of the user module.
        return redirect(url_for('books.list'))

    if not form.validate_on_submit():
        flash(gettext("The form doesn't validate..."))

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

        # commit
        db.session.commit()

        # flash will display a message to the user
        flash(gettext('That book has been edited !'))

        # redirect user to the 'home' method of the user module.
        return redirect(url_for('books.list', book_id=book_id))

    return render_template("books/edit.html",
        form=form, book=book, user=g.user)


@mod.route('/<book_id>/del/', methods=['GET', 'POST'])
@requires_login
def delete(book_id):
    """
    Delete the book with book_id
    """

    # We get the part to deleter
    book = Book.query.get(id=book_id)
    db.session.delete(book)
    # commit
    db.session.commit()

    # flash will display a message to the user
    flash(gettext('That part has been edited !'))

    # redirect user to the list of parts method of the user module.
    return redirect(url_for('books.parts_list', book_id=book_id))


@mod.route('/<book_id>/parts/', methods=['GET', 'POST'])
@requires_login
def parts_list(book_id):
    """
    List the parts (ordered by order field) from the book with book_id
    """
    parts = Part.query.get(book_id)
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
    if form.validate_on_submit():
        # create an user instance not yet stored in the database
        part = Part(book_id=form.book_id.data, title=form.title.data,
        content=form.content.data, order=form.order.data)
        # Insert the record in our database and commit it
        db.session.add(part)
        db.session.commit()

        # flash will display a message to the user
        flash(gettext('That part has been added !'))

        # redirect user to the 'home' method of the user module.
        return redirect(url_for('books.parts_list', book_id=book_id))

    return render_template("books/add_part.html",
        form=form, session=session, user=g.user)


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
        form=form, book=book, session=session, user=g.user)


@mod.route('/<book_id>/del_part/<part_id>/', methods=['GET', 'POST'])
@requires_login
def del_part(book_id, part_id):
    """
    Delete the part with part_id in the book with book_id
    """

    # We get the part to delete
    part = Part.query.filter_by(id=part_id).get()

    # flash will display a message to the user
    flash(gettext('That part has been edited !'))

    # redirect user to the list of parts method of the user module.
    return redirect(url_for('books.parts_list',
        book_id=book_id), session=session, user=g.user)