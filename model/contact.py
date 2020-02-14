from sys import maxsize


class Contact:

    def __init__(self, firstname = None, middle_name = None, lastname = None, nick_name = None, title = None, company = None, address = None,
                 homephone = None, mobilephone = None, workphone = None, fax = None, email = None, email2 = None, email3 = None,
                 homepage = None, bday = None, bmonth = None, byear = None, aday = None, amonth = None, ayear = None, secondary_address = None,
                 secondary_notes = None, secondaryphone = None, id = None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middle_name = middle_name
        self.lastname = lastname
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.address = address
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.fax = fax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secondary_address = secondary_address
        self.secondary_notes = secondary_notes
        self.secondaryphone = secondaryphone
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page
        self.id = id

    def __repr__(self):
        return "%s, %s, %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
       return (self.id is None or other.id is None or self.id == other.id) \
              and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize





