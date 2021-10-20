import unittest
from src.pub import Pub
from src.drink import Drink
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
        # pdb.set_trace()
        # print(self.pub.drinks[0].name)
        # print(self.pub.drinks[0].price)
        self.assertEqual(1, len(self.pub.drinks))