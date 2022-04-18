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

# Class to test the input of the user.
# written by Sunny
class TestInput(unittest.TestCase):
    # Test whether the input is in an integer
    def inputYear_Valid(self):
        self.assertTrue(type(self) == int)
        
    # Test whether the input is in a string
    def inputCompanyName_Valid(self):
        self.assertTrue(type(self) == str)

    # Test whether column name input exists in the data
    def existCol(self):
        colName = ["Fiscal Year", "Employer", "Initial Approvals", "Initial Denials", "Continuing Approvals", "Continuing Denials", "NAICS", "Tax ID", "State", "City", "ZIP"] 
        self.assertIn(colName)

    # Test whether the input is empty or not (Edge Case)
    def existInput(self):
        self.assertNotEqual(self, "")


if __name__ == '__main__':
    unittest.main()

