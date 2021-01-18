import sqlite3


def add_cat_to_bd(cat_url, cat_id, cur):
    cur.execute("INSERT INTO cats VALUES (?, ?)", (cat_url, cat_id))


def find_cat_id(cat_id):
    pass


def create_db():
    db = sqlite3.connect('cats.db')
    sql = db.cursor()
    sql.execute("""CREATE TABLE IF NOT EXISTS cats (
    cat_url TEXT,
    cat_id TEXT
    )""")
    db.commit()
    db.close()


if __name__ == "__main__":
    create_db()
