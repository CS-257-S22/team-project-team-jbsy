# method to get minimum and maximum of given column
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
