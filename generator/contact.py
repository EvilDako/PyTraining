__author__ = 'dako'
from model.contact import Contact
import random
import string
import os.path
import json
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n=5
f="data/contacts.json"

for o, a in opts:
    if o == "-n":
        n=int(a)
    elif o == "-f":
        f = a

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", address="", tel_home="", email="")] + [
    Contact(firstname=random_string("firstname", 15), middlename=random_string("middlename", 15),
            lastname=random_string("lastname", 15), nickname=random_string("nickname", 15),
            title=random_string("title", 15), company=random_string("company", 15),
            address=random_string("address", 30), tel_home=random_string("tel_home", 15), email=random_string("email", 15))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    out.write(json.dumps(testdata, default=lambda x: x.__dict__, indent=2))