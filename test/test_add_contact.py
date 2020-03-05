# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app, json_contacts, db, check_ui):
    contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    app.wd.implicitly_wait(2)
    assert len(old_contacts)+1 == len(db.get_contact_list())
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)
    if check_ui:
        assert sorted(old_contacts, key = Contact.id_or_max) == sorted(new_contacts, key = Contact.id_or_max)

