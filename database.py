import sqlite3
import log


def logdb(func):
    def wrapper(cat_id, cur):
        # db_logger = logging.getLogger('db')
        #
        # file_log = logging.FileHandler('Log.log')
        # console_out = logging.StreamHandler()
        #
        # logging.basicConfig(handlers=(file_log, console_out),
        #                     format='[%(asctime)s | %(levelname)s]: %(message)s',
        #                     datefmt='%m.%d.%Y %H:%M:%S',
        #                     level=logging.INFO)
        # db_logger.info(f'Try to get id:{cat_id}')
        dblog = log.get_logger('db')
        dblog.debug(f'Try to get id:{cat_id}')
        return func(cat_id, cur)
    return wrapper


def add_cat_to_bd(cat_url, cat_id, cur):
    cur.execute("INSERT INTO cats VALUES (?, ?)", (cat_url, cat_id))


@logdb
def find_cat_id(cat_id, cur):
    cur.execute('SELECT cat_url FROM cats WHERE cat_id=?', (cat_id,))
    url = cur.fetchone()
    return url


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
