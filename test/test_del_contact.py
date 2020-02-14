from model.contact import Contact
from random import randrange

#def test_delete_all_contacts(app):
#    app.contact.delete_all_contacts()

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testFirstName", middlename="testMiddleName", lastname="testLastName",
                                   nickname="testNickName", title="testTitle", company="testCompany",
                                   address="testAddress",
                                   homephone="testHomeTelephone", mobilephone="testMobileTelephone",
                                   workphone="testWorkTelephone", fax="testFax", email="testE-mail",
                                   email2="testE-Mail2", email3="testE-mail3",
                                   homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
                                   amonth="May", ayear="1998", secondaryaddress="testSecondaryAddress",
                                   secondary_home="testSecondaryHome", secondarynotes="testSecondaryNotes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)