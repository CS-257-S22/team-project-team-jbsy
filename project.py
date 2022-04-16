filepath = 'dummyData.csv';
database = open(filepath,"r");

# method to get the names of companies within the input state
def getCompaniesByState(state):
    substring = "\"" + state + "\"";
    for i in range(60):
        lineData = database.readline()
        databaseInfo = lineData.split(",");
        if(databaseInfo[8]==substring):
            print(databaseInfo[1]);

# method to get the statistics of the input company
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

# method to get the names of companies with the input number of initial approval
def getCompaniesByMinInitApproval(initApproval):
    substring = initApproval;
    database.readline();
    for i in range(60):
        lineData = database.readline()
        databaseInfo = lineData.split(",");
        if(int(databaseInfo[2].replace("\"",""))>=initApproval):
            print("Employer => " + databaseInfo[1]);

# getStatByCompanies("FUNKTRONIC LABS");
# print(getCompaniesByState("CA"));
# getCompaniesByMinInitApproval(1);