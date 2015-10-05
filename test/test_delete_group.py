__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name_name", header="head_head"))
    app.group.delete()
