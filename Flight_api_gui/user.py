# user.py
import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

        # Send confirmation email
        send_confirmation_email(email, flight_number)

    except mysql.connector.Error as error:
        print(f"Error: {error}")

    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydbconnection' in locals() and mydbconnection:
            mydbconnection.close()


def send_confirmation_email(email, flight_number):
    # Set up SMTP server configuration
    smtp_server = "smtp-mail.outlook.com"  # Update with your SMTP server
    smtp_port = 587  # Update with your SMTP port
    sender_email = "mahadinaeem00@outlook.com"  # Update with your email
    sender_password = "naeem2580NAEEM"  # Update with your email password

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Flight Booking Confirmation"

    # Email body
    body = f"Dear Passenger, your booking for flight number {
        flight_number} has been confirmed. Thank you for choosing our service!\n best regards\nteam members"
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Confirmation email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Failed to send confirmation email: {e}")

# Rest of the code remains unchanged
