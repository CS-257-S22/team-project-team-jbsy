import csv

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

def printData(dataToPrint):
    for x in dataToPrint:
        print(x + "\n")

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

        print(visaData["REDDY GI ASSOCIATES"]["2020"]["Initial Approvals"])
        return [visaData, mostRecentYear]


# readFile("dummyData.csv")


            
            


