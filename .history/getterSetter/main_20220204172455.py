class BankAccount:
    __value = 0

    @property
    def amount(self):
        return self.__value
    
    @amount.getter
    def amount(self):
        return 'Stan konta: ' + str(self.__value) + 'zł'
    
    @amount.setter
    def amount(self, value):
        self.__value += value


myAccount = BankAccount()
myAccount.amount = 50
print(myAccount.amount)
myAccount.amount = 150
print(myAccount.amount)
print(myAccount._BankAccount__value)
