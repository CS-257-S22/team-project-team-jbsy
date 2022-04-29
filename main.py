import sys
from helper import printUsage, readFile 
from service import initiateCommand
from verification import columnExist, companyExist, commandLen, inputValid


def readCommandLine():
    """Main function that reads command line"""

    # Read the commandline as arg
    arg = sys.argv

    # Check if the command includes enough arguments
    if not commandLen(arg):
        # Prints Usage then return
        if "--usage" in arg:
            printUsage()
            return
        # Return to Test
        elif "test.py" in arg:
            return
        else:
            print("Command Line Error, Please check if your command is in a correct format.\n")
            print("Command for running tests => python3 test.py")
            print("Command for displaying usage => python3 main.py --usage")
            print("Example Command for Company Search => python3 main.py dummyData.csv --company PULMONICS PLUS PLLC")
            print("Example Command for Company State Search => python3 main.py dummyData.csv --state CA")
            print("Example Command for minInitApproval Search => python3 main.py dummyData.csv --minInitApproval 2")

            print("\nFor more information, please check our README!\n")
            return

    fileData = readFile(arg[1])
    if fileData == False:
        return

    # all the H-1B data of company 
    visaData = fileData[0]
    mostRecentYear = fileData[1]
    command = arg[2]

    # the last elements in the command, either the target value we want to reach
    target = ' '.join(arg[3:])

    # if input command does not match with the target value, print error message
    if not inputValid(target, command):
        print("Invalid Input : command does not match with target")
        return

    # if input command is not a valid command, print error message
    if not columnExist(command[2:], visaData):
        print("Invalid Command : command is not in column")
        return
    
    # when searching for company, if the company does not exist, print error message
    if ("company" in command):
        if not companyExist(target, arg[1]):
            print("Invalid Company : Input company does not exist")
            return

    initiateCommand({"command": command, "visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})

readCommandLine()

# Commandline example

# python3 main.py dummyData.csv --company PULMONICS PLUS PLLC
# python3 main.py dummyData.csv --state CA
# python3 main.py dummyData.csv --minInitApproval 2
# python3 main.py --usage