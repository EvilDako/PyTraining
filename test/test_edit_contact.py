__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.contact import Contact
import random

def test_edit_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    contact_new = Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="PETRO", title="Mr", company="SUPERCOMPANY_2", address="Moscow, Old Arbat, 10",
                          tel_home="595555555", tel_mobile="89009009091", tel_work="495123555", tel_fax="+799999999", email="petrov@mail.ru", email2="petr@mail.ru", email3="petrovich@mail.ru", homepage="www.petrusha.com",
                          address2="none_2", phone2="none_2", notes="too many funny comments")
    contact_new.id = contact.id
    app.contact.edit_contact_by_id(contact.id, contact_new)
    new_contacts = db.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    #old_contacts[index] = contact
    #assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)