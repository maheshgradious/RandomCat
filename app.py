from flask import Flask

app = Flask(__name__)


@app.route('/')
def index_cat():
    # TODO return cat picture and id
    return "Hello, I'm Cat!"


@app.route('/<cat_id>/')
def get_cat_by_id(cat_id):
    # TODO return cat picture by id if exists
    return "<img src='https://cdn2.thecatapi.com/logos/thecatapi_256xW.png'>"


if __name__ == '__main__':
    app.run()
