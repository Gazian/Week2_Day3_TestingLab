import unittest
from src.pub import Pub
from src.drink import Drink
from src.customer import Customer
# import pdb

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        
    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)
    
    def test_pub_till_can_change(self):
        self.pub.pub_till_change(4.50)
        self.assertEqual(1004.50, self.pub.till)
    
    def test_pub_can_add_drinks(self):
        drink = Drink("Beavertown IPA", 4.50)
        self.pub.add_drinks_to_pub(drink)
        self.assertEqual(1, len(self.pub.drinks))
        
    def test_find_drink_by_name(self):
        drink = Drink("Beavertown IPA", 4.50)
        self.pub.add_drinks_to_pub(drink)
        found_drink = self.pub.find_drink_by_name(drink.name)
        self.assertEqual("Beavertown IPA", found_drink.name)

    def test_sell_drink_to_customer(self):
        drink = Drink("Innis & Gunn", 5.50)
        customer = Customer("Jean-Pierre", 15.50, 21)
        self.pub.add_drinks_to_pub(drink)
        self.pub.find_drink_by_name(drink)
        self.pub.sell_drink_to_customer(customer, drink)
        self.assertEqual(10, customer.wallet)
        self.assertEqual(1005.50, self.pub.till)

    def test_check_age(self):
        customer = Customer("Jean-Pierre", 15.50, 21)
        self.assertEqual(True, self.pub.check_age(customer))

    def test_customer_can_buy_drink(self):
        drink = Drink("Innis & Gunn", 5.50)
        customer = Customer("Jean-Pierre", 15.50, 21)
        self.pub.add_drinks_to_pub(drink)
        self.pub.find_drink_by_name(drink)
        self.pub.sell_drink_to_customer(customer, drink)
        self.assertEqual(10, customer.wallet)
        self.assertEqual(1005.5, self.pub.till)

    def test_customer_cant_buy_drink(self):
        drink = Drink("Innis & Gunn", 5.50)
        customer = Customer("Sam", 10, 17)
        self.pub.add_drinks_to_pub(drink)
        self.pub.find_drink_by_name(drink)
        self.pub.sell_drink_to_customer(customer, drink)
        self.assertEqual(10, customer.wallet)
        self.assertEqual(1000, self.pub.till)

