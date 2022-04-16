import sys
from helper import readFile 
from service import initiateCommand

def readCommandLine():
    # Read the commandline as arg
    arg = sys.argv

    # Todo: Verify if arg data is correct
    fileData = readFile(arg[1])

    # all the H-1B data of company 
    visaData = fileData[0]
    mostRecentYear = fileData[1]
    command = arg[2]
    # the last element in the command
    target = arg[-1]

    # Todo: Verify if target relevant (company name exists, or column name exists, etc)
    initiateCommand({"command": command, "visaData": visaData, "target": target, "mostRecentYear": mostRecentYear})
    
readCommandLine()

# project.py dummyData.csv --company "Google"

# Commandline example
# python3 project.py dummyData.csv --company "Google"