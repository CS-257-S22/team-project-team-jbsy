def formatQueryForGetList(whereQuery):
    
    # List of Query Strings
    minInitApproval = whereQuery["minInitApproval"] if "minInitApproval" in whereQuery else None
    fiscalYear = whereQuery["fiscalYear"] if "fiscalYear" in whereQuery else None
    company = whereQuery["name"] if "name" in whereQuery else None
    state = whereQuery["companyState"] if "companyState" in whereQuery else None

    # basic select query
    selectQuery = "SELECT fiscalYear, company, SUM(initialApprovals), SUM(initialDenials), SUM(continuingApprovals), SUM(continuingDenials), companyState, companyCity, companyZIP FROM companies" 
    # basic group by query
    groupByQuery = " GROUP BY fiscalYear, company, companyState, companyCity, companyZIP"
    # basic having query
    havingQuery = ""
    
    whereQuery = " WHERE fiscalYear = " + fiscalYear
    
    if minInitApproval != None:
        havingQuery = " HAVING SUM(initialApprovals) >= " + minInitApproval
    if state != None:
        whereQuery = whereQuery + " AND companyState = " + "'" + state + "'"
    if company != None:
        whereQuery = whereQuery + " AND company LIKE " + "'%" + company + "%'"           
        
    finalQuery = selectQuery + whereQuery + groupByQuery + havingQuery + ";"

    return finalQuery
  