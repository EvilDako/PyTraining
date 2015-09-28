# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="VANO", title="Sir", company="SUPERCOMPANY", address="Moscow, Old Arbat, 9",
                          tel_home="495555555", tel_mobile="89009009090", tel_work="495123456", tel_fax="+899999999", email="ivanov@mail.ru", email2="ivan@mail.ru", email3="ivanovich@mail.ru", homepage="www.vanyusha.com",
                          address2="none", phone2="none", notes="many funny comments"))
    app.session.logout()


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="PETRO", title="Mr", company="SUPERCOMPANY_2", address="Moscow, Old Arbat, 10",
                          tel_home="595555555", tel_mobile="89009009091", tel_work="495123555", tel_fax="+799999999", email="petrov@mail.ru", email2="petr@mail.ru", email3="petrovich@mail.ru", homepage="www.petrusha.com",
                          address2="none_2", phone2="none_2", notes="too many funny comments"))
    app.session.logout()


def test_delete_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.delete()
    app.session.logout()