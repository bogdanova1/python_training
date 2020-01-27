# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(first_name="testFirstName", middle_name="testMiddleName", last_name="testLastName", nick_name="testNickName", title="testTitle", company="testCompany", address="testAddress",
                               home_telephone="testHomeTelephone", mobile_telephone="testMobileTelephone", work_telephone="testWorkTelephone", fax="testFax", e_mail="testE-mail", e_mail2="testE-Mail2", e_mail3="testE-mail3",
                               homepage="testHomepage", bday="20", bmonth="May", byear="1992", aday="20", amonth="May", ayear="1998", secondary_address="testSecondaryAddress",
                               secondary_home="testSecondaryHome", secondary_notes="testSecondaryNotes"))


def test_add_empty_contact(app):
    app.contact.create(Contact(first_name="", middle_name="", last_name="", nick_name="", title="", company="", address="",
                               home_telephone="", mobile_telephone="", work_telephone="", fax="", e_mail="", e_mail2="", e_mail3="",
                               homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", secondary_address="",
                               secondary_home="", secondary_notes=""))

