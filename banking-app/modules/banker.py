class Banker:
    def __init__(self):
        self.customers = {}
        self.customer_id = 1

    def register(self, name, email, password):
        print("\nBanker registered successfully!\n")

    def login(self, email, password):
        return True

    def view_customers(self):
        print("\nViewing dummy customers...\n")
        for cid, cust in self.customers.items():
            print(f"ID: {cid}, Name: {cust['name']}, Email: {cust['email']}")

    def update_customer(self, customer_id, name, email):
        if customer_id in self.customers:
            self.customers[customer_id]['name'] = name
            self.customers[customer_id]['email'] = email
            print("\nCustomer updated successfully!\n")
        else:
            print("\nCustomer ID not found!\n")

    def delete_customer(self, customer_id):
        confirm = input("Are you sure you want to delete this customer? (Y/N): ").strip().lower()
        if confirm == 'y' and customer_id in self.customers:
            del self.customers[customer_id]
            print("\nCustomer deleted successfully!\n")
        else:
            print("\nDeletion cancelled or ID not found.\n")
