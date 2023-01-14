import unittest
from myfunction import getTotalMarks

class TestMyFunction(unittest.TestCase):

    def test_function_working(self):
        actual = getTotalMarks('ux,60newlinecloud,60')
        expected = '120'
        self.assertEqual(actual,expected)

    def test_mark_too_high(self):
        actual = getTotalMarks('ux,120newlinecloud,60')
        expected = 'you have entered an incorrect value, module score must not be more than 100 or less than 0'
        self.assertEqual(actual,expected)

    def test_incorrect(self):
        actual = getTotalMarks('ux,60newlinecloud,60')
        expected = '140'
        self.assertNotEqual(actual,expected)
    
if __name__ == '__main__':
    unittest.main()