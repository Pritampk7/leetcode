class User(object):
    def __init__(self, email):
        self.email = email

    def signIn(self):

        print("logged in")


class Wizard(User):

    def __init__(self, name, power, email):
        User.__init__(self, email)
        self.name = name
        self.power =power
        self.email = email

    def attack(self):
        print(f"attacking with power os {self.power} and email is {self.email}")


class Archer(User):
    def __init__(self, name, num_arrows, email):
        super().__init__(email)
        self.name = name
        self.num_arrows = num_arrows
        self.email = email

    def attack(self):
        print(f"attacking with arrows  {self.num_arrows} : arrows decreased ")


wizard1 = Wizard('Merlin', 60,"err")
Archer1 = Archer('jack', 60,"err")
print(Archer1.attack())