import sqlite3
from flask import g

DATABASE = 'db.db'


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        g._database = sqlite3.connect(DATABASE)
        db = g._database
    db.row_factory = sqlite3.Row
    return db


def close_db(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


def query_db(query, args=()):
    db_cursor = get_db().execute(query, args)
    rows = db_cursor.fetchall()
    db_cursor.close()
    return rows if rows else None
