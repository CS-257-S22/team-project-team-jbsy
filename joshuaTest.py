import unittest
import helper
from service import getCompaniesByMinInitApproval

class UnitTestHelper(unittest.TestCase):
    
    # Test on getting column name by index
    def testGetColumnNameByIndex(self):
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

    # Test on creating company data by year
    def testCreateDataByYear(self):

        # Edge Case to handle empty list
        self.assertEqual(helper.createDataByYear([]), [])

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

    # Make Test for Print

    # Test on reading csv file
    def testReadFile(self):
        dummyData = "dummyData.csv"

        # Edge Case: Check if the function returns an error when the file is not found??

        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]

        # Check if the most recent year is saved correctly
        self.assertEqual(mostRecentYear, "2020")

        # Check if the Visa Data is a dictionary
        self.assertIsInstance(testVisaData, dict)

        testOneVisaData = testVisaData["REDDY GI ASSOCIATES"]

        # Check if the data of all the years are in the company
        self.assertIn("2018", testOneVisaData)
        self.assertIn("2019", testOneVisaData)
        self.assertIn("2020", testOneVisaData)

        # Check if the data of one year is in the correct format
        dataWeWant = {'City': 'MESA', 'Continuing Approvals': '0','Continuing Denials': '1','Employer': 'REDDY GI ASSOCIATES',
        'Fiscal Year': '2018','Initial Approvals': '0','Initial Denials': '0','NAICS': '99','State': 'AZ','Tax ID': '','ZIP': '85209'}
        
        self.assertDictEqual(testOneVisaData["2018"], dataWeWant)

class UnitTestService(unittest.TestCase):

    def testGetCompaniesByMinInitApproval(self):
        dummyData = "dummyData.csv"
        readFileResult = helper.readFile(dummyData)
        mostRecentYear = readFileResult[1]
        testVisaData = readFileResult[0]
        testArgument = {"target": "2", "mostRecentYear": mostRecentYear, "visaData": testVisaData}

        # Edge Case: return an empty list if all the data in arguments are not passed in
        # self.assertEqual(getCompaniesByMinInitApproval({}), ValueError)
        self.assertEqual(getCompaniesByMinInitApproval({}), [])

        testResult = getCompaniesByMinInitApproval(testArgument)

        # Todo: Check if the function is returning a list

        # Return a non-empty list 
        self.assertNotEqual(len(testResult), 0)

        testCompanyInList = testResult[0]

        # Check if necessary elements are in company
        self.assertIn("companyName", testCompanyInList)
        self.assertIn("data", testCompanyInList)

        testCompanyName = testCompanyInList["companyName"]
        testCompanyData = testCompanyInList["data"]

        #Check Company name
        self.assertEqual(testCompanyName, "REDDY GI ASSOCIATES")

        #Check Company Data
        dataWeWant = {'City': 'MESA','Continuing Approvals': '2','Continuing Denials': '1','Employer': 'REDDY GI ASSOCIATES','Fiscal Year': '2020','Initial Approvals': '5','Initial Denials': '0','NAICS': '93','State': 'AZ','Tax ID': '','ZIP': '85209'}
        self.assertDictEqual(testCompanyData, dataWeWant)

        



if __name__ == '__main__':
    unittest.main()

