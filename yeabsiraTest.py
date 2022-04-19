import unittest
from service import getStatByCompany
from helper import readFile

class TestSOMETHING(unittest.TestCase):
    def test_(self):
        #self.maxDiff(None);
        filePath = 'dummyData.csv'
        visaData = readFile(filePath)
        company1 = "REDDY GI ASSOCIATES"
        company2 = "FUNKTRONIC LABS"
        company3 = "BOEHRINGER INGELHEIM PHARMA"
        correctResult1 = {"companyName" : company1 , "data" : {'2018': {'Fiscal Year': '2018', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '1', 'NAICS': '99', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}, '2019': {'Fiscal Year': '2019', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '1', 'NAICS': '100', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}, '2020': {'Fiscal Year': '2020', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '5', 'Initial Denials': '0', 'Continuing Approvals': '2', 'Continuing Denials': '1', 'NAICS': '93', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}}}
        correctResult2 = {"companyName" : company2 , "data" : {'2018': {'Fiscal Year': '2018', 'Employer': 'FUNKTRONIC LABS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '0', 'NAICS': '51', 'Tax ID': '', 'State': 'CA', 'City': 'SOUTH EL MONTE', 'ZIP': '91733'}, '2019': {'Fiscal Year': '2019', 'Employer': 'FUNKTRONIC LABS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '0', 'NAICS': '54', 'Tax ID': '', 'State': 'CA', 'City': 'SOUTH EL MONTE', 'ZIP': '91733'}, '2020': {'Fiscal Year': '2020', 'Employer': 'FUNKTRONIC LABS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '23', 'Continuing Denials': '0', 'NAICS': '41', 'Tax ID': '', 'State': 'CA', 'City': 'SOUTH EL MONTE', 'ZIP': '91733'}}}
        correctResult3 = {"companyName" : company3 , "data" : {'2018': {'Fiscal Year': '2018', 'Employer': 'BOEHRINGER INGELHEIM PHARMA', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '0', 'NAICS': '56', 'Tax ID': '', 'State': 'CT', 'City': 'RIDGEFIELD', 'ZIP': '06877'}, '2019': {'Fiscal Year': '2019', 'Employer': 'BOEHRINGER INGELHEIM PHARMA', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '0', 'NAICS': '59', 'Tax ID': '', 'State': 'CT', 'City': 'RIDGEFIELD', 'ZIP': '06877'}, '2020': {'Fiscal Year': '2020', 'Employer': 'BOEHRINGER INGELHEIM PHARMA', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '0', 'NAICS': '66', 'Tax ID': '', 'State': 'CT', 'City': 'RIDGEFIELD', 'ZIP': '06877'}}}
        self.assertDictEqual(getStatByCompany({"visaData": visaData[0], "target": company1}), correctResult1) 
        self.assertDictEqual(getStatByCompany({"visaData": visaData[0], "target": company2}), correctResult2)
        self.assertDictEqual(getStatByCompany({"visaData": visaData[0], "target": company3}), correctResult3)


if __name__ == '__main__':
      unittest.main()

