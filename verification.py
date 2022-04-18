import helper


# Test whether company name exists in the data
def companyExist(input, filename):
    data = helper.readFile(filename)
    compData = data[0]
    if input in compData:
        return True
    else:
        return False

# Check whether column name exists in the data
def columnExist(input, filename):
    yearByData = list(filename.values())
    input = input.lower()


    for i in range(len(yearByData)):
        yearData = yearByData[i]
        colData = list(yearData.values())

    for i in range(len(colData)):
        colDataList = list(colData[i].keys())

    for i in range(len(colDataList)):
        colDataList[i] = colDataList[i].lower()

    if input in colDataList:
        return True

    elif input == "company" or input == "mininitapproval":
        return True

    else:
        return False

# Check if command only includes an integer
def containsNumber(value):
    if type(value) is not str:
        return False
    for character in value:
        if character == " ":
            return False
        elif character.isdigit() is False:
            return False
    return True

# Check if command line has the correct length
def commandLen(arg):
    if type(arg) is not list:
        return False
    if len(arg) >= 4:
        return True
    else:
        return False

# Check if target is valid (int/str depending on the commandline)
def inputValid(target, command):
    if (("company" in command) and (type(target) == str)):
        return True
    elif (("state" in command) and (type(target) == str)):
        return True
    elif (("minInitApproval" in command) and containsNumber(target)):
        return True
    else:
        print(target, command)
        return False