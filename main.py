import sys
from helper import readFile 
from service import initiateCommand

# main function that reads command line
def readCommandLine():
    # Read the commandline as arg
    arg = sys.argv

    # Todo: Verify if arg data is correct
    fileData = readFile(arg[1])

    # all the H-1B data of company 
    visaData = fileData[0]
    mostRecentYear = fileData[1]
    command = arg[2]

    # the last elements in the command, either the target value we want to reach
    target = ' '.join(arg[3:])

    # Todo: Verify if target relevant (company name exists, or column name exists, etc)
    initiateCommand({"command": command, "visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})
    
readCommandLine()


# Commandline example

# python3 main.py dummyData.csv --company PULMONICS PLUS PLLC
# python3 main.py dummyData.csv --state CA
# python3 main.py dummyData.csv --minInitApproval 2