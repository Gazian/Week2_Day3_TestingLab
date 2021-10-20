import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 1000)
    
    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)
        
    def test_pub_has_till(self):
        self.assertEqual(1000, self.pub.till)