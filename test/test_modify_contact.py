from model.contact import Contact
from random import randrange


def test_modify_contact_first_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="testFirstName", middlename="testMiddleName", lastname="testLastName",
                                   nickname="testNickName", title="testTitle", company="testCompany",
                                   address="testAddress",
                                   homephone="testHomeTelephone", mobilephone="testMobileTelephone",
                                   workphone="testWorkTelephone", fax="testFax", email="testE-mail",
                                   email2="testE-Mail2", email3="testE-mail3",
                                   homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
                                   amonth="May", ayear="1998", secondaryaddress="testSecondaryAddress",
                                   secondaryhome="testSecondaryHome", secondarynotes="testSecondaryNotes"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="NewFirstName3", lastname="NewLastName3")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    l1 = sorted(old_contacts, key = Contact.id_or_max)
    l2 = sorted(new_contacts, key = Contact.id_or_max)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)


# def test_modify_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="testFirstName", middlename="testMiddleName", last_name="testLastName",
#                                    nickname="testNickName", title="testTitle", company="testCompany",
#                                    address="testAddress",
#                                    homephone="testHomeTelephone", mobilephone="testMobileTelephone",
#                                    workphone="testWorkTelephone", fax="testFax", email="testE-mail",
#                                    email2="testE-Mail2", email3="testE-mail3",
#                                    homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20",
#                                    amonth="May", ayear="1998", secondaryaddress="testSecondaryAddress",
#                                    secondary_home="testSecondaryHome", secondarynotes="testSecondaryNotes"))
#
#     app.contact.modify_first_contact(Contact(middlename="NewMiddleName"
#                                              ,last_name="NewLastName"
#                                              ,nickname="NewNickName"
#                                              ,title="NewTitle",company="NewCompany"
#                                              , address="NewAddress"
#                                              ,homephone="NewHomeTelephone"
#                                              ,mobilephone="NewMobileTelephone"
#                                              ,workphone="NewWorkTelephone"
#                                              ,fax="NewFax"
#                                              ,email="NewE-mail"
#                                              ,email2="NewE-mail2"
#                                              ,email3="NewE-mail3"
#                                              ,homepage="NewHomepage"
#                                              ,bday="20"
#                                              ,bmonth="May"
#                                              ,byear="1992"
#                                              ,aday="20"
#                                              ,amonth="May"
#                                              ,ayear="1992"
#                                              ,secondaryaddress="NewSecondaryAddress"
#                                              ,secondary_home="NewSecondaryHome"
#                                              ,secondarynotes="NewSecondaryNotes"))

#def test_modify_contact_middle_name(app):
#    app.contact.modify_first_contact(Contact(last_name="NewMiddleName"))


#def test_modify_contact_last_name(app):
#    app.contact.modify_first_contact(Contact(last_name="NewLastName"))


#def test_modify_contact_nick_name(app):
#    app.contact.modify_first_contact(Contact(nickname="NewNickName"))


#def test_modify_contact_title(app):
#    app.contact.modify_first_contact(Contact(title="NewTitle"))


#def test_modify_contact_company(app):
#    app.contact.modify_first_contact(Contact(company="NewCompany"))


#def test_modify_contact_address(app):
#    app.contact.modify_first_contact(Contact(address="NewAddress"))


#def test_modify_contact_home_telephone(app):
#    app.contact.modify_first_contact(Contact(homephone="NewHomeTelephone"))


#def test_modify_contact_mobile_telephone(app):
#    app.contact.modify_first_contact(Contact(mobilephone="NewMobileTelephone"))


#def test_modify_contact_work_telephone(app):
#    app.contact.modify_first_contact(Contact(workphone="NewWorkTelephone"))


#def test_modify_contact_fax(app):
#    app.contact.modify_first_contact(Contact(fax="NewFax"))


#def test_modify_contact_e_mail(app):
#    app.contact.modify_first_contact(Contact(email="NewE-mail"))


#def test_modify_contact_e_mail2(app):
#    app.contact.modify_first_contact(Contact(email2="NewE-Mail2"))


#def test_modify_contact_e_mail3(app):
#    app.contact.modify_first_contact(Contact(email3="NewE-Mail3"))


#def test_modify_contact_homepage(app):
#    app.contact.modify_first_contact(Contact(homepage="NewHomepage"))


#def test_modify_contact_bday(app):
#    app.contact.modify_first_contact(Contact(bday="20"))


#def test_modify_contact_bmonth(app):
#    app.contact.modify_first_contact(Contact(bmonth="May"))


#def test_modify_contact_byear(app):
#    app.contact.modify_first_contact(Contact(byear="1992"))


#def test_modify_contact_aday(app):
#    app.contact.modify_first_contact(Contact(aday="20"))


#def test_modify_contact_amonth(app):
#    app.contact.modify_first_contact(Contact(amonth="May"))


#def test_modify_contact_ayear(app):
#    app.contact.modify_first_contact(Contact(ayear="1992"))


#def test_modify_contact_secondary_address(app):
#    app.contact.modify_first_contact(Contact(secondaryaddress="NewSecondaryAddress"))


#def test_modify_contact_secondary_secondary_home(app):
#    app.contact.modify_first_contact(Contact(secondary_home="NewSecondaryHome"))


#def test_modify_contact_secondary_secondary_notes(app):
#    app.contact.modify_first_contact(Contact(secondarynotes="NewSecondaryNotes"))
