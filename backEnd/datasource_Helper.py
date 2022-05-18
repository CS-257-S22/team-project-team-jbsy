class Datasource_helper:
    """Class for helper function for Datasource"""
    
    def getBasicSelectQuery(self):
        """Get basic SELECT part of Query

        Returns:
            selectQuery (string) -- SELECT part of a basic query
        """
        
        # basic select query
        selectQuery = "SELECT fiscalYear, company, SUM(initialApprovals), SUM(initialDenials), SUM(continuingApprovals), SUM(continuingDenials), companyState, companyCity, companyZIP FROM companies" 
        
        return selectQuery
    
    def getBasicGroupByQuery(self):
        """Get basic GROUP BY part of Query

        Returns:
            groupByQuery (string) -- GROUP BY part of a basic query
        """
        
        # basic group by query
        groupByQuery = " GROUP BY fiscalYear, company, companyState, companyCity, companyZIP"
        
        return groupByQuery
    
    def getWhereQuery(self, fiscalYear):
        """Get basic GROUP BY part of Query
        
        Argument:
            fiscalYear (str) -- User input value for fiscal year

        Returns:
            whereQuery (string) -- WHERE part of a basic query including fiscal year
        """
        
        # basic where query with fiscal year
        whereQuery = " WHERE fiscalYear = " + fiscalYear
        
        return whereQuery
        
    def formatQueryForGetList(self, whereQuery):
        """Create Query based on user input

        Arguments:
            whereQuery (dict) --  User input value for company search

        Returns:
            finalQuery (string) -- Formated SQL query for company search
        """
        # List of Query Parameters
        minInitApproval = whereQuery["minInitApproval"] if "minInitApproval" in whereQuery else None
        fiscalYear = whereQuery["fiscalYear"] if "fiscalYear" in whereQuery else None
        company = whereQuery["name"] if "name" in whereQuery else None
        state = whereQuery["companyState"] if "companyState" in whereQuery else None
        
        # Create Basic where Query
        whereQuery = self.getWhereQuery(fiscalYear)
        
        # Having of Query is dependent of having a minimum threshold
        havingQuery = ""
        
        # When minInitApproval is passed in
        if minInitApproval != None:
            havingQuery = " HAVING SUM(initialApprovals) >= " + minInitApproval
        # When state is passed in
        if state != None:
            whereQuery = whereQuery + " AND companyState = " + "'" + state + "'"
        # When company is passed in
        if company != None:
            whereQuery = whereQuery + " AND company LIKE " + "'%" + company + "%'"           
            
        # Final formatted Query
        finalQuery = self.getBasicSelectQuery() + whereQuery + self.getBasicGroupByQuery() + havingQuery + ";"

        return finalQuery
    