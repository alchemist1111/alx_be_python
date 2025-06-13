# Bank account class
class BankAccount:
    def __init__(self, initial_balance=0):
        """
          Initialize the bank account with an optional initial balance.
        By default, balance is 0.
        """
        self.__account_balance = initial_balance # Private attribute for balance
        
    def deposit(self, amount):
        """
          Deposit a positive amount into the account.
        """
        if amount > 0:
            self.__account_balance += amount
        else:
            raise ValueError("Amount can not be zero.")
        
    def withdraw(self, amount):
        """
          Withdraw the specified amount if funds are sufficient.
          Returns True if successful, False otherwise.
        """
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False
    
    def display_balance(self):
        """
          Print the current account balance.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")
                    