__author__ = 'dako'
from fixture.orm import ORMFixture

db = ORMFixture(host="localhost", port=8926, database='addressbook', user="root", password="")

try:
    l = db.get_contact_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass # db.destroy()
