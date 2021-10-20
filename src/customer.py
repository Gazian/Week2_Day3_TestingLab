class Customer:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet
    
    def customer_wallet_change(self,amount):
        self.wallet -= amount