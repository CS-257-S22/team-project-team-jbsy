from multiprocessing.sharedctypes import Array
import unittest
import helper

from service import getCompaniesByState
class Tests(unittest.TestCase):

    # Test function to get companies by state
    def test_getCompaniesByState(self):
        dummyData = "dummyData.csv"

        testReadFile = helper.readFile(dummyData)
        testVisaData = testReadFile[0]
        testMostRecentYear = testReadFile[1] 
        testState = "CA"
    
        testArgument = {"visaData": testVisaData, "target": testState, "mostRecentYear": testMostRecentYear}
        testResult = getCompaniesByState(testArgument)

        # Check if the companies are stored in a list
        self.assertIsInstance(testResult, list)

        # Check if the company list is not empty
        self.assertTrue(testResult)

        # Check if the most recent year is 2020
        self.assertEqual(testMostRecentYear, "2020" )

if __name__ == '__main__':
      unittest.main()