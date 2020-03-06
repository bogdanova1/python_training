from fixture.db import DbFixture
from fixture.orm import ORMFixture
from fixture.group import Group

# db1 = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")
#
# try:
#     contacts = db1.get_contact_list()
#     for contact in contacts:
#         print(contact)
#     print(len(contacts))
# finally:
#     db1.destroy()

db2 = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = db2.get_contacts_in_group(Group(id="332"))
    for item in l:
        print(item)
    print(len(l))
finally:
    pass
