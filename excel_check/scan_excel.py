# coding:utf-8

from excel_check.excel_to_csv import excel_to_csv
from excel_check.mysql_common import sql_connect


def scan_execl():
    excel_to_csv()
    sql_connect()