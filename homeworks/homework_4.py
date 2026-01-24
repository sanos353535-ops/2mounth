class Contact:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
    @classmethod
    def validate_phone_number(cls,phone_number):
        if phone_number.isdigit() and len(phone_number) == 10:
            return True
        else:
            return False
class Contactlist:
    all_contacts = []

    @classmethod
    def add_contact(cls,name,phone_number):
        if Contact.validate_phone_number(phone_number):
            new_contact = Contact(name, phone_number)
            cls.all_contacts.append(new_contact)

        else:
            raise ValueError('number error')
