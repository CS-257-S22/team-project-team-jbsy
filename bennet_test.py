from multiprocessing.sharedctypes import Array
from unittest.mock import patch
from io import StringIO
from service import initiateCommand
import unittest
import helper


from service import getCompaniesByState
class UnitTestService(unittest.TestCase):
    """Unit tests for service functions"""

    """Unit tests for getCompaniesByState function"""
    def test_emptyList_getCompaniesByState(self):
        """Test empty list for getCompaniesByState"""

        with patch('sys.stdout', new = StringIO()) as fake_out:
            # Edge Case: return an empty list if all the data in arguments are not passed in
            self.assertEqual(getCompaniesByState({}), [])

            # Check if it prints the wanted result
            self.assertIn("Need all the data in argument", fake_out.getvalue())

    def test_returnList_getCompaniesByState(self):
        """Test return list for getCompaniesByState"""

        dummyData = "dummyData.csv"

        testReadFile = helper.readFile(dummyData)
        testVisaData = testReadFile[0]
        testMostRecentYear = testReadFile[1] 
        testState = "CA"
    
        testArgument = {"visaData": testVisaData, "target": testState, "mostRecentYear": testMostRecentYear}
        testResult = getCompaniesByState(testArgument)
        companyInfo= testResult[0]
        
        # Check if the companies are stored in a list
        self.assertIsInstance(testResult, list)

        # Check if the company list is not emptys
        self.assertTrue(testResult)

        # Check if the most recent year is of companies in the list is 2020
        self.assertEqual(testMostRecentYear, "2020")

        # Checking validity for the element tag representing a company name in the list
        self.assertIn("companyName", companyInfo)

    def test_resultValidity_getCompaniesByState(self):
        """Test the validity of the results from getCompaniesByState"""

        dummyData = "dummyData.csv"

        testReadFile = helper.readFile(dummyData)
        testVisaData = testReadFile[0]
        testMostRecentYear = testReadFile[1] 
        testState = "CA"
    
        testArgument = {"visaData": testVisaData, "target": testState, "mostRecentYear": testMostRecentYear}
        testResult = getCompaniesByState(testArgument)

        # Typical test cases to check if function prints the expected company names in the list for CA
        self.assertEqual(testResult[0]["companyName"], "THE BELPORT COMPANY INC")
        self.assertEqual(testResult[1]["companyName"], "CALLAWAY GOLF SALES COMPANY")
        self.assertEqual(testResult[2]["companyName"], "PAYSAFE PARTNERS LP")
        self.assertEqual(testResult[3]["companyName"], "STATE OF CA SECY OF STATE S OFFICE")
        self.assertEqual(testResult[4]["companyName"], "EMERALD HEALTH PHARMACEUTICALS INC")
        self.assertEqual(testResult[5]["companyName"], "GONSALVES & SANTUCCI INC DBA THE C")
        self.assertEqual(testResult[6]["companyName"], "A T KEARNEY")
        self.assertEqual(testResult[7]["companyName"], "AMERI INFO INC")
        self.assertEqual(testResult[8]["companyName"], "SAN JOSE STATE UNIVERSISTY")
        self.assertEqual(testResult[9]["companyName"], "LIN ZHI INTERNATIONAL INC")
        self.assertEqual(testResult[10]["companyName"], "FUNKTRONIC LABS")
        self.assertEqual(testResult[11]["companyName"], "ELM EAST LLC")
class IntegrationTestService(unittest.TestCase):
    """Integration Tests for service functions"""

    def test_integration_getCompaniesByState(self):
        """Test the validity of the information printed by the command line arguments for getCompaniesByState"""

        testCommand = "--state"
        testTarget = "CA"
        dummyData = "dummyData.csv"
        testReadFile = helper.readFile(dummyData)
        testmostRecentYear = testReadFile[1]
        testVisaData = testReadFile[0]

        testArgument = {"visaData": testVisaData, "target": testTarget, "mostRecentYear": testmostRecentYear, "command": testCommand}

        companyName1 = "THE BELPORT COMPANY INC"
        companyName2 = "CALLAWAY GOLF SALES COMPANY"
        companyName3 = "PAYSAFE PARTNERS LP"

        with patch('sys.stdout', new = StringIO()) as fake_out:
            # Execute command line argument
            initiateCommand(testArgument)

            # Check if the command line arguments prints the expected names company names
            self.assertIn(companyName1, fake_out.getvalue())
            self.assertIn(companyName2, fake_out.getvalue())
            self.assertIn(companyName3, fake_out.getvalue())

if __name__ == '__main__':
      unittest.main()