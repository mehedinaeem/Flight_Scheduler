import mysql.connector

db_name = "Flight_info"

mydbconnection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="naee2580",
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
            email varchar(50),
            FOREIGN KEY (flight_number) REFERENCES flight(flight_number)
        )
    """
    mycursor.execute(sqlquery)
    print("Table created successfully")

# Get user input for data
flight_number = input("Enter your flight number:")
name = input("Enter name: ")
phone = int(input("Enter phone number: "))
email = input("Enter email: ")

# Insert data into the table
sql_insert = "INSERT INTO user_info (flight_number,name, phone, email) VALUES (%s,%s, %s, %s)"
values = (flight_number,name, phone, email)

mycursor.execute(sql_insert, values)
mydbconnection.commit()

print("Data inserted successfully")

# Close the connection
mycursor.close()
mydbconnection.close()
