# connection
import mysql.connector

db_name="Flight_info"

mydbconnection=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="naee2580",
    database=db_name
)




mycursor=mydbconnection.cursor()

#  values = (flight_number, departure_time, departure_date, arrival_place,
#                       arrival_date, arrival_time, aircraft_type, airline, estimated_time)


sqlquery= """
    CREATE TABLE user_info(
        name varchar(50),
        phone int,
        email varchar(50)
    )
    """

mycursor.execute(sqlquery)
print("create table succesfully")