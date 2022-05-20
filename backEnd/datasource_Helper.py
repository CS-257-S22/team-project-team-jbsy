class Datasource_helper:
    """Class for helper function for Datasource"""
    
    def formatCategoryToColumn(self, category):
        """Format category name to relevant column name 

        Arguments:
            category (str) -- Column/category to use

        Returns:
            columnName (string) -- Category converted to relevant column name in DB
        """
        
        return "SUM("+category+")"

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
     
    def getBasicOrderByQuery(self, category, order = "DESC"):
        """Get basic ORDER BY part of Query
        
        Arguments:
            category (str) -- Column/category to use to get top 10 companies from
            order (str) --  Order of order by, ASC or DESC

        Returns:
            orderByQuery (string) -- ORDER BY part of a basic query
        """     
        
        # basic orderBy query with fiscal year
        orderByQuery = " ORDER BY " + category + " " + order
        
        return orderByQuery
    
    def getLimitQuery(self, limitNum):
        """Get LIMIT part of Query
        
        Arguments:
            limitNum (int) -- Number of records to get from DB

        Returns:
            limitQuery (string) -- LIMIT part of a basic query
        """
        
        # limit query
        limitQuery = " LIMIT " + str(limitNum)
        
        return limitQuery
        
    def formatQueryForGetCompanies(self, whereQuery):
        """Create Query based on user input for get companies

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
    
    def formatQueryForRanking(self, rankingCategory, fiscalYear):
        """Create Query based on fiscal year for ranking search

        Arguments:
            rankingCategory (str) -- Column/category to use to get top 10 companies from
            fiscalYear (str) --  User selected value for fiscalYear

        Returns:
            finalQuery (string) -- Formated SQL query for ranking search
        """
    
        # Create Basic where Query
        whereQuery = self.getWhereQuery(fiscalYear)
        
        # Column to select from
        columnName = self.formatCategoryToColumn(rankingCategory)
        
        # Final formatted Query
        finalQuery = self.getBasicSelectQuery() + whereQuery + self.getBasicGroupByQuery() + self.getBasicOrderByQuery(columnName) + self.getLimitQuery(10) + ";"

        return finalQuery
        