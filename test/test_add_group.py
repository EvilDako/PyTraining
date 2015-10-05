# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    app.group.create(Group(name="GROUP_N", header="Header of the GROUP_N", footer="Footer of the GROUP_N"))

def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
