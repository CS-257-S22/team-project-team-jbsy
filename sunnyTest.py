import unittest
import helper
import verification

# Class to test the input of the user.
class UnitTestHelper(unittest.TestCase):
    # Test if companyExist method works
    def testCompanyExist(self):

        # Edge Case : file name does not end in csv
        dummyData = "dummyData.c"
        self.assertFalse(dummyData[-3:] == ".v")

        # Check if file name ends in csv
        dummyData = "dummyData.csv"
        self.assertEqual(dummyData[-3:], "csv")
        
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.companyExist('REDDY GI ASSOCIATES', dummyData))
        self.assertFalse(verification.companyExist('NO SUCH COMPANY', dummyData))

    # Test if columnExist method works
    def testColumnExist(self):

        # Get dummyData and testVisaData for the test
        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        testVisaData = readFileResult[0]
        
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.columnExist("company", testVisaData))
        self.assertTrue(verification.columnExist("City", testVisaData))
        self.assertTrue(verification.columnExist("NAICS", testVisaData))
        self.assertFalse(verification.columnExist("None", testVisaData))



if __name__ == '__main__':
    unittest.main()

