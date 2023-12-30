class Inventory:

    def __init__(self):
        self.inv = {}

    def addItem(self, fruit, quantity):
        if fruit in self.inv:
            self.inv[fruit] += quantity
        else:
            self.inv[fruit] = quantity

    def removeItem(self, fruit, quantity):
        self.inv[fruit] -= quantity

    def checkStock(self, fruit):
        if self.inv.get(fruit) < 0:
            return 0
        return self.inv.get(fruit, 0)


inventory = Inventory()
inventory.addItem("apples", 5)
inventory.addItem("apples", 5)
inventory.addItem("oranges", 3)
inventory.removeItem("apples", 1)
print(inventory.checkStock("apples"))
