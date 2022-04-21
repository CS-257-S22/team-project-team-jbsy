import unittest
from service import getStatByCompany, getCompaniesByMinInitApproval
from helper import readFile

class TestSOMETHING(unittest.TestCase):
    
    def test_getStatsbyCompany1(self):

        """unit test for edge case for getStatsbyCompany"""

        filePath = 'dummyData.csv'
        visaData = readFile(filePath)

        company0 = "CARLETON COLLEGE"

        correctResult0 = {}
       
        
        #edge case
        self.assertDictEqual(getStatByCompany({"visaData": visaData[0], "target": company0}), correctResult0)
  
    def test_getStatsbyCompany1(self):

        """unit test for typical case for getStatsbyCompany"""

        filePath = 'dummyData.csv'
        visaData = readFile(filePath)

        company1 = "REDDY GI ASSOCIATES"

        correctResult1 = {"companyName" : company1 , "data" : {'2018': {'Fiscal Year': '2018', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '1', 'NAICS': '99', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}, '2019': {'Fiscal Year': '2019', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '1', 'NAICS': '100', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}, '2020': {'Fiscal Year': '2020', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '5', 'Initial Denials': '0', 'Continuing Approvals': '2', 'Continuing Denials': '1', 'NAICS': '93', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}}}

        self.assertDictEqual(getStatByCompany({"visaData": visaData[0], "target": company1}), correctResult1)
       
    def test_getStatsbyCompany2(self):

        """unit test for typical case for getStatsbyCompany"""

        filePath = 'dummyData.csv'
        visaData = readFile(filePath)

        company2 = "FUNKTRONIC LABS"

        rawData1 = getCompaniesByMinInitApproval({"visaData": visaData[0], "target": "0", "mostRecentYear":"2020"})

        correctResult2 = {"companyName" : company2 , "data" : {'2018': {'Fiscal Year': '2018', 'Employer': 'FUNKTRONIC LABS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '0', 'NAICS': '51', 'Tax ID': '', 'State': 'CA', 'City': 'SOUTH EL MONTE', 'ZIP': '91733'}, '2019': {'Fiscal Year': '2019', 'Employer': 'FUNKTRONIC LABS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '0', 'NAICS': '54', 'Tax ID': '', 'State': 'CA', 'City': 'SOUTH EL MONTE', 'ZIP': '91733'}, '2020': {'Fiscal Year': '2020', 'Employer': 'FUNKTRONIC LABS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '23', 'Continuing Denials': '0', 'NAICS': '41', 'Tax ID': '', 'State': 'CA', 'City': 'SOUTH EL MONTE', 'ZIP': '91733'}}}

        self.assertDictEqual(getStatByCompany({"visaData": visaData[0], "target": company2}), correctResult2) 

    def test_getStatsbyCompany3(self):

        """unit test for typical case for getStatsbyCompany"""

        filePath = 'dummyData.csv'
        visaData = readFile(filePath)

        company3 = "CANCER TREATMENT CTRS OF AMERICA G"

        correctResult3 = {"companyName" : company3 , "data" : {'2018': {'Fiscal Year': '2018', 'Employer': 'CANCER TREATMENT CTRS OF AMERICA G', 'Initial Approvals': '0', 'Initial Denials': '1', 'Continuing Approvals': '0', 'Continuing Denials': '0', 'NAICS': '62', 'Tax ID': '', 'State': 'FL', 'City': 'BOCA RATON', 'ZIP': '33487'}, '2019': {'Fiscal Year': '2019', 'Employer': 'CANCER TREATMENT CTRS OF AMERICA G', 'Initial Approvals': '0', 'Initial Denials': '1', 'Continuing Approvals': '0', 'Continuing Denials': '0', 'NAICS': '61', 'Tax ID': '', 'State': 'FL', 'City': 'BOCA RATON', 'ZIP': '33487'}, '2020': {'Fiscal Year': '2020', 'Employer': 'CANCER TREATMENT CTRS OF AMERICA G', 'Initial Approvals': '4', 'Initial Denials': '1', 'Continuing Approvals': '5', 'Continuing Denials': '0', 'NAICS': '82', 'Tax ID': '', 'State': 'FL', 'City': 'BOCA RATON', 'ZIP': '33487'}}}

        self.assertDictEqual(getStatByCompany({"visaData": visaData[0], "target": company3}), correctResult3)
    
    #edge case
    def test_minInitApprovalfor0(self):

         """unit test for edge case for getCompaniesbyMinInitApproval"""

         filePath = 'dummyData.csv'
         visaData = readFile(filePath) 

         rawData0 = getCompaniesByMinInitApproval({"visaData": visaData[0], "target": "0", "mostRecentYear":"2020"})


         correctResult0 = [{'companyName': 'REDDY GI ASSOCIATES', 'data': {'Fiscal Year': '2020', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '5', 'Initial Denials': '0', 'Continuing Approvals': '2', 'Continuing Denials': '1', 'NAICS': '93', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}}, {'companyName': 'ADMIRAL INSTRUMENTS LLC', 'data': {'Fiscal Year': '2020', 'Employer': 'ADMIRAL INSTRUMENTS LLC', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': '0', 'NAICS': '31', 'Tax ID': '', 'State': 'AZ', 'City': 'TEMPE', 'ZIP': '85281'}}, {'companyName': 'THE BELPORT COMPANY INC', 'data': {'Fiscal Year': '2020', 'Employer': 'THE BELPORT COMPANY INC', 'Initial Approvals': '0', 
'Initial Denials': '1', 'Continuing Approvals': '4', 'Continuing Denials': '0', 'NAICS': '35', 'Tax ID': '', 'State': 'CA', 'City': 'CAMARILLO', 'ZIP': '93012'}}, {'companyName': 'CALLAWAY GOLF SALES COMPANY', 'data': {'Fiscal Year': '2020', 'Employer': 'CALLAWAY GOLF SALES COMPANY', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '7', 'Continuing Denials': '0', 'NAICS': '38', 'Tax ID': '', 'State': 'CA', 'City': 'CARLSBAD', 'ZIP': '92008'}}, {'companyName': 'PAYSAFE PARTNERS LP', 'data': {'Fiscal Year': '2020', 'Employer': 'PAYSAFE PARTNERS LP', 'Initial Approvals': '10', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '0', 'NAICS': '54', 'Tax ID': '', 'State': 'CA', 
'City': 'IRVINE', 'ZIP': '92612'}}, {'companyName': 'STATE OF CA SECY OF STATE S OFFICE', 'data': {'Fiscal Year': '2020', 'Employer': 'STATE OF CA SECY OF STATE S OFFICE', 'Initial Approvals': '20', 'Initial Denials': '0', 'Continuing Approvals': '19', 'Continuing Denials': '1', 'NAICS': '58', 'Tax ID': '', 'State': 'CA', 'City': 'SACRAMENTO', 'ZIP': '95814'}}, {'companyName': 'EMERALD HEALTH PHARMACEUTICALS INC', 'data': {'Fiscal Year': '2020', 'Employer': 'EMERALD HEALTH PHARMACEUTICALS INC', 'Initial Approvals': '20', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '1', 'NAICS': '54', 'Tax ID': '', 'State': 'CA', 'City': 'SAN DIEGO', 'ZIP': '92121'}}, {'companyName': 'GONSALVES & SANTUCCI INC DBA THE C', 'data': {'Fiscal Year': '2020', 'Employer': 'GONSALVES & SANTUCCI INC DBA THE C', 'Initial Approvals': '1', 'Initial Denials': '0', 
'Continuing Approvals': '5', 'Continuing Denials': '0', 'NAICS': '22', 'Tax ID': '', 'State': 'CA', 'City': 'SAN FRANCISCO', 'ZIP': '94111'}}, {'companyName': 'A T KEARNEY', 'data': {'Fiscal Year': '2020', 'Employer': 'A T KEARNEY', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '17', 'Continuing Denials': '0', 'NAICS': '89', 'Tax ID': '', 'State': 'CA', 'City': 'SAN FRANCISCO', 'ZIP': '94111'}}, {'companyName': 'AMERI INFO INC', 'data': {'Fiscal Year': '2020', 'Employer': 'AMERI INFO INC', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '2', 'Continuing Denials': '0', 'NAICS': '64', 'Tax ID': '', 'State': 'CA', 'City': 'SAN JOSE', 'ZIP': '95129'}}, {'companyName': 'SAN JOSE STATE UNIVERSISTY', 'data': {'Fiscal Year': '2020', 'Employer': 'SAN JOSE STATE UNIVERSISTY', 'Initial Approvals': '1', 'Initial Denials': 
'0', 'Continuing Approvals': '13', 'Continuing Denials': '0', 'NAICS': '41', 'Tax ID': '', 'State': 'CA', 'City': 'SAN JOSE', 'ZIP': '95192'}}, {'companyName': 'LIN ZHI INTERNATIONAL INC', 'data': {'Fiscal Year': '2020', 'Employer': 'LIN ZHI INTERNATIONAL INC', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '4', 'Continuing Denials': '0', 'NAICS': '22', 'Tax ID': '', 'State': 'CA', 'City': 'SANTA CLARA', 'ZIP': '95051'}}, {'companyName': 'FUNKTRONIC LABS', 'data': {'Fiscal Year': '2020', 'Employer': 'FUNKTRONIC LABS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '23', 'Continuing Denials': '0', 'NAICS': '41', 'Tax ID': '', 'State': 'CA', 'City': 'SOUTH EL MONTE', 'ZIP': '91733'}}, {'companyName': 'ELM EAST LLC', 'data': {'Fiscal Year': '2020', 'Employer': 'ELM EAST LLC', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '0', 'NAICS': '64', 'Tax ID': '', 'State': 'CA', 'City': 'SUNNYVALE', 'ZIP': '94086'}}, {'companyName': 'BOEHRINGER INGELHEIM PHARMA', 'data': {'Fiscal Year': '2020', 'Employer': 'BOEHRINGER INGELHEIM PHARMA', 'Initial Approvals': '0', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '0', 'NAICS': '66', 'Tax ID': '', 'State': 'CT', 'City': 'RIDGEFIELD', 'ZIP': '06877'}}, {'companyName': 'GLOBAL TAX NETWORK ATLANTIC LLC', 'data': {'Fiscal Year': '2020', 'Employer': 'GLOBAL TAX NETWORK ATLANTIC LLC', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '4', 'Continuing Denials': '0', 'NAICS': '44', 'Tax ID': '', 'State': 'CT', 'City': 'STAMFORD', 'ZIP': '06902'}}, {'companyName': 'DISTRICT OF COLUMBIA PUBLC SCHOOLS', 'data': {'Fiscal Year': '2020', 'Employer': 'DISTRICT OF COLUMBIA PUBLC SCHOOLS', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '2', 'Continuing Denials': '0', 'NAICS': '51', 'Tax ID': '', 'State': 'DC', 'City': 'WASHINGTON', 'ZIP': '20002'}}, {'companyName': 'PULMONICS PLUS PLLC', 'data': {'Fiscal Year': '2020', 'Employer': 'PULMONICS PLUS PLLC', 'Initial Approvals': '1', 'Initial Denials': '0', 'Continuing Approvals': '0', 'Continuing Denials': 
'0', 'NAICS': '52', 'Tax ID': '', 'State': 'DC', 'City': 'WASHINGTON', 'ZIP': '20036'}}, {'companyName': 'AIRPORT SHERPA LLC', 'data': {'Fiscal Year': '2020', 'Employer': 'AIRPORT SHERPA LLC', 'Initial Approvals': '1', 'Initial Denials': '1', 'Continuing Approvals': '4', 'Continuing Denials': '0', 'NAICS': '89', 'Tax ID': '', 'State': 'DE', 'City': 'WILMINGTON', 'ZIP': '19801'}}, {'companyName': 'CANCER TREATMENT CTRS OF AMERICA G', 'data': {'Fiscal Year': '2020', 'Employer': 'CANCER TREATMENT CTRS OF AMERICA G', 'Initial Approvals': '4', 'Initial Denials': '1', 'Continuing Approvals': '5', 'Continuing Denials': '0', 'NAICS': '82', 'Tax ID': '', 'State': 'FL', 'City': 'BOCA RATON', 'ZIP': '33487'}}]           

         self.assertEqual(rawData0, correctResult0)
        
    def test_minInitApprovalfor4(self):

        """unit test for typical case for getCompaniesbyMinInitApproval"""

        filePath = 'dummyData.csv'
        visaData = readFile(filePath)

        rawData4 = getCompaniesByMinInitApproval({"visaData": visaData[0], "target": "4", "mostRecentYear":"2020"})

        correctResult4 = [{'companyName': 'REDDY GI ASSOCIATES', 'data': {'Fiscal Year': '2020', 'Employer': 'REDDY GI ASSOCIATES', 'Initial Approvals': '5', 'Initial Denials': '0', 'Continuing Approvals': '2', 'Continuing Denials': '1', 'NAICS': '93', 'Tax ID': '', 'State': 'AZ', 'City': 'MESA', 'ZIP': '85209'}}, {'companyName': 'PAYSAFE PARTNERS LP', 'data': {'Fiscal Year': '2020', 'Employer': 'PAYSAFE PARTNERS LP', 'Initial Approvals': '10', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '0', 'NAICS': '54', 'Tax ID': '', 'State': 'CA', 'City': 'IRVINE', 'ZIP': '92612'}}, 
{'companyName': 'STATE OF CA SECY OF STATE S OFFICE', 'data': {'Fiscal Year': '2020', 'Employer': 'STATE OF CA SECY OF STATE S OFFICE', 'Initial Approvals': '20', 'Initial Denials': '0', 'Continuing Approvals': '19', 'Continuing Denials': '1', 'NAICS': '58', 'Tax ID': '', 'State': 'CA', 'City': 'SACRAMENTO', 'ZIP': '95814'}}, {'companyName': 'EMERALD HEALTH PHARMACEUTICALS INC', 'data': {'Fiscal Year': '2020', 'Employer': 'EMERALD HEALTH PHARMACEUTICALS INC', 'Initial Approvals': '20', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '1', 'NAICS': '54', 'Tax ID': '', 'State': 'CA', 'City': 'SAN DIEGO', 'ZIP': '92121'}}, {'companyName': 'CANCER TREATMENT CTRS OF AMERICA G', 'data': {'Fiscal Year': '2020', 'Employer': 'CANCER TREATMENT CTRS OF AMERICA G', 'Initial Approvals': '4', 'Initial Denials': '1', 'Continuing Approvals': '5', 'Continuing Denials': '0', 'NAICS': '82', 'Tax ID': '', 'State': 'FL', 'City': 'BOCA RATON', 'ZIP': '33487'}}]

        self.assertEqual(rawData4, correctResult4)

    def test_minInitApprovalfor20(self):

        """unit test for edge case for getCompaniesbyMinInitApproval"""
 
        filePath = 'dummyData.csv'
        visaData = readFile(filePath)
        
        correctResult20 = [{'companyName': 'STATE OF CA SECY OF STATE S OFFICE', 'data': {'Fiscal Year': '2020', 'Employer': 'STATE OF CA SECY OF STATE S OFFICE', 'Initial Approvals': '20', 'Initial Denials': '0', 'Continuing Approvals': '19', 'Continuing Denials': '1', 'NAICS': '58', 'Tax ID': '', 'State': 'CA', 'City': 'SACRAMENTO', 'ZIP': '95814'}}, {'companyName': 'EMERALD HEALTH PHARMACEUTICALS INC', 'data': {'Fiscal Year': '2020', 'Employer': 'EMERALD HEALTH PHARMACEUTICALS INC', 'Initial Approvals': '20', 'Initial Denials': '0', 'Continuing Approvals': '1', 'Continuing Denials': '1', 'NAICS': '54', 'Tax ID': '', 'State': 'CA', 'City': 'SAN DIEGO', 'ZIP': '92121'}}]
        
        rawData20 = getCompaniesByMinInitApproval({"visaData": visaData[0], "target": "20", "mostRecentYear":"2020"})
        
        self.assertEqual(rawData20, correctResult20)


if __name__ == '__main__':
      unittest.main()

