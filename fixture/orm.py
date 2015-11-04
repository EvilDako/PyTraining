__author__ = 'dako'
from pony.orm import *
from datetime import datetime
from model.contact import Contact
from model.group import Group
from pymysql.converters import decoders

class ORMFixture:

    db=Database()

    class ORMGroup(db.Entity):
        _table_='group_list'
        id = PrimaryKey(int, column='group_id')
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')


    class ORMContact(db.Entity):
        _table_='addressbook'
        id = PrimaryKey(int, column='id')
        firstname = Optional(str, column='firstname')
        middlename = Optional(str, column='middlename')
        lastname = Optional(str, column='lastname')
        nickname = Optional(str, column='nickname')
        company = Optional(str, column='company')
        title = Optional(str, column='title')
        address = Optional(str, column='address')
        tel_home = Optional(str, column='home')
        tel_mobile = Optional(str, column='mobile')
        tel_work = Optional(str, column='work')
        tel_fax = Optional(str, column='fax')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        email3 = Optional(str, column='email3')
        homepage = Optional(str, column='homepage')
        address2 = Optional(str, column='address2')
        phone2 = Optional(str, column='phone2')
        notes = Optional(str, column='notes')
        deprecated = Optional(datetime, column='deprecated')


    def __init__(self, host, port, database, user, password):
        self.db.bind('mysql', host=host, port=port, database=database, user=user, password=password, conv=decoders)
        self.db.generate_mapping()
        sql_debug(True)


    def convert_groups_to_model(self, groups):
        def convert(group):
            return Group(id=str(group.id), name=group.name, header=group.header, footer=group.footer)
        return list(map(convert, groups))

    def convert_contacts_to_model(self, contacts):
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname, lastname=contact.lastname)
        return list(map(convert, contacts))


    @db_session
    def get_group_list(self):
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))

    @db_session
    def get_contact_list(self):
        return self.convert_contacts_to_model(select(c for c in ORMFixture.ORMContact if c.deprecated is None))