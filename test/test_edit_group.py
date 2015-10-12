__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="name_name", header="head_head"))
    old_groups = app.group.get_group_list()
    app.group.edit(Group(name="new_name", header="new_header", footer="new_footer"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
