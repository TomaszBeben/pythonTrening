class BankAccount:
    __value: 0

    def amount(self):
        return self._BankAccount__value
    
myAccount = BankAccount()
print(myAccount.amount())