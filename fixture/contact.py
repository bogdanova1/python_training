from selenium.webdriver.support.ui import Select

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # fill contact form
        self.fill_contact_form(contact, mode="create")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()

    def modify_first_contact(self,contact):
        wd = self.app.wd
        self.open_home_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        # fill contact form
        self.fill_contact_form(contact, mode="edit")
        # submit edition
        wd.find_element_by_name("update").click()

    def fill_contact_form(self, contact, mode):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.first_name)
        self.app.change_field_value("middlename", contact.middle_name)
        self.app.change_field_value("lastname", contact.last_name)
        self.app.change_field_value("nickname", contact.nick_name)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.home_telephone)
        self.app.change_field_value("mobile", contact.mobile_telephone)
        self.app.change_field_value("work", contact.work_telephone)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email", contact.e_mail)
        self.app.change_field_value("email2", contact.e_mail2)
        self.app.change_field_value("email3", contact.e_mail3)
        self.app.change_field_value("homepage", contact.homepage)
        if contact.bday is not None:
            wd.find_element_by_name("bday").click()
            Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday)
            wd.find_element_by_xpath("//option[@value='"+contact.bday+"']").click()
        if contact.bmonth is not None:
            wd.find_element_by_name("bmonth").click()
            Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bmonth)
            wd.find_element_by_xpath("//option[@value='"+contact.bmonth+"']").click()
        self.app.change_field_value("byear", contact.byear)
        if contact.aday is not None:
            wd.find_element_by_name("aday").click()
            Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.aday)
            wd.find_element_by_xpath("(//option[@value='"+contact.aday+"'])[2]").click()
        if contact.amonth is not None:
            wd.find_element_by_name("amonth").click()
            Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.amonth)
            if mode == "edit":
                wd.find_element_by_css_selector("option[value=\""+contact.amonth.lower()+"\"]").click()
            else:
                wd.find_element_by_xpath("(//option[@value='"+contact.amonth+"'])[2]").click()
        self.app.change_field_value("ayear", contact.ayear)
        self.app.change_field_value("address2", contact.secondary_address)
        self.app.change_field_value("phone2", contact.secondary_home)
        self.app.change_field_value("notes", contact.secondary_notes)

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_name("add"))) > 0:
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_home_page()
        while self.count() > 0:
            # select first contact
            wd.find_element_by_name("selected[]").click()
            # submit deletion
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            wd.switch_to.alert.accept()

