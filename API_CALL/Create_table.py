# connection
import mysql.connector

db_name = "send_mail"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database=db_name
)

mycursor = mydbconnection.cursor()

#  values = (flight_number, departure_time, departure_date, arrival_place,
#                       arrival_date, arrival_time, aircraft_type, airline, estimated_time)

sqlquery = """
    CREATE TABLE user_data(
        Name varchar(10),
        phone_number varchar(250) primary key,
        mail varchar(50)
    )
"""

mycursor.execute(sqlquery)
print("create table successfully")
