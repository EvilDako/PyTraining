# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="GROUP_N", header="Header of the GROUP_N", footer="Footer of the GROUP_N"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.group.create(Group(name="", header="", footer=""))
    app.session.logout()

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit(Group(name="new_name", header="new_header", footer="new_footer"))
    app.session.logout()


def test_delete_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.delete()
    app.session.logout()
