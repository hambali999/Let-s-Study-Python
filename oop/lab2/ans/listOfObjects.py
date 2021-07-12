class Contact:
    def __init__(self, name, phone):
        self._name = name
        self._phone = phone

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        self._phone = phone

    def __str__(self):
        return f'Name: {self._name} Phone: {self._phone}'


class Phone:
    def __init__(self, name):
        self._name = name
        self._contacts = []

    def addContact(self, name, phone):
        self._contacts.append(Contact(name, phone))

    def search(self, name):  ## When dealing with object always return None if not found
        for contact in self._contacts:
            if contact.name == name:
                return contact

    def remove(self, name):
        contact = self.search(name)
        if contact is not None:
            self._contacts.remove(contact)
            return True
        return False

    def __str__(self):
        return f"Name: {self._name} Contacts: [{', '.join(str(c) for c in self._contacts)}]"


def test():
    p = Phone('Joe')
    p.addContact('James', 11111111)
    p.addContact('John', 22222222)
    contact = p.search('James')
    if contact is not None:
        print(contact)
    else:
        print('Contact not found')

    removed = p.remove('John')
    if removed:
        print('Removed')
    else:
        print('User is not found')


if __name__ == '__main__':
    test()
