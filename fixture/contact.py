__author__ = 'dako'
from model.contact import Contact

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
        # open contacts list
        self.open_contact_list()
        self.select_contact_by_index(index)
        # press edit button
        wd.find_element_by_css_selector('img[alt="Edit"]').click()
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

    def open_contact_list(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/index.php")):
            wd.find_element_by_link_text("home").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()


    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_list()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_list()
            self.contact_cache=[]
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                lastname = cells[1].text
                firstname = cells[2].text
                #тут получал ФИО из атрибута чекбокса
                #text = element.find_element_by_name("selected[]").get_attribute("title")
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return list(self.contact_cache)
