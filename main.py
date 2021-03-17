from db_create import create_connection, user_import
from py_trans_load import daily_user_ct_create

def main():
    # Input name for db and user data csv file
    db_name = "keetsqlite.db"
    users_file = "users.csv"

    # Creating users sqlite table and importing CSV data into it
    conn = create_connection(db_name)
    user_import(users_file, conn)

    # Taking data from SQLite, transforming with python, and sending back to SQLite db
    daily_user_ct_create(db_name)

    print('Complete')
    return


if __name__ == '__main__':
    main()