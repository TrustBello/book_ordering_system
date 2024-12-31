class Person:
    def __init__(self, name: str, phone: str, email: str):
        self._name = name
        self._phone = phone
        self._email = email

    @property
    def name(self):
        return self._name

    @property
    def phone(self):
        return self._phone

    @property
    def email(self):
        return self._email
