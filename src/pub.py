class Pub:
    def __init__ (self, name, till):
        self.name = name
        self.till = till
        self.drinks = []
        
    def pub_till_change(self, amount):
        self.till += amount