__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.contact import Contact
from random import randrange

def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="PETRO", title="Mr", company="SUPERCOMPANY_2", address="Moscow, Old Arbat, 10",
                          tel_home="595555555", tel_mobile="89009009091", tel_work="495123555", tel_fax="+799999999", email="petrov@mail.ru", email2="petr@mail.ru", email3="petrovich@mail.ru", homepage="www.petrusha.com",
                          address2="none_2", phone2="none_2", notes="too many funny comments")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == app.contact.count()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)