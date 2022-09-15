from flask import Flask, render_template, session, redirect
from helpers import close_db, query_db

app = Flask(__name__)

# a prerequisite setting before session can be used or accessed
app.secret_key = 'asdfawkjeflkjh'


@app.route('/')
def index():
    rows = query_db('SELECT * FROM users')
    for row in rows:
        print(row['email'])

    if 'visits' not in session:
        session['visits'] = 0
    else:
        session['visits'] += 1
    return render_template('index.html')


@app.route('/items')
def items():
    items = ['thing', 'thing2', 'thing3']
    return render_template('items.html', items=items)


@app.route('/redirect')
def redir():
    return redirect('/')


@app.teardown_appcontext
def close_connection(exception):
    close_db(exception)
