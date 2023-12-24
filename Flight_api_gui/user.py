# user.py
import mysql.connector

db_name = "flight_info"

def book_flight(flight_number, name, phone, email):
    try:
        mydbconnection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="naee2580",
            database=db_name
        )

        mycursor = mydbconnection.cursor()

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

        sql_insert = "INSERT INTO user_info (flight_number, name, phone, email) VALUES (%s, %s, %s, %s)"
        values = (flight_number, name, phone, email)

        mycursor.execute(sql_insert, values)
        mydbconnection.commit()

        print("Data inserted successfully")

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydbconnection' in locals() and mydbconnection:
            mydbconnection.close()
