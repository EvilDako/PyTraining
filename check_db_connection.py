__author__ = 'dako'
from mysql import connector

connection = connector.connect(host="localhost", port='8926', database='addressbook', user="root", password="")

try:
    cursor = connection.cursor()
    cursor.execute("select * from group_list")
    for row in cursor.fetchall():
        print(row)

finally:
    connection.close()
