import unittest
import project
import helper
import verification

class TestSOMETHING(unittest.TestCase):
    def test_approval(self):
        self.assertEqual(service.getCompaniesByState("SD"),"NATIONAL MUSIC MUSEUM");
       # self.assertEqual(test("0 NORTH AVE WAKEFIELD LLC"),"1");
    #def test_denial(self):
       # self.assertEqual(test("7CINFO COM INC"),"1");
       # self.assertEqual(test("ACORNS GROW INCORPORATED"),"0");

    # Test whether the input is in an integer
    def inputYear_Valid(self, input):
        self.assertTrue(type(input) == int)
        
    # Test whether the input is in a string
    def inputCompanyName_Valid(self, input):
        self.assertTrue(type(input) == str)

    # Test whether the input exists
    def existInput(self, input):
        self.assertNotEqual(input == "")

    # Test whether column name exists in the data
    def existCol(self, input, filename):
        self.assertTrue(verification.columnTest(input,filename))

if __name__ == '__main__':
      print(service.getCompaniesByState("SD"));
      unittest.main()

