
from io import StringIO
import unittest
from unittest.mock import patch
import helper
from main import initiateCommand
from service import getCompaniesByMinInitApproval

class UnitTestHelper(unittest.TestCase):
    """Unit Test for Helper Functions"""

    def test_GetColumnNameByIndex(self):
        """Test GetColumnNameByIndex"""
        self.assertEqual(helper.getColumnNameByIndex(0), "Fiscal Year")
        self.assertEqual(helper.getColumnNameByIndex(1), "Employer")
        self.assertEqual(helper.getColumnNameByIndex(2), "Initial Approvals")
        self.assertEqual(helper.getColumnNameByIndex(3), "Initial Denials")
        self.assertEqual(helper.getColumnNameByIndex(4), "Continuing Approvals")
        self.assertEqual(helper.getColumnNameByIndex(5), "Continuing Denials")
        self.assertEqual(helper.getColumnNameByIndex(6), "NAICS")
        self.assertEqual(helper.getColumnNameByIndex(7), "Tax ID")
        self.assertEqual(helper.getColumnNameByIndex(8), "State")
        self.assertEqual(helper.getColumnNameByIndex(9), "City")
        self.assertEqual(helper.getColumnNameByIndex(10), "ZIP")
        # Edge Case
        self.assertEqual(helper.getColumnNameByIndex(11), "")

    def test_emptyList_testCreateDataByYear(self):
        """Test empty list for CreateDataByYear"""

        # Edge Case to handle empty list
        self.assertEqual(helper.createDataByYear([]), [])

    def test_returnVal_testCreateDataByYear(self):
        """Test return value for CreateDataByYear"""

        testLine = ['2018', 'REDDY GI ASSOCIATES', '0', '0', '0', '1', '99', '', 'AZ', 'MESA', '85209']
        checkResult = helper.createDataByYear(testLine)

        # Check if there are two elements in the returned list
        self.assertEqual(len(checkResult), 2)

        fiscalYear = checkResult[0]

        # Check if the fiscal year is correct 
        self.assertEqual(fiscalYear, "2018")

        companyDataByYear = checkResult[1]
        resultWeWant = {'City': 'MESA', 'Continuing Approvals': '0', 'Continuing Denials': '1', 'Employer': 'REDDY GI ASSOCIATES', 
        'Fiscal Year': '2018','Initial Approvals': '0','Initial Denials': '0','NAICS': '99','State': 'AZ','Tax ID': '','ZIP': '85209'}

        # Check if the function created the dictionary we want
        self.assertDictEqual(companyDataByYear, resultWeWant)
    
    def test_noCompanies_PrintMinInitApproval(self):
        """Test PrintMinInitApproval for empty list"""

        # When there are no companies
        with patch('sys.stdout', new = StringIO()) as fake_out1:
            helper.printMinInitApproval({"companiesList": [], "target": "2"})

            # Check if it prints the wanted result
            self.assertEqual("No companies exist with Initial Approval above 2\n", fake_out1.getvalue())

    def test_Companies_PrintMinInitApproval(self):
        """Test PrintMinInitApproval for list of companies"""

        # When there are list of companies
        with patch('sys.stdout', new = StringIO()) as fake_out2:            
            helper.printMinInitApproval({"companiesList": [{"companyName": "Carleton College", "data": {}}, {"companyName": "St.Olaf", "data": {}}], "target": "2"})

            # Check if it prints the wanted result
            self.assertIn("Carleton College", fake_out2.getvalue())
            self.assertIn("St.Olaf", fake_out2.getvalue())
            self.assertIn("\nCompanies with Minimum Initial Approval of 2", fake_out2.getvalue())

    def test_noCompany_PrintCompany(self):
        """Test PrintCompany empty dict"""

        # When there is no company
        with patch('sys.stdout', new = StringIO()) as fake_out1:
            helper.printCompany({})

            # Check if it prints the wanted result
            self.assertEqual("Company does not exist in dataset\n", fake_out1.getvalue())

    def test_Company_PrintCompany(self):
        """Test PrintCompany for a Company"""

        testCompanyData = {"companyName": 'REDDY GI ASSOCIATES', 'data': {"2020" : {'Fiscal Year': '2020', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '5', 'Initial Denials': '0', 'Continuing Approvals': '2', 'Continuing Denials': '1', 'NAICS': '93', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}}}

        # When there is a company
        with patch('sys.stdout', new = StringIO()) as fake_out2:            
            helper.printCompany(testCompanyData)

            # Check if it prints the wanted result
            self.assertIn("Statistic for REDDY GI ASSOCIATES:", fake_out2.getvalue())
            self.assertIn("Fiscal Year => 2020", fake_out2.getvalue())
            self.assertIn("Initial Approvals => 5", fake_out2.getvalue())
            self.assertIn("Initial Denials => 0", fake_out2.getvalue())
            self.assertIn("Continuing Approvals => 2", fake_out2.getvalue())
            self.assertIn("Continuing Denials => 1", fake_out2.getvalue())
            self.assertIn("NAICS => 93", fake_out2.getvalue())
            self.assertIn("Tax ID =>", fake_out2.getvalue())
            self.assertIn("State => AZ", fake_out2.getvalue())
            self.assertIn("City => MESA", fake_out2.getvalue())
            self.assertIn("ZIP => 85209", fake_out2.getvalue())

    def test_noCompanies_PrintCompaniesInState(self):
        """Test PrintCompaniesInState for empty list"""

        # When there are no companies
        with patch('sys.stdout', new = StringIO()) as fake_out1:
            helper.printCompaniesInState([], "CA")

            # Check if it prints the wanted result
            self.assertEqual("No companies exist in a given state\n", fake_out1.getvalue())

    def test_PrintCompaniesInState(self):
        """Test PrintCompaniesInState"""

        # When there are list of companies
        with patch('sys.stdout', new = StringIO()) as fake_out2:            
            helper.printCompaniesInState([{"companyName": "Carleton College", "data": {}}, {"companyName": "St.Olaf", "data": {}}], "MN")

            # Check if it prints the wanted result
            self.assertIn("Carleton College", fake_out2.getvalue())
            self.assertIn("St.Olaf", fake_out2.getvalue())
            self.assertIn("Companies located in MN:", fake_out2.getvalue())

    def test_fileError_testReadFile(self):
        """Test File error in testReadFile"""

        dummyData = "dummyData.csv"

        # Edge Case: Check if the function prints an error and returns
        with patch('sys.stdout', new = StringIO()) as fake_out1:
            result = helper.readFile(dummyData[::-1])

            # Check if it prints the wanted result
            self.assertEqual("Please input a valid file\n", fake_out1.getvalue())
            self.assertFalse(result)

    def test_return_Format_testReadFile(self):
        """Test return format testReadFile"""

        dummyData = "dummyData.csv"

        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]

        # Check if the most recent year is saved correctly
        self.assertEqual(mostRecentYear, "2020")

        # Check if the Visa Data is a dictionary
        self.assertIsInstance(testVisaData, dict)

    def test_return_Validity_testReadFile(self):
        """Test return validity for testReadFile"""

        dummyData = "dummyData.csv"

        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]

        testOneVisaData = testVisaData["REDDY GI ASSOCIATES"]

        # Check if the data of all the years are in the company
        self.assertIn("2018", testOneVisaData)
        self.assertIn("2019", testOneVisaData)
        self.assertIn("2020", testOneVisaData)

        dataWeWant = {'City': 'MESA', 'Continuing Approvals': '0','Continuing Denials': '1','Employer': 'REDDY GI ASSOCIATES',
        'Fiscal Year': '2018','Initial Approvals': '0','Initial Denials': '0','NAICS': '99','State': 'AZ','Tax ID': '','ZIP': '85209'}

        # Check if the data of one year is in the correct format
        self.assertDictEqual(testOneVisaData["2018"], dataWeWant)

