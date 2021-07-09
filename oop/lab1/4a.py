

class BankAccount():
    def __init__(self, accountId, pin, balance = 100):
        self.__accountId = accountId
        self.__pin = pin
        self.__balance = balance

    #getter
    @property
    def accountId(self): return self.__accountId

    @property
    def pin(self): return self.__pin

    @property
    def balance(self): return self.__balance

    #setter
    @pin.setter
    def pin(self, newPin): self.__pin = newPin
    
    @balance.setter
    def balance(self, newBalance): self.__balance = newBalance

    #methods
    def changePin(self, oldpin, newpin):
        if oldpin == self.__pin:
            self.__pin = newpin
            return True
        else: 
            return False

    def deposit(self, amount):
        self.__balance += amount #is the same as (self.__balance = self.__balance + amount)
        print(f"Amount of ${amount} deposited")

    def withdraw(self, amount):
        if amount > self.__balance:
            print(f"Withdraw unsuccesful ")
            return False
        else: 
            self.__balance - amount
            print(f"Withdraw successful")
            return False

    #ERRORS HERE
    def transfer(self, anotherAccount, amount):
        if self.withdraw(amount):
            anotherAccount.deposit(amount)
            return True
        return False

    def __str__(self):
        return f'accoundId: {self.__accountId} balance: ${self.__balance:.2f}'




#start of code
account1 = BankAccount('B1', 111)

print(account1.accountId, account1.pin, account1.balance)

account1.deposit(100)

# print(account1.balance)

account1.changePin(111, 120)

# print(account1.pin)

account2 = BankAccount('B2', 222)

print(account2.accountId, account2.pin, account2.balance)

# print(account2.withdraw(200))


#---------------------------------
#ERRORS HERE
account1.transfer(account2, 100)

print(account1.balance)
print(account2.balance)

print(account1.__str__())
print(account2.__str__())
