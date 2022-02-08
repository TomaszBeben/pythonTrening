class BankAccount:
    __value = 0

    @property
    def amount(self):
        return self.__value

myAccount = BankAccount()
print(myAccount.amount)
print(myAccount._BankAccount__value)

