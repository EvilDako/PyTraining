__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name_name", header="head_head"))
    app.group.edit(Group(name="new_name", header="new_header", footer="new_footer"))
