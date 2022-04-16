from helper import printMinAndMaxData

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

def getCompaniesByColumn(arguments):
    visaData = arguments["visaData"]
    columnName = arguments["columnName"]
    mostRecentYear = arguments["mostRecentYear"]

    listOfMinCompanies = []
    listOfMaxCompanies = []

    for companyName in visaData:
        # First company in data
        if len(listOfMinCompanies) == 0 and len(listOfMaxCompanies) == 0:
            listOfMinCompanies.append({"companyName": companyName, "data": visaData[companyName]})
            listOfMaxCompanies.append({"companyName": companyName, "data": visaData[companyName]})
        else:
            # first company in min and max list
            targetMinCompany = listOfMinCompanies[0]
            targetMaxCompany = listOfMaxCompanies[0]

            # get value at column
            targetMin = targetMinCompany["data"][mostRecentYear][columnName]
            targetMax = targetMaxCompany["data"][mostRecentYear][columnName]
            currValue = visaData[companyName][mostRecentYear][columnName]

            # For minimum
            # If less, replace
            if int(currValue) < int(targetMin):
                listOfMinCompanies = []
                listOfMinCompanies.append({"companyName": companyName, "data": visaData[companyName]})
            # If the same, append to the list
            elif int(currValue) == int(targetMin):
                listOfMinCompanies.append({"companyName": companyName, "data": visaData[companyName]})
            
            # For maximum
            # If more, replace
            if int(currValue) > int(targetMax):
                listOfMaxCompanies = []
                listOfMaxCompanies.append({"companyName": companyName, "data": visaData[companyName]})
            # If the same, append to the list
            elif int(currValue) == int(targetMax):
                listOfMaxCompanies.append({"companyName": companyName, "data": visaData[companyName]})
            
    return [listOfMinCompanies, listOfMaxCompanies]

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
    
def initiateCommand(argument):
    command = argument["command"]
    visaData = argument["visaData"]
    target = argument["target"]
    mostRecentYear = argument["mostRecentYear"]
    
    if "company" in command:
        print("company?")
        #call getStatByCompanies
    # elif "state" in command:
    #     # call getCompaniesByState
    # call minimum and maximum then print
    elif "initApproval" in command:
        result = getCompaniesByColumn({"visaData": visaData, "columnName": "Initial Approvals", "mostRecentYear": mostRecentYear})

        minCompanies = result[0]
        maxCompanies = result[1]

        printMinAndMaxData({"maxList": maxCompanies, "minList": minCompanies, "mostRecentYear": mostRecentYear, "columnName": "Initial Approvals"})
    # call minimum and maximum then print
    elif "continuingApproval" in command:
        result = getCompaniesByColumn({"visaData": visaData, "columnName": "Continuing Approvals", "mostRecentYear": mostRecentYear})

        minCompanies = result[0]
        maxCompanies = result[1]

        printMinAndMaxData({"maxList": maxCompanies, "minList": minCompanies, "mostRecentYear": mostRecentYear, "columnName": "Continuing Approvals"})
    else:
        print("Please input a command that is valid\n")


