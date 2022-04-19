from io import StringIO
import unittest
from unittest.mock import patch
import helper
import verification
import main

class UnitTestHelper(unittest.TestCase):
    """Unit Test for readCommandLine() and Verification"""

    def testCompanyExist(self):
        """Unit Test to check if companyExist method works"""

        # Edge Case : file name does not end in csv
        dummyData = "dummyData.c"
        self.assertFalse(dummyData[-3:] == ".csv")

        # Check if file name ends in csv
        dummyData = "dummyData.csv"
        self.assertEqual(dummyData[-3:], "csv")
        
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.companyExist('REDDY GI ASSOCIATES', dummyData))
        self.assertFalse(verification.companyExist('NO SUCH COMPANY', dummyData))

        pass

    def testColumnExist(self):
        """Unit Test to check if columnExistt method works"""

        # Get dummyData and testVisaData for the test
        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        testVisaData = readFileResult[0]
        
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.columnExist("company", testVisaData))
        self.assertTrue(verification.columnExist("City", testVisaData))
        self.assertTrue(verification.columnExist("NAICS", testVisaData))
        self.assertFalse(verification.columnExist("None", testVisaData))

    def testContainsNum(self):
        """Unit Test to check if containsNumber method works"""

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
        self.assertTrue(verification.containsNum(testStr))
        self.assertTrue(verification.containsNum("19"))
        self.assertFalse(verification.containsNum("1 9"))
        self.assertFalse(verification.containsNum("Yes"))
        self.assertFalse(verification.containsNum("he11o"))
    
    def testcommandLen(self):
        """Unit Test to check if commandLen method works"""
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
    
    def testInputValid(self):
        """Unit Test to check if inputValid method works"""

        # No need to check for empty commands because we check the command line length before 
        # Sample cases to see if the method returns the correct booleans
        self.assertTrue(verification.inputValid("PULMONICS PLUS PLLC", "--company"))
        self.assertTrue(verification.inputValid("CA", "--state"))
        self.assertTrue(verification.inputValid("2", "--minInitApproval"))
        self.assertFalse(verification.inputValid("None", "--minInitApproval"))

class IntegrationTest(unittest.TestCase):
    """Integration Test for readCommandLine() and Verification"""
    
    def test_Error_Verification_IntegrationTest(self):
        """Integration Test for Verification to check if errors are printed out correctly"""
        
        testArg = ["main.py", "dummyData.csv", "--company"]

        # When there are less arguments in the command line.
        with patch("sys.argv", testArg):
            with patch('sys.stdout', new = StringIO()) as fake_out:
                main.readCommandLine()
                
                # Check if it prints an error
                self.assertEqual("Invalid Command : Need more arguments\n", fake_out.getvalue())

    def test_Verification_IntegrationTestCompany(self):
        """Integration Test for --Company & Verification to check if results are printed out correctly"""

        testArg = ["main.py", "dummyData.csv", "--company", "PULMONICS", "PLUS", "PLLC"]

        # When the command line argument is looking for companies
        with patch("sys.argv", testArg):
            with patch('sys.stdout', new = StringIO()) as fake_out:
                main.readCommandLine()

                expectedValue1 = "Fiscal Year => 2020"
                expectedValue2 = "City => WASHINGTON"
                expectedValue3 = "ZIP => 20036"

                # Check if it passes the verification test and give the result we want
                self.assertIn(expectedValue1, fake_out.getvalue())
                self.assertIn(expectedValue2, fake_out.getvalue())
                self.assertIn(expectedValue3, fake_out.getvalue())

    def test_Verification_IntegrationTestState(self):
        """Integration Test for --State & Verification to check if results are printed out correctly"""

        testArg = ["main.py", "dummyData.csv", "--state", "CA"]

        # When the command line argument is looking for states
        with patch("sys.argv", testArg):
            with patch('sys.stdout', new = StringIO()) as fake_out:
                main.readCommandLine()

                expectedValue1 = "CALLAWAY GOLF SALES COMPANY"
                expectedValue2 = "A T KEARNEY"
                expectedValue3 = "FUNKTRONIC LABS"

                # Check if it passes the verification test and give the result we want
                self.assertIn(expectedValue1, fake_out.getvalue())
                self.assertIn(expectedValue2, fake_out.getvalue())
                self.assertIn(expectedValue3, fake_out.getvalue())
        
        def test_Verification_IntegrationTestState(self):
            """Integration Test for Verification to check if results are printed out correctly"""

        testArg = ["main.py", "dummyData.csv", "--state", "CA"]

        with patch("sys.argv", testArg):
            with patch('sys.stdout', new = StringIO()) as fake_out:
                main.readCommandLine()

                expectedValue1 = "CALLAWAY GOLF SALES COMPANY"
                expectedValue2 = "A T KEARNEY"
                expectedValue3 = "FUNKTRONIC LABS"

                # Check if it passes the verification test and give the result we want
                self.assertIn(expectedValue1, fake_out.getvalue())
                self.assertIn(expectedValue2, fake_out.getvalue())
                self.assertIn(expectedValue3, fake_out.getvalue())

    def test_Verification_IntegrationTestMinInitApproval(self):
        """Integration Test for --minInitApproval & Verification to check if results are printed out correctly"""

        testArg = ["main.py", "dummyData.csv", "--minInitApproval", "2"]

        # When the command line argument is looking for minimum initial approval
        with patch("sys.argv", testArg):
            with patch('sys.stdout', new = StringIO()) as fake_out:
                main.readCommandLine()

                expectedValue1 = "REDDY GI ASSOCIATES"
                expectedValue2 = "STATE OF CA SECY OF STATE S OFFICE"
                expectedValue3 = "CANCER TREATMENT CTRS OF AMERICA G"

                # Check if it passes the verification test and give the result we want
                self.assertIn(expectedValue1, fake_out.getvalue())
                self.assertIn(expectedValue2, fake_out.getvalue())
                self.assertIn(expectedValue3, fake_out.getvalue())
        

if __name__ == '__main__':
    unittest.main()

