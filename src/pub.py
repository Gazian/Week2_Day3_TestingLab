class Pub:
    def __init__ (self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        
    def pub_till_change(self, amount):
        self.till += amount
        
    def add_drinks_to_pub(self, drink):
        self.drinks.append(drink)
    
    def find_drink_by_name(self, name):
        for drink in self.drinks:
            if drink.name == name:
                return drink
        
    def check_age(self, customer):
        return customer.age >= 18
        
    def sell_drink_to_customer(self, customer, drink):
        if self.check_age(customer):
            self.find_drink_by_name(drink)
            customer.customer_wallet_change(drink.price)
            self.pub_till_change(drink.price)
        
