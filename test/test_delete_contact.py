__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.contact import Contact


def test_delete_contact(app):
    app.contact.delete()
