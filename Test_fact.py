from unittest import TestCase
from factoriel import fact

class Testfact(TestCase):
    def test_fact(self):
        result= fact(3)
        self.assertEqual(6, result)

