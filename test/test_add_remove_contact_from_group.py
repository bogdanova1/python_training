from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db2 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_remove_contact_from_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name = "test"))
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(firstname="testFirstName", middlename="testMiddleName", lastname="testLastName",
                                   nickname="testNickName", title="testTitle", company="testCompany",
                                   address="testAddress",
                                   homephone="testHomeTelephone", mobilephone="testMobileTelephone",
                                   workphone="testWorkTelephone", fax="testFax", email="testE-mail",
                                   email2="testE-Mail2", email3="testE-mail3",
                                   homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
                                   amonth="May", ayear="1998", secondaryaddress="testSecondaryAddress",
                                   secondaryhome="testSecondaryHome", secondarynotes="testSecondaryNotes"))
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
 #   index = contacts.index(contact)
    groups = db.get_group_list()
    group = random.choice(groups)
    app.contact.add_contact_to_group(contact, group)
    try:
        l = db2.get_contacts_in_group(Group(id=group.id))
        assert (contact in l) == True
    finally:
        pass
    app.contact.remove_contact_from_group(contact, group)
    try:
        l = db2.get_contacts_not_in_group(Group(id=group.id))
        assert (contact in l) == True
    finally:
        pass
