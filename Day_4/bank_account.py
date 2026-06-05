class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient balance. Overdraft not allowed.")
        else:
            self.balance -= amount
            print(f"Withdrawn ₹{amount}")

    def get_balance(self):
        return self.balance
    
    print(" Bank Account ")

account = BankAccount("Safana", 1000)

account.deposit(500)
account.withdraw(300)
account.withdraw(2000)

print("Current Balance:", account.get_balance())