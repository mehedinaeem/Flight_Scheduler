import mysql.connector

db_name = "send_mail"

# Create a connection without specifying the database
mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="naee2580"
)

# Create a cursor
mycursor = mydbconnection.cursor()

# Create the database if it doesn't exist
mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
print("connect succesfully")