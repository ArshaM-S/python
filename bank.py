class BankAccount:
    def __init__(self, acc_no, name, acc_type, balance):
        self.acc_no = acc_no
        self.name = name
        self.acc_type = acc_type
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs{amount} deposited successfully.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Rs{amount} withdrawn successfully.")

    def display(self):
        print("\n--- Account Details ---")
        print(f"Account Number: {self.acc_no}")
        print(f"Name: {self.name}")
        print(f"Account Type: {self.acc_type}")
        print(f"Balance: Rs{self.balance}")

# Get user input 
acc_no = input("Enter account number: ")
name = input("Enter account holder name: ")
acc_type = input("Enter type of account (e.g., Savings/Current): ")
balance = float(input("Enter initial balance: "))

# Create account object
account = BankAccount(acc_no, name, acc_type, balance)

# Display initial details
account.display()

# Deposit and Withdraw operations
deposit_amount = float(input("\nEnter amount to deposit: "))
account.deposit(deposit_amount)
account.display()

withdraw_amount = float(input("\nEnter amount to withdraw: "))
account.withdraw(withdraw_amount)
account.display()
