'''
Create a class BankAccount with attributes account_number, holder_name, balance.
Implement methods:

__str__ to return account details.
deposit(amount) to add money.
withdraw(amount) to withdraw money if sufficient balance.
show_details() to display account information.
From BankAccount, inherit:

SavingsAccount with an extra attribute interest_rate.
CurrentAccount with an extra attribute overdraft_limit.
'''


class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = balance
    
    def __str__(self):
        return f"Account Number: {self.account_number}, Holder: {self.holder_name}, Balance: ${self.balance:.2f}"
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        else:
            print("Insufficient funds or invalid amount.")
    
    def show_details(self):
        print(self)

class SavingsAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, interest_rate):
        super().__init__(account_number, holder_name, balance)
        self.interest_rate = interest_rate
    
    def __str__(self):
        return super().__str__() + f", Interest Rate: {self.interest_rate}%"
    
    def show_details(self):
        print(self)

class CurrentAccount(BankAccount):
    def __init__(self, account_number, holder_name, balance, overdraft_limit):
        super().__init__(account_number, holder_name, balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self, amount):
        if 0 < amount <= self.balance + self.overdraft_limit:
            self.balance -= amount
            print(f"Withdrew ${amount:.2f}. Remaining balance: ${self.balance:.2f}")
        else:
            print("Withdrawal exceeds overdraft limit.")
    
    def __str__(self):
        return super().__str__() + f", Overdraft Limit: ${self.overdraft_limit:.2f}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    savings = SavingsAccount("SA12345", "John Doe", 5000, 2.5)
    current = CurrentAccount("CA67890", "Jane Doe", 3000, 1000)
    
    savings.show_details()
    current.show_details()
    
    savings.deposit(500)
    savings.withdraw(1000)
    savings.show_details()
    
    current.withdraw(3500)
    current.show_details()




