from model.contact import Contact


def test_modify_contact_first_name(app):
    app.contact.modify_first_contact(Contact(first_name="NewFirstName"))


def test_modify_contact(app):
    app.contact.modify_first_contact(Contact(middle_name="NewMiddleName"
                                             ,last_name="NewLastName"
                                             ,nick_name="NewNickName"
                                             ,title="NewTitle",company="NewCompany"
                                             , address="NewAddress"
                                             ,home_telephone="NewHomeTelephone"
                                             ,mobile_telephone="NewMobileTelephone"
                                             ,work_telephone="NewWorkTelephone"
                                             ,fax="NewFax"
                                             ,e_mail="NewE-mail"
                                             ,e_mail2="NewE-mail2"
                                             ,e_mail3="NewE-mail3"
                                             ,homepage="NewHomepage"
                                             ,bday="20"
                                             ,bmonth="May"
                                             ,byear="1992"
                                             ,aday="20"
                                             ,amonth="May"
                                             ,ayear="1992"
                                             ,secondary_address="NewSecondaryAddress"
                                             ,secondary_home="NewSecondaryHome"
                                             ,secondary_notes="NewSecondaryNotes"))

#def test_modify_contact_middle_name(app):
#    app.contact.modify_first_contact(Contact(last_name="NewmMiddleName"))


#def test_modify_contact_last_name(app):
#    app.contact.modify_first_contact(Contact(last_name="NewLastName"))


#def test_modify_contact_nick_name(app):
#    app.contact.modify_first_contact(Contact(nick_name="NewNickName"))


#def test_modify_contact_title(app):
#    app.contact.modify_first_contact(Contact(title="NewTitle"))


#def test_modify_contact_company(app):
#    app.contact.modify_first_contact(Contact(company="NewCompany"))


#def test_modify_contact_address(app):
#    app.contact.modify_first_contact(Contact(address="NewAddress"))


#def test_modify_contact_home_telephone(app):
#    app.contact.modify_first_contact(Contact(home_telephone="NewHomeTelephone"))


#def test_modify_contact_mobile_telephone(app):
#    app.contact.modify_first_contact(Contact(mobile_telephone="NewMobileTelephone"))


#def test_modify_contact_work_telephone(app):
#    app.contact.modify_first_contact(Contact(work_telephone="NewWorkTelephone"))


#def test_modify_contact_fax(app):
#    app.contact.modify_first_contact(Contact(fax="NewFax"))


#def test_modify_contact_e_mail(app):
#    app.contact.modify_first_contact(Contact(e_mail="NewE-mail"))


#def test_modify_contact_e_mail2(app):
#    app.contact.modify_first_contact(Contact(e_mail2="NewE-Mail2"))


#def test_modify_contact_e_mail3(app):
#    app.contact.modify_first_contact(Contact(e_mail3="NewE-Mail3"))


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
#    app.contact.modify_first_contact(Contact(secondary_address="NewSecondaryAddress"))


#def test_modify_contact_secondary_secondary_home(app):
#    app.contact.modify_first_contact(Contact(secondary_home="NewSecondaryHome"))


#def test_modify_contact_secondary_secondary_notes(app):
#    app.contact.modify_first_contact(Contact(secondary_notes="NewSecondaryNotes"))
