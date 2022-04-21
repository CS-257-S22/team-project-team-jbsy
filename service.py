from helper import printCompaniesInState, printCompany, printMinInitApproval, printUsage

def getCompaniesByState(arguments):
   """Get a list of companies within the input state

    Arguments:
    arguments -- dict for function arguments (dict)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)
        mostRecentYear -- the fiscal year to find data in (string)

    Returns:
    list -- a list that has all the companies (dict) that are within the state
    """
   if "target" not in arguments or "visaData" not in arguments or "mostRecentYear" not in arguments:
        print("Need all the data in argument")
        # raise ValueError
        return []

   state = arguments["target"] 
   visaData = arguments["visaData"]
   mostRecentYear = arguments["mostRecentYear"]

   companyList = []

   # add companies in a state to a list
   for j in visaData:
        if(visaData[j][mostRecentYear]["State"]==state):
            companyList.append({"companyName": j, "data": visaData[j]})
            
   return companyList  
        
def getStatByCompany(arguments):
    """Get a company that matches the given name

    Arguments:
    arguments -- dict for function arguments (dict)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)

    Returns:
    dict -- data of company
    """
    company = arguments["target"]
    visaData = arguments["visaData"]

    # Find and return company with the matching name
    if company in visaData:
        return {"companyName": company, "data": visaData[company]}
    else:
        return {}

def getCompaniesByMinInitApproval(arguments):
    """Get companies with a minimum threshold initial approval

    Arguments:
    arguments -- dict for function arguments (dict)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)
        mostRecentYear -- the fiscal year to find data in (string)

    Returns:
    list -- a list that has all the companies (dict) that have at least certain number of minimum initial approvals
    """

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
            companyList.append({"companyName": j, "data": visaData[j][mostRecentYear]})        
    return companyList;      

def initiateCommand(argument):
    """General function that interprets command and initates relevant function

    Arguments:
    arguments -- dict for function arguments (dict)
        command -- command line keyword user put in (string)
        target -- state put in via command line (string)
        visaData -- all the statistics of companies (dict)
        mostRecentYear -- the fiscal year to find data in (string)
    """

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
    
    elif "minInitApproval" in command:
        result = getCompaniesByMinInitApproval({"visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})
        printMinInitApproval({"companiesList":result, "target": target, "mostRecentYear": mostRecentYear})
    
    elif "usage" in command:
        printUsage()

    else:
        print("Please input a command that is valid\n")


