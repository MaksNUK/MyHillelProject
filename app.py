import sqlite3
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


def execute_query(query):
    with sqlite3.connect('books.db') as conn:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        return cursor.fetchall()


def get_by_id(table, book_id):
    return execute_query(
        f"SELECT * FROM {table} WHERE id={book_id}"
    )[0]


def select_all(table):
    return execute_query(
        f"SELECT * FROM {table}"
    )


def get_by_year(table, value):
    return execute_query(
        f"SELECT * FROM {table} WHERE year={value}"
    )[0]


def get_id_by_name(table, value):
    return execute_query(
        f"SELECT * FROM {table} WHERE name='{value}'"
    )[0][0]


@app.route('/')
def book_list():
    books = execute_query("SELECT * FROM book")
    return render_template('index.html',
                           books=books, get_by_id=get_by_id, get_by_year=get_by_year)


@app.route('/author/<int:pk>/')
def book_detail(pk):
    books = execute_query(f"SELECT * FROM book WHERE author={pk}")
    return render_template('index.html',
                           books=books, get_by_id=get_by_id, get_by_year=get_by_year)


@app.route('/year/<int:year>/')
def books_by_year(year):
    books = execute_query(f"SELECT * FROM book WHERE year={year}")
    return render_template('index.html',
                           books=books, get_by_id=get_by_id, get_by_year=get_by_year)


@app.route('/genre/<int:pk>/')
def books_by_genre(pk):
    books = execute_query(f"SELECT * FROM book WHERE genre={pk}")
    return render_template('index.html',
                           books=books, get_by_id=get_by_id, get_by_year=get_by_year)


@app.route('/edit/book/<int:pk>/', methods=['GET', 'POST'])
def edit_book(pk):
    if request.method == 'POST':
        if "hidden_form" in request.form:
            book_values = execute_query(
                f"SELECT * FROM book WHERE id='{pk}'"
            )
            return render_template('edit_book.html',
                                   book_values=book_values,
                                   get_by_id=get_by_id, get_by_year=get_by_year, select_all=select_all)
        elif request.form['edit_form']:
            execute_query(
                f"""
                UPDATE book
                SET 
                name='{request.form['name']}',
                genre='{get_id_by_name('genre', request.form['genre'])}',
                author='{get_id_by_name('author', request.form['author'])}',
                year='{request.form['year']}'
                WHERE id={pk};"""
            )
            return redirect('/')

    return redirect('/')


@app.route('/create/book/', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        execute_query(
            f"""
            INSERT INTO book (name, genre, author, year)
            VALUES
            ('{request.form['name']}',
            '{get_id_by_name('genre', request.form['genre'])}',
            '{get_id_by_name('author', request.form['author'])}',
            '{request.form['year']}')"""
        )
        return redirect('/')
    return render_template('add_book.html', select_all=select_all)


@app.route('/create/janr/', methods=['GET', 'POST'])
def add_genre():
    genres = execute_query(f'SELECT * FROM genre')
    if request.method == 'POST':
        execute_query(
            f"INSERT INTO genre (name) VALUES ('{request.form['genre']}')"
        )
        return redirect('/create/janr/')
    return render_template('add_genre.html', select_all=select_all, genres=genres)


@app.route('/create/author/', methods=['GET', 'POST'])
def add_author():
    authors = execute_query(f'SELECT * FROM author')
    if request.method == 'POST':
        execute_query(
            f"INSERT INTO author (name) VALUES ('{request.form['author']}')"
        )
        return redirect('/create/author/')
    return render_template('add_author.html', select_all=select_all, authors=authors)


@app.route('/remove_book/', methods=['POST'])
def remove_book():
    execute_query(
        f"DELETE FROM book WHERE id={request.form['id']}"
    )
    return redirect('/')


if __name__ == '__main__':
    app.run(
        host='127.0.0.1',
        port=5777,
        debug=True
    )
