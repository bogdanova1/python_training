from selenium.webdriver.support.ui import Select
from model.contact import Contact
import re

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def create(self, contact):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact, mode="create")
        # submit contact creation
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first_contact(self):
        self.delete_contact_by_index(self, 0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        # submit deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def modify_first_contact(self):
        wd = self.app.wd
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        self.select_contact_by_index(index)
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()
        # fill contact form
        self.fill_contact_form(new_contact_data, mode="edit")
        # submit edition
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def fill_contact_form(self, contact, mode):
        wd = self.app.wd
        self.app.change_field_value("firstname", contact.firstname)
        self.app.change_field_value("middlename", contact.middle_name)
        self.app.change_field_value("lastname", contact.lastname)
        self.app.change_field_value("nickname", contact.nick_name)
        self.app.change_field_value("title", contact.title)
        self.app.change_field_value("company", contact.company)
        self.app.change_field_value("address", contact.address)
        self.app.change_field_value("home", contact.homephone)
        self.app.change_field_value("mobile", contact.mobilephone)
        self.app.change_field_value("work", contact.workphone)
        self.app.change_field_value("fax", contact.fax)
        self.app.change_field_value("email", contact.email)
        self.app.change_field_value("email2", contact.email2)
        self.app.change_field_value("email3", contact.email3)
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
                wd.find_element_by_css_selector("option[value='"+contact.amonth.lower()+"']").click()
            else:
                wd.find_element_by_xpath("(//option[@value='"+contact.amonth+"'])[2]").click()
        self.app.change_field_value("ayear", contact.ayear)
        self.app.change_field_value("address2", contact.secondary_address)
        self.app.change_field_value("phone2", contact.secondaryphone)
        self.app.change_field_value("notes", contact.secondary_notes)

    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(
#                wd.find_elements_by_name("add"))) > 0:
                wd.find_elements_by_xpath("/html/body/div[1]/div[4]/form[2]/table/tbody/tr[1]/th[2]/a")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contacts_page()
        return len(wd.find_elements_by_name("selected[]"))

    def delete_all_contacts(self):
        wd = self.app.wd
        self.open_contacts_page()
        while self.count() > 0:
            # select first contact
            wd.find_element_by_name("selected[]").click()
            # submit deletion
            wd.find_element_by_xpath("//input[@value='Delete']").click()
            wd.switch_to.alert.accept()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contacts_page()
            self.contact_cache = []
#            for element in wd.find_elements_by_name('entry'):
            for element in wd.find_elements_by_xpath('//tr[@name="entry"]'):
                cells = element.find_elements_by_tag_name("td")
                firstname = cells[2].text
                lastname = cells[1].text
#                id = element.find_element_by_name('selected[]').get_attribute('value')
                id = element.find_element_by_tag_name('input').get_attribute('value')
                all_phones = cells[5].text
                address = cells[3].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(firstname= firstname, lastname= lastname, id = id, address = address,
                                                  all_phones_from_home_page=all_phones, all_emails_from_home_page=all_emails ))
        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name("td")[7]
        cell.find_elements_by_tag_name("a")[0].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        row = wd.find_elements_by_name('entry')[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_elements_by_tag_name("a")[0].click()

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name('firstname').get_attribute("value")
        lastname = wd.find_element_by_name('lastname').get_attribute("value")
        id = wd.find_element_by_name('id').get_attribute("value")
        homephone = wd.find_element_by_name('home').get_attribute("value")
        workphone = wd.find_element_by_name('work').get_attribute("value")
        mobilephone = wd.find_element_by_name('mobile').get_attribute("value")
        secondaryphone = wd.find_element_by_name('phone2').get_attribute("value")
        address = wd.find_element_by_name('address').get_attribute("value")
        email = wd.find_element_by_name('email').get_attribute("value")
        email2 = wd.find_element_by_name('email2').get_attribute("value")
        email3 = wd.find_element_by_name('email3').get_attribute("value")

        return Contact(firstname=firstname, lastname=lastname, id=id,
                       homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone,
                       address=address, email=email, email2=email2, email3=email3 )

    def get_from_view_page (self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone= self.searchwithNone("H", text)
        workphone= self.searchwithNone("W", text)
        mobilephone=self.searchwithNone("M", text)
        secondaryphone=self.searchwithNone("P", text)
        return Contact(homephone=homephone, workphone=workphone,
                       mobilephone=mobilephone, secondaryphone=secondaryphone)

    def searchwithNone(self, pref, text):
        if re.search(pref, text) is None :
            return None
        else:
            return re.search(pref+": (.*)", text).group(1)
