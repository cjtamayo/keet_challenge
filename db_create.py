from sqlite3 import Error
import csv
import sqlite3


def create_connection(db_file):
    """
    Creates SQLite db
    :param db_file: db file name to connect to. If nonexistent, a new db will be created
    :return: SQLite connection
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return conn


def user_import(user_file, conn):
    """
    Creates user table from CSV
    :param user_file: CSV user file
    :param db_file: db file name
    :param conn: db connection
    :return:
    """
    # Command to create SQLite tables
    user_cmd = """ CREATE TABLE IF NOT EXISTS users (
                                        id TEXT,
                                        first_name TEXT,
                                        last_name TEXT,
                                        age TEXT,
                                        gender TEXT,
                                        visit_date TEXT
                                    ); """

    duc_cmd = """ CREATE TABLE IF NOT EXISTS daily_user_counts (
                                            year TEXT,
                                            month TEXT,
                                            day TEXT,
                                            observed TEXT,
                                            count TEXT
                                        ); """

    try:
        # Create cursor and tables
        cur = conn.cursor()
        cur.execute(user_cmd)
        cur.execute(duc_cmd)

        # Use CSV to fill users table
        csv_read = open(user_file)
        rows = csv.reader(csv_read)
        cur.executemany('INSERT INTO users VALUES (?,?,?,?,?,?)', rows)

        # Remove headers
        cur.execute("DELETE FROM users WHERE id = 'id'")

        # Commit and close connection
        conn.commit()
        conn.close()
    except Error as e:
        print(e)

    return
