class BankAccount:
    def __init__(self, initial_balance=0):
        self.__account_balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__account_balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__account_balance:
                self.__account_balance -= amount
                print(f"Withdrawn: {amount}")
                return True
            else:
                print("Insufficient funds.")
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False
    
    def display_balance(self):
        print(f"Current Balance: {self.__account_balance:.2f}")

        # main-0.py
import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <initial_balance> <operation> <amount>")
        sys.exit(1)
    
    try:
        initial_balance = float(sys.argv[1])
    except ValueError:
        print("Initial balance must be a number.")
        sys.exit(1)
    
    account = BankAccount(initial_balance)
    
    if len(sys.argv) < 3:
        print("Please provide an operation: deposit, withdraw, or display")
        sys.exit(1)
    
    operation = sys.argv[2].lower()
    result = ""

    if operation == 'deposit':
        if len(sys.argv) < 4:
            print("Please provide an amount to deposit.")
            sys.exit(1)
        try:
            amount = float(sys.argv[3])
            result = account.deposit(amount)
        except ValueError:
            print("Deposit amount must be a number.")
    
    elif operation == 'withdraw':
        if len(sys.argv) < 4:
            print("Please provide an amount to withdraw.")
            sys.exit(1)
        try:
            amount = float(sys.argv[3])
            result = account.withdraw(amount)
        except ValueError:
            print("Withdrawal amount must be a number.")
    
    elif operation == 'display':
        result = account.display_balance()
    
    else:
        print("Unknown operation. Use 'deposit', 'withdraw', or 'display'.")
    
    if result:
        print(result)

if __name__ == "__main__":
    main()
