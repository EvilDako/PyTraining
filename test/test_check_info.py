__author__ = 'dako'
import re
from random import randrange


#Проверка телефонных номеров
def test_phones_on_home_page(app, db):
    cont = app.contact.get_contact_list()
    for i, c in enumerate(cont):
        contact_from_home_page = c
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contact_from_db = db.get_contact_by_id(c.id)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_db)


def test_phones_on_contact_view_page(app, db):
    cont = app.contact.get_contact_list()
    for i, c in enumerate(cont):
        contact_from_view_page = app.contact.get_contact_from_view_page(i)
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contact_from_db = db.get_contact_by_id(c.id)
        assert contact_from_view_page.tel_home == contact_from_edit_page.tel_home == contact_from_db.tel_home
        assert contact_from_view_page.tel_work == contact_from_edit_page.tel_work == contact_from_db.tel_work
        assert contact_from_view_page.tel_mobile == contact_from_edit_page.tel_mobile == contact_from_db.tel_mobile
        assert contact_from_view_page.phone2 == contact_from_edit_page.phone2 == contact_from_db.tel_phone2

#Проверка адреса
def test_address_on_home_page(app, db):
    cont = app.contact.get_contact_list()
    for i, c in enumerate(cont):
        contact_from_home_page = app.contact.get_contact_list()[i]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contact_from_db = db.get_contact_by_id(c.id)
        assert contact_from_home_page.address == contact_from_edit_page.address == contact_from_db.address

#Проверка фамилии
def test_lastname_on_home_page(app, db):
    cont = app.contact.get_contact_list()
    for i, c in enumerate(cont):
        contact_from_home_page = app.contact.get_contact_list()[i]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contact_from_db = db.get_contact_by_id(c.id)
        assert contact_from_home_page.lastname == contact_from_edit_page.lastname == contact_from_db.lastname

#Проверка имени
def test_firstname_on_home_page(app, db):
    cont = app.contact.get_contact_list()
    for i, c in enumerate(cont):
        contact_from_home_page = app.contact.get_contact_list()[i]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contact_from_db = db.get_contact_by_id(c.id)
        assert contact_from_home_page.firstname == contact_from_edit_page.firstname == contact_from_db.firstname

#Проверка адресов электронной почты
def test_emails_on_home_page(app, db):
    cont = app.contact.get_contact_list()
    for i, c in enumerate(cont):
        contact_from_home_page = app.contact.get_contact_list()[i]
        contact_from_edit_page = app.contact.get_contact_info_from_edit_page(i)
        contact_from_db = db.get_contact_by_id(c.id)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_db)


def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.tel_home, contact.tel_mobile, contact.tel_work, contact.phone2]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3])))