__author__ = 'dako'
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def create(self, contact):
        wd = self.app.wd
        # init creation new contact
        wd.find_element_by_link_text("add new").click()
        # fill new contact form
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.tel_home)
        self.change_field_value("mobile", contact.tel_mobile)
        self.change_field_value("work", contact.tel_work)
        self.change_field_value("fax", contact.tel_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("homepage", contact.homepage)
        # submit creation new contact
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.contact_cache = None

    def edit(self, contact):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        # modify contact information
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.tel_home)
        self.change_field_value("mobile", contact.tel_mobile)
        self.change_field_value("work", contact.tel_work)
        self.change_field_value("fax", contact.tel_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("homepage", contact.homepage)
        #submit updating
        wd.find_element_by_name("update").click()
        #return to home page
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_to_edit_by_id(id)
        # modify contact information
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.tel_home)
        self.change_field_value("mobile", contact.tel_mobile)
        self.change_field_value("work", contact.tel_work)
        self.change_field_value("fax", contact.tel_fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)
        self.change_field_value("homepage", contact.homepage)
        self.change_field_value("homepage", contact.homepage)
        #submit updating
        wd.find_element_by_name("update").click()
        #return to home page
        wd.find_element_by_link_text("home page").click()
        self.contact_cache = None

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath(".//*[@href='edit.php?id=%s']" % id).click()


    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_element_by_tag_name("a").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def delete (self, index):
        self.delete_contact_by_index(0)

    #delete contact
    def delete_contact_by_index(self, index):
        wd = self.app.wd
        # open contacts list
        self.open_contact_list()
        self.select_contact_by_index(index)
        # press delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # close submit window
        wd.switch_to_alert().accept()
        # return to home page
        self.open_contact_list()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        # open contacts list
        self.open_contact_list()
        self.select_contact_by_id(id)
        # press delete button
        wd.find_element_by_xpath("//div[@id='content']/form[2]/div[2]/input").click()
        # close submit window
        wd.switch_to_alert().accept()
        # return to home page
        self.open_contact_list()
        self.contact_cache = None


    def open_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_xpath(".//*[@id='%s']" % id).click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    def add_to_group(self, group):
        wd = self.app.wd
        wd.find_element_by_name("to_group").click()
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[4]/select/option[text()='%s'][1]" % group).click()
        wd.find_element_by_name("add").click()

    def delete_from_group(self):
        pass

    def check_contact_in_group(self, group):
        pass
        """
        проверить в выбранной группе наличие контакта по id
        """



    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache=[]
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                all_phones = cells[5].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, address=address, id=id,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        tel_home = wd.find_element_by_name("home").get_attribute("value")
        tel_work = wd.find_element_by_name("work").get_attribute("value")
        tel_mobile = wd.find_element_by_name("mobile").get_attribute("value")
        phone2 = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(lastname=lastname, firstname=firstname, id=id,
                       tel_home=tel_home, tel_work=tel_work, tel_mobile=tel_mobile, phone2=phone2,
                       address=address, email=email, email2=email2, email3=email3)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        tel_home = re.search("H: (.*)", text).group(1)
        tel_work = re.search("W: (.*)", text).group(1)
        tel_mobile = re.search("M: (.*)", text).group(1)
        phone2 = re.search("P: (.*)", text).group(1)
        return Contact(tel_home=tel_home, tel_work=tel_work, tel_mobile=tel_mobile, phone2=phone2)

    def get_group_list_from_contact_page(self):
        wd = self.app.wd
        l = wd.find_elements_by_name