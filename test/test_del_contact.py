from model.contact import Contact

#def test_delete_all_contacts(app):
#    app.contact.delete_all_contacts()

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="testFirstName", middle_name="testMiddleName", last_name="testLastName",
                                   nick_name="testNickName", title="testTitle", company="testCompany",
                                   address="testAddress",
                                   home_telephone="testHomeTelephone", mobile_telephone="testMobileTelephone",
                                   work_telephone="testWorkTelephone", fax="testFax", e_mail="testE-mail",
                                   e_mail2="testE-Mail2", e_mail3="testE-mail3",
                                   homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
                                   amonth="May", ayear="1998", secondary_address="testSecondaryAddress",
                                   secondary_home="testSecondaryHome", secondary_notes="testSecondaryNotes"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_first_contact()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)