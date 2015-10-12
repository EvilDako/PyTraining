# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="VANO", title="Sir", company="SUPERCOMPANY", address="Moscow, Old Arbat, 9",
                          tel_home="495555555", tel_mobile="89009009090", tel_work="495123456", tel_fax="+899999999", email="ivanov@mail.ru", email2="ivan@mail.ru", email3="ivanovich@mail.ru", homepage="www.vanyusha.com",
                          address2="none", phone2="none", notes="many funny comments")
    app.contact.create(contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)