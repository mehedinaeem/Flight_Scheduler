# user.py
import mysql.connector

db_name = "flight_info"

def book_flight():
    # Connect to the database
    mydbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database=db_name
    )

    mycursor = mydbconnection.cursor()

    # Check if the table exists, if not, create it
    mycursor.execute("SHOW TABLES LIKE 'user_info'")
    table_exists = mycursor.fetchone()

    if not table_exists:
        sqlquery = """
             CREATE TABLE user_info(
                flight_number varchar(10),
                name varchar(50),
                phone varchar(50),
                email varchar(50)
            )
        """
        mycursor.execute(sqlquery)
        print("Table created successfully")

    # Get user input for data
    flight_number = input("Enter your flight number: ")
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    # Insert data into the table
    sql_insert = "INSERT INTO user_info (flight_number, name, phone, email) VALUES (%s, %s, %s, %s)"
    values = (flight_number, name, phone, email)

    mycursor.execute(sql_insert, values)
    mydbconnection.commit()

    print("Data inserted successfully")

    # Close the cursor and the connection
    mycursor.close()
    mydbconnection.close()
