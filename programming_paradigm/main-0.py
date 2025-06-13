import sys
from bank_account import BankAccount

def main():
    # Create a BankAccount instance with an initial balance of $100
    account = BankAccount(1000)

    # Ensure at least one argument is provided (command)
    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    # Split the command and amount (if provided)
    parts = sys.argv[1].split(':')
    command = parts[0]
    amount = float(parts[1]) if len(parts) > 1 else None

    # Handle deposit command
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    
    # Handle withdraw command
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    
    # Handle display command
    elif command == "display":
        account.display_balance()
    
    # Handle invalid commands or missing amount
    else:
        print("Invalid command or missing amount.")

if __name__ == "__main__":
    main()
