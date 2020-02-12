from model.contact import Contact
from random import randrange

#def test_delete_all_contacts(app):
#    app.contact.delete_all_contacts()

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testFirstName", middle_name="testMiddleName", lastname="testLastName",
                                   nick_name="testNickName", title="testTitle", company="testCompany",
                                   address="testAddress",
                                   homephone="testHomeTelephone", mobilephone="testMobileTelephone",
                                   workphone="testWorkTelephone", fax="testFax", e_mail="testE-mail",
                                   e_mail2="testE-Mail2", e_mail3="testE-mail3",
                                   homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
                                   amonth="May", ayear="1998", secondary_address="testSecondaryAddress",
                                   secondary_home="testSecondaryHome", secondary_notes="testSecondaryNotes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    assert len(old_contacts) - 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index:index+1] = []
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)