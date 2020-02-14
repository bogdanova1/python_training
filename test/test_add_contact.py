# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="testFirstName", middle_name="testMiddleName", lastname="testLastName", nick_name="testNickName", title="testTitle", company="testCompany", address="testAddress",
                      homephone="testHomeTelephone", mobilephone="testMobileTelephone", workphone="testWorkTelephone", fax="testFax", email="testE-mail", email2="testE-Mail2", email3="testE-mail3",
                      homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20", amonth="May", ayear="1998", secondary_address="testSecondaryAddress",
                      secondary_notes="testSecondaryNotes", secondaryphone="testSecondaryphone")
    app.contact.create(contact)
    assert len(old_contacts)+1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


# def test_add_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", middle_name="", lastname="", nick_name="", title="", company="", address="",
#                                homephone="", mobilephone="", workphone="", fax="", email="", email2="", email3="",
#                                homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", secondary_address="",
#                                secondaryphone="", secondary_notes="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts)+1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
