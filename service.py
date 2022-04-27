from helper import printCompaniesInState, printCompany, printMinInitApproval, printUsage

def getCompaniesByState(userInput):
   """Get a list of companies within the input state

    Arguments:
    userInput -- dict for function getCompaniesByState (dict)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)
        mostRecentYear -- the fiscal year to find data in (string)

    Returns:
    list -- a list that has all the companies (dict) that are within the state
    """
   if "target" not in userInput or "visaData" not in userInput or "mostRecentYear" not in userInput:
        print("Need all the data in argument")
        # raise ValueError
        return []

   state = userInput["target"] 
   visaData = userInput["visaData"]
   mostRecentYear = userInput["mostRecentYear"]

   companyList = []

   # add companies in a state to a list
   for j in visaData:
        if(visaData[j][mostRecentYear]["State"]==state):
            companyList.append({"companyName": j, "data": visaData[j]})
            
   return companyList  
        
def getStatByCompany(userInput):
    """Get a company that matches the given name

    Arguments:
    userInput -- dict for function getStatByCompany (dict)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)

    Returns:
    dict -- data of company
    """
    company = userInput["target"]
    visaData = userInput["visaData"]

    # Find and return company with the matching name
    if company in visaData:
        return {"companyName": company, "statistic": visaData[company]}
    else:
        return {}

def getCompaniesByMinInitApproval(userInput):
    """Get companies with a minimum threshold initial approval

    Arguments:
    userInput -- dict for function getCompaniesByMinInitApproval (dict)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)
        mostRecentYear -- the fiscal year to find data in (string)

    Returns:
    list -- a list that has all the companies (dict) that have at least certain number of minimum initial approvals
    """

    if "target" not in userInput or "visaData" not in userInput or "mostRecentYear" not in userInput:
        print("Need all the data in argument")
        # raise ValueError
        return []
        
    initApproval  = userInput["target"]
    visaData = userInput["visaData"]
    mostRecentYear = userInput["mostRecentYear"]

    companyList = []
    for j in visaData:
        if(int(visaData[j][mostRecentYear]["Initial Approvals"]) >= int(initApproval)):
            companyList.append({"companyName": j, "statistic": visaData[j][mostRecentYear]})        
    return companyList;      

def initiateCommand(userInput):
    """General function that interprets command and initates relevant function

    Arguments:
    userInput -- dict for function initiateCommand (dict)
        command -- command line keyword user put in (string)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)
        mostRecentYear -- the fiscal year to find data in (string)
    """

    command = userInput["command"]
    visaData = userInput["visaData"]
    target = userInput["target"]
    mostRecentYear = userInput["mostRecentYear"]
    
    # Give stat for a company
    if "company" in command:
        company = getStatByCompany({"visaData": visaData, "target": target})
        printCompany(company)

    # Give companies in a state
    elif "state" in command:
        companyList = getCompaniesByState({"visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})
        printCompaniesInState(companyList, target)
    
    elif "minInitApproval" in command:
        result = getCompaniesByMinInitApproval({"visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})
        printMinInitApproval({"companiesList":result, "target": target, "mostRecentYear": mostRecentYear})
    
    elif "usage" in command:
        printUsage()

    else:
        print("Please input a command that is valid\n")


