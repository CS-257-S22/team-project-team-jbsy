import psycopg2
import config as config
from datasource_Helper import *

class CompanyInfo:
    """Class that converts read data from DB to readable data"""
    
    def __init__(self, companyStat):
        """Constructor for CompanyInfo Class"""
        
        self.fiscalYear = companyStat[0]
        self.name = companyStat[1]
        self.initialApprovals = companyStat[2]
        self.initialDenials = companyStat[3]
        self.continuingApprovals = companyStat[4]
        self.continuingDenials = companyStat[5]
        self.companyState = companyStat[6]
        self.companyCity = companyStat[7]
        self.companyZIP = companyStat[8] 

class DataSource:
    """Class that has methods regarding database connection and CRUD"""
        
    def __init__(self):
        """Constructor for DataSource Class"""
        
        self.connection = self.connect()

    def connect(self):
        """Connect to database based on the information in config file
        
        Returns:
            connection -- connection to the designated database
        """
        
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def executeQuery(self, query):
        """Method to Execute the given SQL Query
        
        Arguments:
            query (str) --  Formatted SQL Query

        Returns:
            resultList (tuple) -- tuple that contains wanted results from the database
        """

        try:
            #set up a cursor
            cursor = self.connection.cursor()
            
            cursor.execute(query)
            resultList = cursor.fetchall()
            
            return resultList if resultList != None else []
            
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getCompaniesStatistics(self, whereQuery):
        """Method to Select Companies based on the input user query
        
        Arguments:
            whereQuery (dict) --  User input value for company search

        Returns:
            companiesList (list) -- list of companies that satisfied the input conditions
        """

        finalQuery = Datasource_helper().formatQueryForGetCompanies(whereQuery)
        companiesResult = self.executeQuery(finalQuery)   
        
        companiesList = []
        
        # Format read data from DB
        for companyStat in companiesResult:
            companiesList.append(CompanyInfo(companyStat))
        
        return companiesList

    def getCompaniesForRanking(self, rankingCategory, fiscalYear):
        """Method to Select top 10 companies for categories based on the given fiscal year
        
        Arguments:
            rankingCategory (str) -- Column/category to use to get top 10 companies from
            fiscalYear (str) --  User selected value for fiscalYear

        Returns:
            companiesList (list) -- list of companies that fall in the top 10 ranking
        """
        
        
        queryForCategory = Datasource_helper().formatQueryForRanking(rankingCategory, fiscalYear)
        companiesResult = self.executeQuery(queryForCategory)   
        
        companiesList = []
        
        # Format read data from DB
        for companyStat in companiesResult:
            companiesList.append(CompanyInfo(companyStat))
        
        return companiesList
        
        
        

if __name__ == '__main__':
    my_source = DataSource()
    # my_source.getlistOfCompanies({"fiscalYear": "2022"})