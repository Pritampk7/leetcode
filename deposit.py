class BankingSystem:
    def __init__(self):

        self.account = {}

    def openAccount(self, accountNumber, initialDeposit):

        if accountNumber not in self.account:
            self.account[accountNumber] = initialDeposit
        return self.account

    def deposit(self, accountNumber, amount):

        if accountNumber in self.account:
            self.account[accountNumber] += amount
        else:
            raise Exception(f"Account {accountNumber} not linked")

    def withdraw(self, accountNumber, amount):

        if accountNumber in self.account:
            self.account[accountNumber] -= amount
        else:
            raise f"{accountNumber} is not available"

    def checkBalance(self, accountNumber):

        return self.account.get(accountNumber)


bank = BankingSystem()
print(bank.openAccount("123", 1000))
bank.deposit("123", 500)
bank.withdraw("123", 1200)
print(bank.checkBalance("123"))
