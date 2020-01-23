from model.contact import Contact

def test_edit_first_contact(app):
    app.session.login( username="admin", password="secret")
    app.contact.edit_first_contact(Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName", nick_name="NickName", title="Title", company="Company", address="Address",
                               home_telephone="HomeTelephone", mobile_telephone="MobileTelephone", work_telephone="WorkTelephone", fax="Fax", e_mail="E-mail", e_mail2="E-Mail2", e_mail3="E-mail3",
                               homepage="Homepage", bday="10", bmonth="March", byear="1990", aday="10", amonth="March", ayear="1999", secondary_address="SecondaryAddress",
                               secondary_home="SecondaryHome", secondary_notes="SecondaryNotes"))
    app.session.logout()

