from verification import Verification

class ControllerHelper:

    def validateQueryString(self,queryArgs):
        """Check if inputValue is apporpriate for query type

        Arguments:
            queryArgs -- dict of queries passed in from URL

        Returns:
            string -- error message or empty string 
        """
        verification = Verification()

        minInitApproval = queryArgs.get('minInitApproval', type=str)
        state = queryArgs.get('state', type=str)

        if minInitApproval:
            # Check whether the threshold passed in is integer
            if verification.containsNum(minInitApproval) != True:
                return minInitApproval + " is not a number." + " Please input a valid number!"
        if state:
            # Check whether the state passed in is string
            if verification.containsNum(state) != False:
                return state + " is not a state." + " Please input a valid state!"

        else:
            return ""

    def processQuery(self, queryArgs):
        """Get companies list based on the query type (Filter)

        Arguments:
            queryType -- type of query to process request (str)
            inputValue -- input value that user put in (str)

        Returns:
            dict -- a dictionary that contains necessary information for conditions in fetching data from database
        """

        # List of Query Strings
        minInitApproval = queryArgs.get('minInitApproval', type=str) or ""
        fiscalYear = queryArgs.get('year', type=str) or "2022"
        company = queryArgs.get('company', type=str) or ""
        state = queryArgs.get('state', type=str) or ""

        whereQuery= {"fiscalYear": fiscalYear}

        # If minInitApproval is valid
        if minInitApproval:
            whereQuery["minInitApproval"] = minInitApproval
        # If state is valid and not a default value
        if state and state != "-":
            whereQuery["companyState"] = state     
        # If company name was specified
        if company:
            companyName = company.upper()
            whereQuery["name"] = companyName

        return whereQuery