__author__ = 'dako'
from mysql import connector
from model.group import Group
from model.contact import Contact

class DbFixture():
    def __init__(self, host, port, database, user, password):
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = connector.connect(host=host, port=port, database=database, user=user, password=password)
        self.connection.autocommit = True


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title," \
                           "address, home, mobile, work, fax, email, email2, email3, homepage," \
                           "address2, phone2, notes from addressbook where deprecated = '0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, title, company,
                 address, tel_home, tel_mobile, tel_work, tel_fax, email, email2,
                 email3, homepage, address2, phone2, notes) = row
                list.append(Contact(id=str(id), firstname=firstname, middlename=middlename,
                                    lastname=lastname, nickname=nickname, company=company,
                                    title=title, address=address, tel_home=tel_home,
                                    tel_mobile=tel_mobile, tel_work=tel_work, tel_fax=tel_fax,
                                    email=email,email2=email2, email3=email3, homepage=homepage,
                                    address2=address2, phone2=phone2, notes=notes))
        finally:
            cursor.close()
        return list

    def get_contact_by_id(self, id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, middlename, lastname, nickname, company, title," \
                           "address, home, mobile, work, fax, email, email2, email3, homepage," \
                           "address2, phone2, notes from addressbook where id = %s and deprecated = '0000-00-00 00:00:00'" % id)
            for row in cursor:
                (id, firstname, middlename, lastname, nickname, title, company,
                 address, tel_home, tel_mobile, tel_work, tel_fax, email, email2,
                 email3, homepage, address2, phone2, notes) = row
        finally:
            cursor.close()
        return Contact(id=str(id), firstname=firstname, middlename=middlename,
                                    lastname=lastname, nickname=nickname, company=company,
                                    title=title, address=address, tel_home=tel_home,
                                    tel_mobile=tel_mobile, tel_work=tel_work, tel_fax=tel_fax,
                                    email=email,email2=email2, email3=email3, homepage=homepage,
                                    address2=address2, phone2=phone2, notes=notes)



    def destroy(self):
        self.connection.close()