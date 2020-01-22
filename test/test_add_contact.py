# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="FirstName", middle_name="MiddleName", last_name="LastName", nick_name="NickName", title="Title", company="Company", address="Address",
                        home_telephone="HomeTelephone", mobile_telephone="MobileTelephone", work_telephone="WorkTelephone", fax="Fax", e_mail="E-mail", e_mail2="E-Mail2", e_mail3="E-mail3",
                        homepage="Homepage", bday="10", bmonth="March", byear="1990", aday="10", amonth="March", ayear="1999", secondary_address="SecondaryAddress",
                        secondary_home="SecondaryHome", secondary_notes="SecondaryNotes"))
    app.logout()


def test_add_empty_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(first_name="", middle_name="", last_name="", nick_name="", title="", company="", address="",
                        home_telephone="", mobile_telephone="", work_telephone="", fax="", e_mail="", e_mail2="", e_mail3="",
                        homepage="", bday="-", bmonth="-", byear="", aday="-", amonth="-", ayear="", secondary_address="",
                        secondary_home="", secondary_notes=""))
    app.logout()
