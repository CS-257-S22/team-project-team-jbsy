import unittest
import helper

# Test whether the company is in the list
class TestInput(unittest.TestCase):
    def input_In_Data(self, input):
        data = helper.readFile("dummyData.csv")
        for i in range(len(data)):
            self.assertEqual(data[i], input)
    def inputYear_Valid(self, input):
        self.assertTrue(type(input) == int)
    def inputCompanyName_Valid(self,input):
        self.assertTrue(type(input) == str)

if __name__ == '__main__':
    unittest.main()