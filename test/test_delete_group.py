__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete()
    app.session.logout()
