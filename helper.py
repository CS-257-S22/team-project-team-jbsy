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
    else:
        return "ZIP"

# Creates a formatted arrary with data by fiscal year
def createDataByYear(lineData):
    # Which year is it
    fiscalYear = lineData[0]

    # Each data in year
    dataByYear = {}
    for i in range(len(lineData)):
        columnName = getColumnNameByIndex(i)
        dataByYear[columnName] = lineData[i]

    # Return a list that has data by fiscal year
    return [fiscalYear, dataByYear]

# Prints list of companies with minimum and maximum column value
def printMinAndMaxData(data):
    maxCompanies = data["maxList"]
    minCompanies = data["minList"]
    mostRecentYear = data["mostRecentYear"]
    columnName = data["columnName"]

    print("\nHere is the list of Companies with Maximum Number of " + columnName + " with " + columnName.lower() + " of " + maxCompanies[0]["data"][mostRecentYear][columnName] + ":\n")
    for x in maxCompanies:
        print(x["companyName"])

    print("\nHere is the list of Companies with Minimum Number of " + columnName + " with " + columnName.lower() +" of " + minCompanies[0]["data"][mostRecentYear][columnName] + ":\n")
    for x in minCompanies:
        print(x["companyName"])

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

                fiscalYear = companyData[0]
                companyDataByYear = companyData[1]

                if companyName not in visaData:
                    visaData[companyName] = {fiscalYear: companyDataByYear}
                else:
                    visaData[companyName][fiscalYear] = companyDataByYear

        # print(visaData["REDDY GI ASSOCIATES"])
        # printData(visaData)
        return [visaData, mostRecentYear]

# readFile("dummyData.csv")


            
            


