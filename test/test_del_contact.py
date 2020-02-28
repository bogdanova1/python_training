from model.contact import Contact
import random


def test_delete_first_contact(app, db, check_ui):
    if db.contact.count() == 0:
        app.contact.create(Contact(firstname="testFirstName", middlename="testMiddleName", lastname="testLastName",
                                   nickname="testNickName", title="testTitle", company="testCompany",
                                   address="testAddress",
                                   homephone="testHomeTelephone", mobilephone="testMobileTelephone",
                                   workphone="testWorkTelephone", fax="testFax", email="testE-mail",
                                   email2="testE-Mail2", email3="testE-mail3",
                                   homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
                                   amonth="May", ayear="1998", secondaryaddress="testSecondaryAddress",
                                   secondary_home="testSecondaryHome", secondarynotes="testSecondaryNotes"))
    old_contacts = db.contact.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_contact_by_id(contact.id)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = db.contact.get_contact_list()
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(old_contacts, key = Contact.id_or_max) == sorted(app.contact.get_contact_list(), key = Contact.id_or_max)