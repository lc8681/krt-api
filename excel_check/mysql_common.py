# coding:utf-8

import pandas
import sqlite3

csv_path = 'huamingce.csv'
sqlite_path = 'sqlite'


def sql_connect():
    table_name = "staff_info"
    conn = sqlite3.connect(sqlite_path)
    conn.execute('drop table staff_info')
    df = pandas.read_csv(csv_path)
    df.to_sql(table_name, conn, if_exists='append', index=False)
    print('ok')


if __name__ == '__main__':
    sql_connect()
