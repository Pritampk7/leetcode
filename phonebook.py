class PhoneBook:
    def __init__(self):
        self.phonebook = {}

    def add(self, name, number):
        self.phonebook[name] = number

    def get(self, name):
        return self.phonebook.get(name, f"User {name} Not registered in Phonebook")


phone_book = PhoneBook()
phone_book.add("Alice", "123-456-7890")
phone_book.add("Bob", "987-654-3210")
print(phone_book.get("Alidce"))
