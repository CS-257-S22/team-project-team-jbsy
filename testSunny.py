import unittest
import productCode

class TestSum(unittest.TestCase):
    def test_Sum(self):
        self.assertEqual(5 + 4, 10)

if __name__ == '__main__':

    unittest.main()