class BankAccount:
    def __init__(self, account_balance=0):
        self.account_balance = account_balance

    def deposit(self, amount):
        self.account_balance += amount
        return f"Deposited: ${amount}"

    def withdraw(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            return amount
        else:
            return None

    def display_balance(self):
        print(f"Current Balance: ${float(self.account_balance)}")
    
