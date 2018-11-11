import unittest
from src import program2

class Program2Test(unittest.TestCase):

    def test_case_1(self):
        test = program2.Palindrome()
        self.assertTrue(test.isPalindrome('qwewq'))

    def test_case_2(self):
        test = program2.Palindrome()
        self.assertTrue(test.isPalindrome('asddsa'))

    def test_case_3(self):
        test = program2.Palindrome()
        self.assertFalse(test.isPalindrome('qwddc'))

    def test_case_4(self):
        test = program2.Palindrome()
        self.assertFalse(test.isPalindrome('dfgtb'))

    def test_case_5(self):
        test = program2.Palindrome()
        self.assertEqual('-1', test.isPalindrome('-1'))


if __name__ == '__main__':
    unittest.main()
    p2t= Program2Test()
