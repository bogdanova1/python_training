from model.contact import Contact
from model.group import Group
from fixture.orm import ORMFixture
import random

db2 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

def test_add_remove_contact_from_group(app, db, check_ui):
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
                                   secondaryphone="testSecondaryPhone", secondarynotes="testSecondaryNotes"))

    groups = db.get_group_list()
    group, contact = None, None
    for g in groups:
        try:
            l = db2.get_contacts_not_in_group(Group(id=g.id))
            if len(l)>0:
                contact = random.choice(l)
                group = g
                break
        finally:
            pass
    if group is None:
        app.group.create(Group(name="test"))
        group = sorted(db.get_group_list(), key=Group.id_or_max)[-1]
        l = db2.get_contacts_not_in_group(Group(id=group.id))
        if len(l) > 0:
            contact = random.choice(l)
        else:
            app.contact.create(Contact(firstname="testFirstName", middlename="testMiddleName", lastname="testLastName",
                                       nickname="testNickName", title="testTitle", company="testCompany",
                                       address="testAddress",
                                       homephone="testHomeTelephone", mobilephone="testMobileTelephone",
                                       workphone="testWorkTelephone", fax="testFax", email="testE-mail",
                                       email2="testE-Mail2", email3="testE-mail3",
                                       homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
                                       amonth="May", ayear="1998", secondaryaddress="testSecondaryAddress",
                                       secondaryphone="testSecondaryPhone", secondarynotes="testSecondaryNotes"))
            contact = sorted(db.get_contact_list(), key=Contact.id_or_max)[-1]
    app.contact.add_contact_to_group(contact, group)
    try:
        l = db2.get_contacts_in_group(Group(id=group.id))
        assert (contact in l) == True
    finally:
        pass
