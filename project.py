filepath = 'dummyData.csv';
database = open(filepath,"r");
database.readline();
approvalPercentages = [];

def getCompaniesByState(state):
   substring = "\"" + state + "\"";
   for i in range(60):
       lineData = database.readline()
       databaseInfo = lineData.split(",");
       if(databaseInfo[8]==substring):
         return databaseInfo[1];

def getStatByCompanies(company):
     substring = "\"" + company + "\"";
     for i in range(60):
        lineData = database.readline()
        databaseInfo = lineData.split(",");
        if(databaseInfo[1]==substring):
            print("Fiscal Year => " + databaseInfo[0]);
            print("Employer => " + databaseInfo[1]);
            print("Initial Approvals => " + databaseInfo[2]);
            print("Initial Denials => " + databaseInfo[3]);
            print("Continuing Approvals => " + databaseInfo[4]);
            print("Continuing Denials => " + databaseInfo[5]);
            print("NAICS => " + databaseInfo[6]);
            print("Tax ID => " + databaseInfo[7]);
            print("State => " + databaseInfo[8]);
            print("City => " + databaseInfo[9]);
            print("ZIP => " + databaseInfo[10]);

def getCompaniesByMinInitApproval(initApproval, target):
    substring = initApproval;
    database.readline();
    for i in range(60):
        lineData = database.readline()
        databaseInfo = lineData.split(",");
        if(int(databaseInfo[2].replace("\"",""))>=initApproval):
            print("Employer => " + databaseInfo[1]);

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
def initiateCommand(command, target):
    if "company" in command:
        #call getStatByCompanies
    elif "state" in command:
        # call getCompaniesByState
    elif "initApproval" in command:
        # call minimum and maximum then print
    elif "ContinuingApprovals" in command:
        # call minimum and maximum then print
    else:
        print("Please input a command that is valid\n")

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

# Commandline example
# python3 project.py dummyData.csv --company "Google"

#getStatByCompanies("CVE TECHNOLOGY GROUP INC");
#print(getCompaniesByState("SD"));
#print(getCompaniesByMinInitApproval(1));
#print(getCompaniesByMinContinuingApproval(1));
#top10VisaApprovalRatesByYear();
approvalRatesByCompany("SAN JOSE STATE UNIVERSISTY");
#approvalPercentage()