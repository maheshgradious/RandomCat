import sqlite3

import requests
from flask import Flask, g

import database

app = Flask(__name__)


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('cats.db')
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def index_cat():
    # TODO return cat picture and id
    get_picture = requests.get('https://api.thecatapi.com/v1/images/search')  # Get picture

    url_pic = get_picture.json()[0]["url"]  # Get picture url from json
    id_pic = get_picture.json()[0]["id"]  # Get picture id from json

    cur = get_db().cursor()  # Connect to db
    database.add_cat_to_bd(url_pic, id_pic, cur)  # Add new record to db
    get_db().commit()  # Commit changes
    return f"<img src='{url_pic}'>"


@app.route('/<cat_id>/')
def get_cat_by_id(cat_id):
    # TODO return cat picture by id if exists

    return "<img src='https://cdn2.thecatapi.com/logos/thecatapi_256xW.png'>"


if __name__ == '__main__':
    app.run()
