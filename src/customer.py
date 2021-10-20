class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age = age
    
    def customer_wallet_change(self, amount):
        self.wallet -= amount