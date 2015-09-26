# -*- coding: utf-8 -*-
import pytest
from contact import Contact
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.contact_creation(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="VANO", title="Sir", company="SUPERCOMPANY", address="Moscow, Old Arbat, 9",
                          tel_home="495555555", tel_mobile="89009009090", tel_work="495123456", tel_fax="+899999999", email="ivanov@mail.ru", email2="ivan@mail.ru", email3="ivanovich@mail.ru", homepage="www.vanyusha.com",
                          address2="none", phone2="none", notes="many funny comments"))
    app.logout()
