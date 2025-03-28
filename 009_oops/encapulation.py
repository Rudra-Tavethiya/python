
class demo:

    __amount = 5000
    def __init__(self):
        pass

    def balance(self):
        print("balance is : ",self.__amount)

    def deposit(self,amt):
        self.__amount+=amt

d = demo()
d.balance()
d.deposit(2000)
d.balance()


print(dir(d))