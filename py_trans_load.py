import pandas as pd
import sqlite3

def daily_user_ct_create(db_name):
    """
    Takes user table data and creates new, grouped df
    :param db_name: string name of SQLite db
    :return:
    """
    # Query calling id and date columns
    user_query = """ SELECT
                        id,
                        visit_date
                    FROM
                        users;"""
    # Create connection to user table and import to pandas
    conn = sqlite3.connect(db_name)
    df = pd.read_sql_query(user_query, conn)

    # Group data and get counts
    df_count = df.groupby('visit_date', as_index=False).count()

    # Date columns
    df_count['year'] = pd.DatetimeIndex(df_count['visit_date']).year
    df_count['month'] = pd.DatetimeIndex(df_count['visit_date']).month
    df_count['day'] = pd.DatetimeIndex(df_count['visit_date']).day

    # Getting expected count based on mean, has a min 2 days, but average based on 4 in case weekends see shift
    df_count['count'] = df_count['id'].rolling(4, min_periods=2).mean()

    # Renaming observed counts column and reordering
    df_count = df_count.rename(columns={'id':'observed'})
    df_count = df_count[['year', 'month', 'day', 'observed', 'count']]

    # Final NaN fill and rounded means
    df_count = df_count.fillna(0).round(2)

    # Sending to daily_user_counts
    df_count.to_sql('daily_user_counts', conn,  if_exists='replace', index=False)

    # Closing connection
    conn.commit()
    conn.close()

    return
