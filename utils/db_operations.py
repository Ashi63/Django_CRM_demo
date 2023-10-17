import mysql.connector
'''
# create a connection with the mysql credientials
dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password= 'Motinagar1!'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("""
                     CREATE DATABASE invoice_processing_users'
                     """) 
'''
import mysql.connector

class DataBaseOperations:
    def __init__(self):
        try:
            self.dataBaseConnection = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Motinagar1!'
            )
            self.cursorObject = self.dataBaseConnection.cursor()
            self.dataBaseName = 'invoice_processing_users'
        except mysql.connector.Error as err:
            print(f"Error: {err}")

    def createDatabase(self):
        try:
            # Check if the database already exists
            self.cursorObject.execute(f"SHOW DATABASES LIKE '{self.dataBaseName}'")
            database_exists = self.cursorObject.fetchone()

            if not database_exists:
                # Database doesn't exist, create it
                dataBaseCreateQuery = f"CREATE DATABASE {self.dataBaseName}"
                self.cursorObject.execute(dataBaseCreateQuery)
                print("Database Created Successfully!")
            else:
                print("Database already exists.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            
    

# Usage
db = DataBaseOperations()
db.createDatabase()
