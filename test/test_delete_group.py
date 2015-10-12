__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.group import Group


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name_name", header="head_head"))
    old_groups = app.group.get_group_list()
    app.group.delete()
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
