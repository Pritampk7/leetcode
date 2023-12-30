class PlayerCharacter:
    def __init__(self):
        self.mylist = []

    def add(self, name):
        self.mylist.append(name)
        return self.mylist

    def get(self):
        return self.mylist if "pritam".title() in self.mylist else False


obj = PlayerCharacter()
obj.mylist.append(12)
obj.add("Pritam")
obj.add("Pritamq")
obj.add("Pritam")
obj.add("Pritamq")

print(obj.get())

