import psycopg2
import config as config
from datasource_Helper import *

class DataSource:
    """Class that has methods regarding database connection and CRUD"""
        
    def __init__(self):
        """Constructor for DataSource Class"""
        
        self.connection = self.connect()

    def connect(self):
        """Connect to database based on the information in config file"""
        
        try:
            connection = psycopg2.connect(database=config.database, user=config.user, password=config.password, host="localhost")
        except Exception as e:
            print("Connection error: ", e)
            exit()
        return connection

    def executeQuery(self, query):

        try:
            #set up a cursor
            cursor = self.connection.cursor()
            
            cursor.execute(query)
            resultList = cursor.fetchall()
            
            return resultList if resultList != None else []
            
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

    def getlistOfCompanies(self, whereQuery):
        """Method to Select Companies in given state and year"""

        finalQuery = Datasource_helper().formatQueryForGetList(whereQuery)
        companiesList = self.executeQuery(finalQuery)   
        return companiesList      

if __name__ == '__main__':
    my_source = DataSource()
    # my_source.getlistOfCompanies({"fiscalYear": "2022"})