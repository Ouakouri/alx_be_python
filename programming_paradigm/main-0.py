import sys
from bank_account import BankAccount

def main():
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <operation> [amount]")
        sys.exit(1)

    operation = sys.argv[1].lower()
    amount = None
    if len(sys.argv) == 3:
        try:
            amount = float(sys.argv[2])
        except ValueError:
            print("Amount must be a number.")
            sys.exit(1)

    account = BankAccount(100) 
    result = ""
    if operation == 'deposit' and amount is not None:
        result = account.deposit(amount)
    elif operation == 'withdraw' and amount is not None:
        result = account.withdraw(amount)
    elif operation == 'display':
        result = account.display_balance()
    else:
        print("Unknown operation or missing amount. Use 'deposit <amount>', 'withdraw <amount>', or 'display'.")
        sys.exit(1)

    if result:
        print(result)

if __name__ == "__main__":
    main()

