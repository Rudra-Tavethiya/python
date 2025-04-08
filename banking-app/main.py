from modules.banker import Banker
from modules.customer import Customer

def main():
    while True:
        print("\n--- Welcome to Banking System ---")
        print("1. Banker")
        print("2. Customer")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            banker = Banker()
            while True:
                print("\n--- Banker Menu ---")
                print("1. Register")
                print("2. Login")
                print("3. Back")
                b_choice = input("Enter your choice: ")

                if b_choice == '1':
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    password = input("Enter password: ")
                    banker.register(name, email, password)

                elif b_choice == '2':
                    email = input("Enter email: ")
                    password = input("Enter password: ")
                    if banker.login(email, password):
                        print("\nLogin successful!\n")
                        while True:
                            print("\n1. View Customers\n2. Update Customer\n3. Delete Customer\n4. Logout")
                            opt = input("Choose option: ")
                            if opt == '1':
                                banker.view_customers()
                            elif opt == '2':
                                cid = int(input("Enter customer ID: "))
                                name = input("Enter new name: ")
                                email = input("Enter new email: ")
                                banker.update_customer(cid, name, email)
                            elif opt == '3':
                                cid = int(input("Enter customer ID to delete: "))
                                banker.delete_customer(cid)
                            elif opt == '4':
                                break
                    else:
                        print("\nInvalid credentials!\n")
                elif b_choice == '3':
                    break

        elif choice == '2':
            while True:
                print("\n--- Customer Menu ---")
                print("1. Register")
                print("2. Login")
                print("3. Back")
                c_choice = input("Enter your choice: ")

                if c_choice == '1':
                    name = input("Enter name: ")
                    email = input("Enter email: ")
                    password = input("Enter password: ")
                    cust = Customer(name, email, password)
                    cust.register()

                elif c_choice == '2':
                    email = input("Enter email: ")
                    password = input("Enter password: ")
                    temp = Customer("", "", "")
                    user = temp.login(email, password)
                    if user:
                        print("\nLogin successful!\n")
                        customer_id = user[0]
                        while True:
                            print("\n1. Deposit\n2. Withdraw\n3. View Balance\n4. Logout")
                            opt = input("Choose option: ")
                            if opt == '1':
                                amt = float(input("Enter amount to deposit: "))
                                temp.deposit(amt, customer_id)
                            elif opt == '2':
                                amt = float(input("Enter amount to withdraw: "))
                                temp.withdraw(amt, customer_id)
                            elif opt == '3':
                                temp.view_balance(customer_id)
                            elif opt == '4':
                                break
                    else:
                        print("\nInvalid credentials!\n")

                elif c_choice == '3':
                    break

        elif choice == '3':
            print("\nThank you for using our banking system. Goodbye!")
            break

        else:
            print("\nInvalid choice. Try again!\n")

if __name__ == '__main__':
    main()
