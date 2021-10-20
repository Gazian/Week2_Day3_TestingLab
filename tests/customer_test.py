import unittest
from src.customer import Customer

class TestCustomer(unittest.TestCase):
    def setUp(self):
        self.customer = Customer("Jean-Pierre",15.50)

    def test_customer_has_name(self):
        self.assertEqual("Jean-Pierre", self.customer.name)
        
    def test_customer_has_wallet(self):
        self.assertEqual(15.50,self.customer.wallet)
        