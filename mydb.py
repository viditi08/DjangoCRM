import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost" ,
    user = "root",
    passwd = "135790Viditi08&@"
)

#prepare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE CRM")

print("All Done!")