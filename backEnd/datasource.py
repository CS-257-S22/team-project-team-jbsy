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

    def getlistOfCompanies(self, whereQuery):
        """Method to Select Companies in given state and year"""
        try:
            #set up a cursor
            cursor = self.connection.cursor()
            
            finalQuery = Datasource_helper().formatQueryForGetList(whereQuery)
                    
            cursor.execute(finalQuery)
            companiesList = cursor.fetchall()
            
            return companiesList if companiesList != None else []
           
        except Exception as e:
            print ("Something went wrong when executing the query: ", e)
            return None

if __name__ == '__main__':
    my_source = DataSource()
    # my_source.getlistOfCompanies({"fiscalYear": "2022"})