import csv

# Returns column name by the index of array
def getColumnNameByIndex(index):
    if index == 0:
        return "Fiscal Year"
    elif index == 1:
        return "Employer"
    elif index == 2:     
        return "Initial Approvals"
    elif index == 3:    
        return "Initial Denials"
    elif index == 4:
        return "Continuing Approvals"
    elif index == 5:
        return "Continuing Denials"
    elif index == 6:
        return "NAICS"
    elif index == 7:
        return "Tax ID"
    elif index == 8:
        return "State"
    elif index == 9:
        return "City"
    elif index == 10:
        return "ZIP"
    else:
        return ""

# Creates a formatted arrary with data by fiscal year
def createDataByYear(lineData):

    # If no line is read, return an empty list
    if len(lineData) == 0:
        return []

    # Which year is it
    fiscalYear = lineData[0]

    # Each data in year
    dataByYear = {}
    for i in range(len(lineData)):
        columnName = getColumnNameByIndex(i)
        dataByYear[columnName] = lineData[i]

    # Return a list that has data by fiscal year
    return [fiscalYear, dataByYear]

def printUsage():
   usageText = open("usage.txt","r")
   print(usageText.read())

#prints list of companies with initial approval above a certian threshold
def printMinInitApproval(data):
    companiesList = data["companiesList"]
    initApproval = data["target"]
    # mostRecentYear = data["mostRecentYear"]

    if len(companiesList) == 0:
        print("No companies exist with Initial Approval above " + initApproval)
    else:     
        print("\nCompanies with Minimum Initial Approval of " + initApproval +":\n")

        companiesName = ""
        for name in companiesList:
            companiesName += name["companyName"] + "\n"
        
        print(companiesName)

# Print list of companies in a state
def printCompaniesInState(companiesList, state):
    if len(companiesList) == 0:
        print("No companies exist in a given state")
    else:     
        print("\nCompanies located in " + state +":\n")

        companiesName = ""
        for name in companiesList:
            companiesName += name["companyName"] + "\n"
        
        print(companiesName)

# Print statistics of a company
def printCompany(companyData):
    if companyData == {}:
        print("Company does not exist in dataset")
    else:
        print("\nStatistic for " +companyData["companyName"]+": \n")

        statsForCompany = ""
        companyStat = companyData["data"]

        for year in companyStat:
            statsForCompany = statsForCompany + "Fiscal Year => " + companyStat[year]["Fiscal Year"]  + "\n"
            # statsForCompany = statsForCompany + "Employer => " + companyStat[year]["Employer"]  + "\n"
            statsForCompany = statsForCompany + "Initial Approvals => " + companyStat[year]["Initial Approvals"] + "\n"
            statsForCompany = statsForCompany + "Initial Denials => " + companyStat[year]["Initial Denials"] + "\n"
            statsForCompany = statsForCompany + "Continuing Approvals => " + companyStat[year]["Continuing Approvals"] + "\n"
            statsForCompany = statsForCompany + "Continuing Denials => " + companyStat[year]["Continuing Denials"] + "\n"
            statsForCompany = statsForCompany + "NAICS => " + companyStat[year]["NAICS"] + "\n"
            statsForCompany = statsForCompany + "Tax ID => " + companyStat[year]["Tax ID"] + "\n"
            statsForCompany = statsForCompany + "State => " +companyStat[year]["State"] + "\n"
            statsForCompany = statsForCompany + "City => " + companyStat[year]["City"] + "\n"
            statsForCompany = statsForCompany + "ZIP => " + companyStat[year]["ZIP"] + "\n\n"
        
        print(statsForCompany)

# Reads a csv file and organizes data
def readFile(filePath):
    # open file
    with open(filePath, 'r') as file:
        reader = csv.reader(file)
        lineCount = 0
        mostRecentYear = "2018"

        # Dictionary for Overall Data
        visaData = {}

        for line in reader:
            # Skip First line in csv file
            if lineCount == 0:
            # column = line.split(",")
                lineCount+=1
            else:
                lineCount+=1
                companyName = line[1]
                fiscalYear = line[0]

                if int(mostRecentYear) < int(fiscalYear):
                    mostRecentYear = fiscalYear

                companyData = createDataByYear(line)

                # If no data, continue
                if len(companyData) == 0:
                    continue 

                fiscalYear = companyData[0]
                companyDataByYear = companyData[1]

                if companyName not in visaData:
                    visaData[companyName] = {fiscalYear: companyDataByYear}
                else:
                    visaData[companyName][fiscalYear] = companyDataByYear

        # print(visaData["REDDY GI ASSOCIATES"])
        # printData(visaData)
        return [visaData, mostRecentYear]



            
            


