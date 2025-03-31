from abc import abstractmethod,ABC


class account(ABC):

    balance=0

    @abstractmethod
    def deposit(self):
        pass

    def checkbalance(self):
        print("current balance : ",self.balance)


class savingaccount(account):

    def deposit(self,amt):
        self.balance+=amt


class loanaccount(account):

    def deposit(self,amount):
        self.balance-=amount
    

s = savingaccount()
s.checkbalance()
s.deposit(2000)
s.checkbalance()
print("************************")
l = loanaccount()
l.balance = 10000
l.checkbalance()
l.deposit(5000)
l.checkbalance()