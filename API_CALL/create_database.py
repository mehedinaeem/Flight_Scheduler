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
    CREATE TABLE flight(
        flight_number varchar(10) primary key,
        departure_time datetime,
        departure_date datetime,
        arrival_place varchar(250),
        arrival_date datetime,
        arrival_time datetime,
        aircraft_type varchar(250),
        airline varchar(50),
        estimated_time varchar(50)
    )
    """

mycursor.execute(sqlquery)
print("create table succesfully")