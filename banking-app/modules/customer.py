from modules.base import User

class Customer(User):
    def __init__(self, name, email, password):
        super().__init__(name, email, password)
        self.__balance = 0

    def register(self):
        print("\nCustomer registered successfully!\n")

    def login(self, email, password):
        return (1, self.name, self.email)

    def deposit(self, amount, customer_id):
        self.__balance += amount
        print("\nDeposit successful!\n")

    def withdraw(self, amount, customer_id):
        if amount <= self.__balance:
            self.__balance -= amount
            print("\nWithdrawal successful!\n")
        else:
            print("\nInsufficient balance!\n")

    def view_balance(self, customer_id):
        print(f"\nYour balance is: {self.__balance}\n")
