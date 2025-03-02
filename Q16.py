'''
Create a class Wallet with attributes owner_name, balance, currency.
Implement methods:

__str__ to return wallet details.
add_money(amount) to increase balance.
spend_money(amount) to decrease balance if sufficient funds.
show_details() to display all wallet information.
From Wallet, inherit:

CryptoWallet with an extra attribute crypto_type.
BankWallet with an extra attribute linked_bank_name.
'''

class Wallet:
    def __init__(self, owner_name, balance, currency):
        self.owner_name = owner_name
        self.balance = balance
        self.currency = currency
    
    def __str__(self):
        return f"Wallet Owner: {self.owner_name}, Balance: {self.balance} {self.currency}"
    
    def add_money(self, amount):
        self.balance += amount
        print(f"{amount} {self.currency} added. New balance: {self.balance} {self.currency}")
    
    def spend_money(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"{amount} {self.currency} spent. Remaining balance: {self.balance} {self.currency}")
        else:
            print("Insufficient funds.")
    
    def show_details(self):
        print(self)

class CryptoWallet(Wallet):
    def __init__(self, owner_name, balance, currency, crypto_type):
        super().__init__(owner_name, balance, currency)
        self.crypto_type = crypto_type
    
    def __str__(self):
        return super().__str__() + f", Crypto Type: {self.crypto_type}"
    
    def show_details(self):
        print(self)

class BankWallet(Wallet):
    def __init__(self, owner_name, balance, currency, linked_bank_name):
        super().__init__(owner_name, balance, currency)
        self.linked_bank_name = linked_bank_name
    
    def __str__(self):
        return super().__str__() + f", Linked Bank: {self.linked_bank_name}"
    
    def show_details(self):
        print(self)

# Example usage
if __name__ == "__main__":
    crypto_wallet = CryptoWallet("Alice", 2.5, "BTC", "Bitcoin")
    bank_wallet = BankWallet("Bob", 5000, "USD", "Chase Bank")
    
    crypto_wallet.show_details()
    bank_wallet.show_details()
    
    crypto_wallet.add_money(1.0)
    crypto_wallet.spend_money(0.5)
    
    bank_wallet.add_money(1000)
    bank_wallet.spend_money(200)
    
    crypto_wallet.show_details()
    bank_wallet.show_details()
