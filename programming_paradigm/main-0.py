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
    
    if operation == 'deposit':
        if len(sys.argv) < 4:
            print("Please provide an amount to deposit.")
            sys.exit(1)
        try:
            amount = float(sys.argv[3])
            print(account.deposit(amount))
        except ValueError:
            print("Deposit amount must be a number.")
    
    elif operation == 'withdraw':
        if len(sys.argv) < 4:
            print("Please provide an amount to withdraw.")
            sys.exit(1)
        try:
            amount = float(sys.argv[3])
            print(account.withdraw(amount))
        except ValueError:
            print("Withdrawal amount must be a number.")
    
    elif operation == 'display':
        print(account.display_balance())
    
    else:
        print("Unknown operation. Use 'deposit', 'withdraw', or 'display'.")

if __name__ == "__main__":
    main()
