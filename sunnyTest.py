import unittest
import helper
import verification

# Class to test the command line input.
class UnitTestHelper(unittest.TestCase):
    # Unit Test to check if companyExist method works
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

    # Unit Test to check if columnExist method works
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

    # Unit Test to check if containsNumber method works
    def testContainsNumber(self):
        
        # Edge case : arg is not string
        testArgList = [193]
        self.assertFalse(verification.commandLen(testArgList))
        testArgInt = 12345678
        self.assertFalse(verification.commandLen(testArgInt))

        # Check if arg is a string
        # Normally, command line changes into argument in main.py. It saves the command line as a list, starting after "python3".
        testStr = "2"
        self.assertTrue(type(testStr) == str)

        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.containsNumber(testStr))
        self.assertTrue(verification.containsNumber("19"))
        self.assertFalse(verification.containsNumber("1 9"))
        self.assertFalse(verification.containsNumber("Yes"))
        self.assertFalse(verification.containsNumber("he11o"))
    
    # Unit Test to check if commandLen method works
    def testcommandLen(self):
        
        # Edge case : arg is not list
        testArgStr = "python3 main.py dummyData.csv --company PULMONICS PLUS PLLC"
        self.assertFalse(verification.commandLen(testArgStr))
        testArgInt = 12345678
        self.assertFalse(verification.commandLen(testArgInt))

        # Check if arg is a list
        # Normally, command line changes into argument in main.py. It saves the command line as a list, starting after "python3".
        testArg = ["main.py", "dummyData.csv", "--company", "PULMONICS PLUS PLLC"]
        self.assertTrue(type(testArg) == list)

        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.commandLen(testArg))
        self.assertTrue(verification.commandLen(["main.py", "dummyData.csv", "--state", "CA"]))
        self.assertTrue(verification.commandLen(["main.py", "dummyData.csv", "--minInitApproval", "2"]))
        self.assertFalse(verification.commandLen(["main.py", "dummyData.csv"]))
        self.assertFalse(verification.commandLen(["main.py", "dummyData.csv", "--minInitApproval"]))
    
    # Unit Test to check if inputValid method works
    def testInputValid(self):

        

        # No need to check for empty commands because we check the command line len before 
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.inputValid("--company", "PULMONICS PLUS PLLC"))
        self.assertTrue(verification.inputValid("--state", "CA"))
        # self.assertTrue(verification.columnExist("NAICS", testVisaData))
        # self.assertFalse(verification.columnExist("None", testVisaData))

if __name__ == '__main__':
    unittest.main()

