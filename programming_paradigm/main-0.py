import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 3:
        print("Usage: python main-0.py <operation> <amount>")
        sys.exit(1)

    operation = sys.argv[1].lower()
    try:
        amount = float(sys.argv[2])
    except ValueError:
        print("Amount must be a number.")
        sys.exit(1)

    account = BankAccount()  
    result = ""
    if operation == 'deposit':
        result = account.deposit(amount)
    elif operation == 'withdraw':
        result = account.withdraw(amount)
    elif operation == 'display':
        result = account.display_balance()
    else:
        print("Unknown operation. Use 'deposit', 'withdraw', or 'display'.")

    if result:
        print(result)

if __name__ == "__main__":
    main()
