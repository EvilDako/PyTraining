# -*- coding: utf-8 -*-
from model.contact import Contact
import pytest
import random
import string

def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [
    Contact(firstname=firstname, middlename=middlename, lastname=lastname, nickname=nickname, title=title, company=company, address=address, tel_home=tel_home, email=email)
    for firstname in ["", random_string("firstname", 15)]
    for middlename in ["", random_string("middlename", 15)]
    for lastname in ["", random_string("lastname", 15)]
    for nickname in ["", random_string("nickname", 15)]
    for title in ["", random_string("title", 15)]
    for company in ["", random_string("company", 15)]
    for address in ["", random_string("address", 30)]
    for tel_home in ["", random_string("tel_home", 15)]
    for email in ["", random_string("email", 15)]
]

@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == app.contact.count()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)