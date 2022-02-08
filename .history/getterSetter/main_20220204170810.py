class BankAccount:
    __value: 0

    def amount(self):
        return self.__value
    
myAccount = BankAccount()
print(myAccount.amount())