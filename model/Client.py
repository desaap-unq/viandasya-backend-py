from model import VirtualWallet


class Client:
    def __init__(self, name, surname, email, phone, locality, address):
        self._name = name
        self._surname = surname
        self._email = email
        self._phone = phone
        self._locality = locality
        self._address = address
        self._wallet = VirtualWallet

    def __init__(self):
        pass

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, a_name):
        self._name = a_name
