__author__ = 'dako'
# -*- coding: utf-8 -*-
from model.group import Group
import random

def test_edit_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="name_name", header="head_head"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    group_new = Group(name="new_name", header="new_header", footer="new_footer")
    group_new.id = group.id
    app.group.edit_group_by_id(group.id, group_new)
    new_groups = db.get_group_list()
    #assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)