from model.contact import Contact

def test_data_on_home_page(app, db):
    db_contacts = db.get_contact_list()
    contacts  = app.contact.get_contact_list()
    assert sorted(db_contacts, key=Contact.id_or_max) == sorted(contacts, key=Contact.id_or_max)

