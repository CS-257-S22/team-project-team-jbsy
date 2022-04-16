import helper
filePath = 'dummyData.csv';
database = open(filePath,"r");
database.readline();


visaData = helper.readFile(filePath);


def getCompaniesByState(state):
   prevCompany = ""
   companies = "";
   for j in visaData:
        for i in range(60):
         currCompany = visaData[j]["2018"]["Employer"];
         if(visaData[j]["2018"]["State"]==state) & (prevCompany!=currCompany):
            companies = companies + visaData[j]["2018"]["Employer"] + "\n";
            prevCompany = currCompany;
            
   return companies    
        

def getStatByCompanies(company):
     statsForCompany = ""
     years = {"2018","2019","2020"}
     for j in visaData:
         for i in years:
            if(j == company):
                statsForCompany = statsForCompany + "\nFiscal Year => " + visaData[j][i]["Fiscal Year"]  + "\n";
                statsForCompany = statsForCompany + "Employer => " + visaData[j][i]["Employer"]  + "\n";
                statsForCompany = statsForCompany + "Initial Approvals => " + visaData[j][i]["Initial Approvals"] + "\n";
                statsForCompany = statsForCompany + "Initial Denials => " + visaData[j][i]["Initial Denials"] + "\n";
                statsForCompany = statsForCompany + "Continuing Approvals => " + visaData[j][i]["Continuing Approvals"] + "\n";
                statsForCompany = statsForCompany + "Continuing Denials => " + visaData[j][i]["Continuing Denials"] + "\n";
                statsForCompany = statsForCompany + "NAICS => " + visaData[j][i]["NAICS"] + "\n";
                statsForCompany = statsForCompany + "Tax ID => " + visaData[j][i]["Tax ID"] + "\n";
                statsForCompany = statsForCompany + "State => " +visaData[j][i]["State"] + "\n";
                statsForCompany = statsForCompany + "City => " + visaData[j][i]["City"] + "\n";
                statsForCompany = statsForCompany + "ZIP => " + visaData[j][i]["ZIP"] + "\n";

     return statsForCompany;


def getCompaniesByMinInitApproval(initApproval):
    companies  = "";
    years = {"2018","2019","2020"}
    for j in visaData:
        for i in years:
            if(int(visaData[j][i]["Initial Approvals"]) >= initApproval):
                companies = companies + visaData[j][i]["Employer"] + " in Year " + visaData[j][i]["Fiscal Year"] + "\n";
    return companies;            

        
#print(helper.readFile(filePath));
#print(getStatByCompanies("GLOBAL TAX NETWORK ATLANTIC LLC"));
#print(getCompaniesByState("CA"));
#print(getCompaniesByMinInitApproval(0));