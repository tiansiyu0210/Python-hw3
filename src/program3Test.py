import unittest
from src import program3

class Program3Test(unittest.TestCase):

    def test_case_1(self):
        test = program3.CreditCard()
        self.assertTrue(test.isValid('371232345686516'))

    def test_case_2(self):
        test = program3.CreditCard()
        self.assertFalse(test.isValid('371232345686546'))

    def test_case_3(self):
        test = program3.CreditCard()
        self.assertTrue(test.isValid('41232345683411'))

    def test_case_4(self):
        test = program3.CreditCard()
        self.assertFalse(test.isValid('41232345683412'))

    def test_case_5(self):
        test = program3.CreditCard()
        self.assertTrue(test.isValid('51232345686544'))

    def test_case_6(self):
        test = program3.CreditCard()
        self.assertFalse(test.isValid('51232345686547'))

    def test_case_7(self):
        test = program3.CreditCard()
        self.assertTrue(test.isValid('61232345686542'))

    def test_case_8(self):
        test = program3.CreditCard()
        self.assertFalse(test.isValid('61232345686547'))


if __name__ == '__main__':
    unittest.main()
    p3t= Program3Test()
