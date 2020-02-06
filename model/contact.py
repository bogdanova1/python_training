from sys import maxsize


class Contact:

    def __init__(self, first_name = None, middle_name = None, last_name = None, nick_name = None, title = None, company = None, address = None,
                            home_telephone = None, mobile_telephone = None, work_telephone = None, fax = None, e_mail = None, e_mail2 = None, e_mail3 = None,
                            homepage = None, bday = None, bmonth = None, byear = None, aday = None, amonth = None, ayear = None, secondary_address = None,
                            secondary_home = None, secondary_notes = None, id = None):
        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.nick_name = nick_name
        self.title = title
        self.company = company
        self.address = address
        self.home_telephone = home_telephone
        self.mobile_telephone = mobile_telephone
        self.work_telephone = work_telephone
        self.fax = fax
        self.e_mail = e_mail
        self.e_mail2 = e_mail2
        self.e_mail3 = e_mail3
        self.homepage = homepage
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.aday = aday
        self.amonth = amonth
        self.ayear = ayear
        self.secondary_address = secondary_address
        self.secondary_home = secondary_home
        self.secondary_notes = secondary_notes
        self.id = id

    def __repr__(self):
        return "%s, %s, %s" % (self.id, self.first_name, self.last_name)

    def __eq__(self, other):
       return (self.id is None or other.id is None or self.id == other.id) and self.first_name == other.first_name and self.last_name == other.last_name

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize





