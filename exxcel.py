import mysql.connector
from openpyxl import Workbook

def main():

    # Connect to DB -----------------------------------------------------------
    db = mysql.connector.connect( user='root', password='', host='127.0.0.1')
    cur = db.cursor()
    database = 'panelpf'
    SQL = 'USE ' + database + ';'
    cur.execute(SQL)
    table_name = 'parametros'
    # Create Excel (.xlsx) file -----------------------------------------------
    wb = Workbook()

    SQL = 'SELECT * from '+ table_name + ';'
    cur.execute(SQL)
    results = cur.fetchall()
    ws = wb.create_sheet(0)
    ws.title = table_name
    ws.append(cur.column_names)
    for row in results:
        ws.append(row)

    workbook_name = 'datainfo'
    wb.save(workbook_name + ".xlsx")


