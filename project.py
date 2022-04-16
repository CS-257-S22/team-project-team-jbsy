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
def getCompaniesByMinContinuingApproval(continuingApproval):
    #substring = continuingApproval;
    database.readline();
    for i in range(60):
        lineData = database.readline();
        databaseInfo = lineData.split(",");
        if(int(databaseInfo[4].replace("\"",""))>=continuingApproval):
            print("Employer => " + databaseInfo[1]);

def approvalRatesByCompany(company):
    approvalRates();
    for i in range(60):
        if (approvalPercentages[i][1]==company):
            print(str(approvalPercentages[i][0]));
            

def approvalRates():
    for i in range(60):
        companyInfo = [];
        lineData = database.readline();
        databaseInfo = lineData.split(",");
        companyInfo.append(100 * (int(databaseInfo[2].replace("\"","")) + int(databaseInfo[4].replace("\"","")))/2);
        companyInfo.append(databaseInfo[1].replace("\"",""));
        approvalPercentages.append(companyInfo);

def top10VisaApprovalRatesByYear():
    approvalRates();
    approvalPercentages.sort(reverse=True);
    for i in range(10):
     print(approvalPercentages[i][1] + " => " + str(approvalPercentages[i][0]));

def readCommandLine():
    # Read the commandline as arg
    arg = sys.argv

    # Todo: Verify if arg data is correct

    fileData = readFile(arg[1])
    visaData = fileData[0]
    mostRecentYear = fileData[1]
    
    command = arg[2]
    target = arg[-1]

    # Todo: Verify if target relevant (company name exists, or column name exists, etc)

    initiateCommand(command, target)
    


# project.py dummyData.csv --company "Google"

def getCompaniesByMinInitApproval(initApproval):
    companies  = "";
    years = {"2018","2019","2020"}
    for j in visaData:
        for i in years:
            if(int(visaData[j][i]["Initial Approvals"]) >= initApproval):
                companies = companies + visaData[j][i]["Employer"] + " in Year " + visaData[j][i]["Fiscal Year"] + "\n";
    return companies;            

        
#print(helper.readFile(filePath));
print(getStatByCompanies("GLOBAL TAX NETWORK ATLANTIC LLC"));
print(getCompaniesByState("CA"));
print(getCompaniesByMinInitApproval(0));

#getStatByCompanies("CVE TECHNOLOGY GROUP INC");
#print(getCompaniesByState("SD"));
#print(getCompaniesByMinInitApproval(1));
#print(getCompaniesByMinContinuingApproval(1));
#top10VisaApprovalRatesByYear();
#approvalRatesByCompany("SAN JOSE STATE UNIVERSISTY");
#approvalPercentage()
