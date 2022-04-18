import helper


# Test whether company name exists in the data
def companyExist(input, filename):
    data = helper.readFile(filename)
    compData = data[0]
    # print(compData)
    if input in compData:
        return True
    else:
        return False

# Check whether column name exists in the data
def columnTest(input, filename):
    yearByData = list(filename.values())

    for i in range(len(yearByData)):
        yearData = yearByData[i]
        colData = list(yearData.values())

    for i in range(len(colData)):
        colDataList = list(colData[i].keys())

    for i in range(len(colDataList)):
        colDataList[i] = colDataList[i].lower()

    if input in colDataList:
        return True

    elif input == "company" or input == "minInitApproval":
        return True

    else:
        # print(colDataList)
        return False

# Check if command includes integer
def containsNumber(value):
    for character in value:
        if character.isdigit():
            return True
    return False

# Check if command line has the correct length
def commandLen(arg):
    if len(arg) > 4:
        return True
    else:
        return False

# Check if input is valid (int/str depending on the commandline)
def inputValid(input, command):
    if (("company" in command) and (type(input) == str)):
        return True
    elif (("state" in command) and (type(input) == str)):
        return True
    # Todo: Create Error when "python3 main.py dummyData.csv --minInitApproval 6 7"
    elif (("minInitApproval" in command) and containsNumber(input)):
        return True
    else:
        return False

# print(companyExist('REDDY GI ASSOCIATE', "dummyData.csv"))
# print(columnTest('City', "dummyData.csv"))
