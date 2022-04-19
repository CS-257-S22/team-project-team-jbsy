from helper import printCompaniesInState, printCompany, printMinInitApproval

# method to get the names of companies within the input state
def getCompaniesByState(arguments):
   state = arguments["target"] 
   visaData = arguments["visaData"]
   mostRecentYear = arguments["mostRecentYear"]

   companyList = []

   # add companies in a state to a list
   for j in visaData:
        if(visaData[j][mostRecentYear]["State"]==state):
            companyList.append({"companyName": j, "data": visaData[j]})
            
   return companyList  
        
# method to get the statistics of the input company
def getStatByCompany(arguments):
    company = arguments["target"]
    visaData = arguments["visaData"]

    # Find and return company with the matching name
    if company in visaData:
        return {"companyName": company, "data": visaData[company]}
    else:
        return {}

# method to get companies with a minimum threshold initial approval
def getCompaniesByMinInitApproval(arguments):
    if "target" not in arguments or "visaData" not in arguments or "mostRecentYear" not in arguments:
        print("Need all the data in argument")
        # raise ValueError
        return []
        

    initApproval  = arguments["target"]
    visaData = arguments["visaData"]
    mostRecentYear = arguments["mostRecentYear"]

    companyList = []
    for j in visaData:
        if(int(visaData[j][mostRecentYear]["Initial Approvals"]) >= int(initApproval)):
            #  companyList.append(visaData[j][mostRecentYear]["Employer"] + " in Year " + visaData[j][mostRecentYear]["Fiscal Year"] + "\n");
            companyList.append({"companyName": j, "data": visaData[j][mostRecentYear]})        
    return companyList;      

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
    
    # Give stat for a company
    if "company" in command:
        company = getStatByCompany({"visaData": visaData, "target": target})
        printCompany(company)

    # Give companies in a state
    elif "state" in command:
        companyList = getCompaniesByState({"visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})
        printCompaniesInState(companyList, target)

    # call minimum and maximum then print
    elif "initApproval" in command:
        result = getCompaniesByColumn({"visaData": visaData, "columnName": "Initial Approvals", "mostRecentYear": mostRecentYear})

        minCompanies = result[0]
        maxCompanies = result[1]

        printMinAndMaxData({"maxList": maxCompanies, "minList": minCompanies, "mostRecentYear": mostRecentYear, "columnName": "Initial Approvals"})
    
    elif "minInitApproval" in command:
        result = getCompaniesByMinInitApproval({"visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})

        # companyList = result[0]

        printMinInitApproval({"companiesList":result, "target": target, "mostRecentYear": mostRecentYear})
    
    # call minimum and maximum then print
    elif "continuingApproval" in command:
        result = getCompaniesByColumn({"visaData": visaData, "columnName": "Continuing Approvals", "mostRecentYear": mostRecentYear})

        minCompanies = result[0]
        maxCompanies = result[1]

        printMinAndMaxData({"maxList": maxCompanies, "minList": minCompanies, "mostRecentYear": mostRecentYear, "columnName": "Continuing Approvals"})
    else:
        print("Please input a command that is valid\n")


