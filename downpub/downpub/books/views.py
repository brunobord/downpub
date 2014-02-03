from flask import Blueprint, request, render_template, flash, g, session, redirect, url_for
from werkzeug import check_password_hash, generate_password_hash
from flask.ext.babel import gettext

from downpub import db
from downpub.books.forms import AddForm, EditForm, AddPartForm, EditPartForm
from downpub.books.models import Book,Part
from downpub.books.decorators import requires_login

mod = Blueprint('books', __name__, url_prefix='/books')

@mod.before_request
def before_request():
  """
  pull user's profile from the database before every request are treated
  """
  g.user = None
  if 'user_id' in session:
    g.user = User.query.get(session['user_id'])



@mod.route('/list')
@requires_login
def list():
  return render_template("books/list.html", books=Book.query.filterby(user_id = g.user).all())

@mod.route('/add')
@requires_login
def add():
  form = AddForm(request.form)
  if form.validate_on_submit():
    # create an user instance not yet stored in the database
    book = Book(title=form.title.data, user_id=g.user)
    # Insert the record in our database and commit it
    db.session.add(book)
    db.session.commit()

    # flash will display a message to the user
    flash(_('That book has been created !'))
    # redirect user to the 'home' method of the user module.
    return redirect(url_for('books.list', book_id = book_id))
  return render_template("books/add.html", form=form)


@mod.route('/edit/<book_id>')
@requires_login
def edit(book_id):
  form = AddForm(request.form)
  book = Book.query.filterby(id = book_id).get()

  if not form.validate_on_submit():
    # form initializing when we first show the edit page
    form.title.data = book.title

  if form.validate_on_submit():
    # get an user instance not yet stored in the database
    book = Book.query.filterby(id = book_id).get()

    # set the new values
    book.title = form.book.data

    # commit
    db.session.commit()

    # flash will display a message to the user
    flash(_('That book has been edited !'))

    # redirect user to the 'home' method of the user module.
    return redirect(url_for('books.list', book_id = book_id))

  return render_template("books/edit.html", form=form)




@mod.route('/del/<book_id>', methods=['GET', 'POST'])
@requires_login
def delete(book_id):
  """
  Delete the part with part_id in the book with book_id
  """

  # We get the part to deleter
  book = Book.query.filterby(id = book_id).get()
  # commit
  db.session.commit()

  # flash will display a message to the user
  flash(_('That part has been edited !'))

  # redirect user to the list of parts method of the user module.
  return redirect(url_for('books.parts_list', book_id = book_id))


@mod.route('/<book_id>/', methods=['GET', 'POST'])
@requires_login
def parts_list(book_id):
  """
  List the parts (ordered by order field) from the book with book_id
  """
  parts = Part.query.filterby(book_id = book_id, user_id = g.user).all()
  return render_template("books/parts_list.html", parts=parts)

@mod.route('/<book_id>/add_part', methods=['GET', 'POST'])
@requires_login
def add_part(book_id):
  """
  Add a part to the book with book_id
  """
  form = AddPartForm(request.form)
  if form.validate_on_submit():
    # create an user instance not yet stored in the database
    part = Part(book_id=form.book_id.data, title=form.title.data, \
      content=form.content.data, order=form.order.data)
    # Insert the record in our database and commit it
    db.session.add(part)
    db.session.commit()

    # flash will display a message to the user
    flash(_('That part has been added !'))

    # redirect user to the 'home' method of the user module.
    return redirect(url_for('books.parts_list', book_id = book_id))

  return render_template("books/add_part.html", form=form)


@mod.route('/<book_id>/edit_part/<part_id>', methods=['GET', 'POST'])
@requires_login
def edit_part(book_id, part_id):
  """
  Edit the part with part_id in the book with book_id
  """
  form = EditPartForm(request.form)
  book = Book.query.filterby(id = book_id).get()
  part = Part.query.filterby(id = part_id).get()
  
  if not form.validate_on_submit():
    # form initializing when we first show the edit page
    form.title.data = part.title 
    form.content.data = part.content 
    form.order.data = part.order 

  if form.validate_on_submit():
    # get an user instance not yet stored in the database
    part = Part.query.filterby(id = part_id).get()

    # set the new values
    part.title = form.title.data
    part.content = form.content.data
    part.order = form.order.data

    # commit
    db.session.commit()

    # flash will display a message to the user
    flash(_('That part has been edited !'))

    # redirect user to the 'home' method of the user module.
    return redirect(url_for('books.parts_list', book_id = book_id))

  return render_template("books/edit_part.html", form=form, book=book)



@mod.route('/<book_id>/del_part/<part_id>', methods=['GET', 'POST'])
@requires_login
def del_part(book_id, part_id):
  """
  Delete the part with part_id in the book with book_id
  """

  # We get the part to deleter
  part = Part.query.filterby(id = part_id).get()

  # flash will display a message to the user
  flash(_('That part has been edited !'))

  # redirect user to the list of parts method of the user module.
  return redirect(url_for('books.parts_list', book_id = book_id))