class UnitTestService(unittest.TestCase):
    """Unit Test for Service Functions"""

    """Unit Tests for GetCompaniesByMinInitApproval"""
    def test_emptyList_GetCompaniesByMinInitApproval(self):
        """Test empty list for GetCompaniesByMinInitApproval"""

        with patch('sys.stdout', new = StringIO()) as fake_out:
            # Edge Case: return an empty list if all the data in arguments are not passed in
            self.assertEqual(getCompaniesByMinInitApproval({}), [])

            # Check if it prints the wanted result
            self.assertIn("Need all the data in argument", fake_out.getvalue())
            
    def test_returnList_GetCompaniesByMinInitApproval(self):
        """Test return list for GetCompaniesByMinInitApproval"""

        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]
        testArgument = {"target": "2", "mostRecentYear": mostRecentYear, "visaData": testVisaData}

        testResult = getCompaniesByMinInitApproval(testArgument)

        # Check if the function is returning a list
        self.assertIsInstance(testResult, list)

        # Return a non-empty list 
        self.assertNotEqual(len(testResult), 0)

    def test_resultElementsValidity_GetCompaniesByMinInitApproval(self):
        """Test result element validity for GetCompaniesByMinInitApproval"""

        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]
        testArgument = {"target": "2", "mostRecentYear": mostRecentYear, "visaData": testVisaData}

        testResult = getCompaniesByMinInitApproval(testArgument)
        testCompanyInList = testResult[0]

        # Check if necessary elements are in company
        self.assertIn("companyName", testCompanyInList)
        self.assertIn("data", testCompanyInList)

    def test_resultValidity_GetCompaniesByMinInitApproval(self):
        """Test result validity for GetCompaniesByMinInitApproval"""

        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]
        testArgument = {"target": "2", "mostRecentYear": mostRecentYear, "visaData": testVisaData}

        testResult = getCompaniesByMinInitApproval(testArgument)
        testCompanyInList = testResult[0]
        testCompanyName = testCompanyInList["companyName"]
        testCompanyData = testCompanyInList["data"]

        #Check Company name
        self.assertEqual(testCompanyName, "REDDY GI ASSOCIATES")

        #Check Company Data
        dataWeWant = {'City': 'MESA','Continuing Approvals': '2','Continuing Denials': '1','Employer': 'REDDY GI ASSOCIATES','Fiscal Year': '2020','Initial Approvals': '5','Initial Denials': '0','NAICS': '93','State': 'AZ','Tax ID': '','ZIP': '85209'}
        self.assertDictEqual(testCompanyData, dataWeWant)

class IntegrationTestService(unittest.TestCase):
    """Integration Test for Service Functions"""

    def test_integrationMinInitApproval(self):
        """Integration Test for MinInitApproval"""

        testCommand = "--minInitApproval"
        testTarget = "2"
        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]
        testArgument = {"command":testCommand, "target": testTarget, "mostRecentYear": mostRecentYear, "visaData": testVisaData}

        # check Print
        expectedCompany1 = "EMERALD HEALTH PHARMACEUTICALS INC"
        expectedCompany2 = "STATE OF CA SECY OF STATE S OFFICE"

        with patch('sys.stdout', new = StringIO()) as fake_out:
            # Initate Command
            initiateCommand(testArgument)

            # Check if it prints the wanted result
            self.assertIn(expectedCompany1, fake_out.getvalue())
            self.assertIn(expectedCompany2, fake_out.getvalue())


def main():
    # unittest.main(verbosity=2)
    unittest.main()

if __name__ == '__main__':
    main()

