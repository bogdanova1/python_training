import re
from random import randrange

def test_phone_on_home_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_home_page = app.contact.get_contact_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.address == contact_from_edit_page.address
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(contact_from_edit_page)

def test_phone_on_contact_view_page(app):
    index = randrange(len(app.contact.get_contact_list()))
    contact_from_view_page = app.contact.get_from_view_page(index)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert merge_phones_like_on_home_page(contact_from_view_page) == merge_phones_like_on_home_page(contact_from_edit_page)
    assert merge_emails_like_on_home_page(contact_from_edit_page) == contact_from_view_page.all_emails_from_view_page
    # assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    # assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
    # assert contact_from_view_page.workphone == contact_from_edit_page.workphone
    # assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone

def clear(s):
    return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                     map(lambda x: clear(x),
                         filter(lambda x: x is not None, [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "" and x is not None, map(lambda x: re.sub(" ","",x),[contact.email, contact.email2, contact.email3])))