import unittest
from myfunction import getClassification

class TestMyFunction(unittest.TestCase):
    def test_function_working(self):
        actual = getClassification('ux,60newlinecloud,60')
        expected = 'Commendation'
        self.assertEqual(actual,expected)

    def test_wrong(self):
        actual = getClassification('ux,60newlinecloud,60') 
        expected = 'Distinction'
        self.assertNotEqual(actual,expected)

if __name__ == '__main__':
    unittest.main()