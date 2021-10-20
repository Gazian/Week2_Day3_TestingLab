import unittest
from src.customer import Customer
from src.drink import Drink
from src.pub import Pub


class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jean-Pierre",15.50)

    def test_customer_has_name(self):
        self.assertEqual("Jean-Pierre", self.customer.name)
        
    def test_customer_has_wallet(self):
        self.assertEqual(15.50,self.customer.wallet)
        
    def test_customer_wallet_can_change(self):
        self.customer.customer_wallet_change(4.5)
        self.assertEqual(11, self.customer.wallet)