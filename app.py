from flask import Flask, render_template, request
from helper import *
from service import *
from verification import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def homePage():
    """Home Page for the Program"""
    return render_template('home.html', title='H-1B Data Hub')

@app.route('/companies/search', methods=['GET'])
def listCompaniesInState():
    """Give a list of Companies"""

    args = request.args
    state = args.get('state', type=str)
    minInitApproval = args.get('minInitApproval', type=str)

    # Verify the two features the program supports at the moment
    if state is None and minInitApproval is None:
        error = "Sorry, Address not Found. Please check your variable name one more time. (No Quotation Marks Please!)"
        return bad_request(error)

    # Get list for minInitApproval
    if state is None:
        # Check whether the threshold passed in as a number
        checkParam = containsNum(minInitApproval)
        if checkParam != True:
            error = minInitApproval + " is not a number." + " Please input a valid number!"
            return bad_request(error)

        fileToRead = "dummyData.csv"
        readOutput = readFile(fileToRead)
        visaData = readOutput[0]
        mostRecentYear = readOutput[1]

        # Get Companies List
        companiesList = getCompaniesByMinInitApproval({"visaData": visaData, "mostRecentYear": mostRecentYear, "target": minInitApproval})

        return render_template('listCompanies.html', type = "minInitApproval", mostRecentYear = mostRecentYear, companiesList = companiesList, target = minInitApproval )    
    # Get list for state
    else:
        # Check whether the state passed in as a string
        checkParam = containsNum(state)
            
        if checkParam != False:
            error = state + " is not a state." + " Please input a valid state!"
            return bad_request(error)

        fileToRead = "dummyData.csv"
        readOutput = readFile(fileToRead)
        visaData = readOutput[0]
        mostRecentYear = readOutput[1]

        # Get Companies List
        companiesList = getCompaniesByState({"visaData": visaData, "mostRecentYear": mostRecentYear, "target": state})

        return render_template('listCompanies.html', type = "state", mostRecentYear = mostRecentYear, companiesList = companiesList, target = state )    

def bad_request(errorMessage = "Your client has issued an invalid request.\n"):
    """Display 400 Error"""
    errorType = "400 Error"
    return render_template('error.html', errorTitle = errorType, errorMessage = errorMessage)

@app.errorhandler(400)
def bad_request_Handler(e):
    """Display 400 Error"""
    errorType = "400 Error"
    return bad_request()


@app.errorhandler(404)
def page_not_found(e):
    """Display 404 Error"""
    errorType = "404 Error"
    errorMessage = "Page not found: the requested URL was not found.\n"

    return render_template('error.html', errorTitle = errorType, errorMessage = errorMessage)

@app.errorhandler(500)
def python_bug(e):
    """Display 500 Error Page"""

    errorType = "500 Error"
    errorMessage = "An error occurred: We promise to fix this! Thank you for your patience.\n"

    return render_template('error.html', errorTitle = errorType, errorMessage = errorMessage)

if __name__ == '__main__':  
    # app.run(host='0.0.0.0', port=81)
    app.run()