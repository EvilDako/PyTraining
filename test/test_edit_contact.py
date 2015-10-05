__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_edit_contact(app):
    app.contact.edit(Contact(firstname="Petr", middlename="Petrovich", lastname="Petrov", nickname="PETRO", title="Mr", company="SUPERCOMPANY_2", address="Moscow, Old Arbat, 10",
                          tel_home="595555555", tel_mobile="89009009091", tel_work="495123555", tel_fax="+799999999", email="petrov@mail.ru", email2="petr@mail.ru", email3="petrovich@mail.ru", homepage="www.petrusha.com",
                          address2="none_2", phone2="none_2", notes="too many funny comments"))
