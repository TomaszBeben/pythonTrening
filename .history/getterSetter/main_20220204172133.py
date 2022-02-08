class BankAccount:
    __value = 0

    @property
    def amount(self):
        return self.__value
    
    @amount.getter
    def amount(self):
        return 'Stan konta: ' + str(self.__value) + 'zł'

myAccount = BankAccount()
print(myAccount.amount)
print(myAccount._BankAccount__value)

myAccount.amount = 50
