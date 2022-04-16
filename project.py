import sys
from helper import readFile

filepath = 'h1b_datahubexport-2018.csv';
database = open(filepath,"r");

def getCompaniesByState(state):
   substring = "\"" + state + "\"";
   for i in range(1000):
       lineData = database.readline()
       databaseInfo = lineData.split(",");
       if(databaseInfo[8]==substring):
         return databaseInfo[1];

def getStatByCompanies(company):
     substring = "\"" + company + "\"";
     for i in range(1000):
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
    for i in range(10000):
        lineData = database.readline()
        databaseInfo = lineData.split(",");
        if(int(databaseInfo[2].replace("\"",""))>=initApproval):
            print("Employer => " + databaseInfo[1]);

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
# print(getCompaniesByState("SD"));
#getCompaniesByMinInitApproval(2);