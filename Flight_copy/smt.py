# smt.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import mysql.connector

def send_email(recipient_email, subject, message):
    # Replace these placeholders with your email configuration
    sender_email = 'mahadinaeem00@gmail.com'
    sender_password = 'NAEEM2580naeem'

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    body = MIMEText(message)
    msg.attach(body)

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")

def send_email_on_delete(flight_number_param):
    # Connect to the database
    mydbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="naee2580",
        database="flight_info"
    )

    mycursor = mydbconnection.cursor()

    try:
        # Retrieve recipient email based on flight_number
        sql_select = "SELECT email FROM user_info WHERE flight_number = %s"
        mycursor.execute(sql_select, (flight_number_param,))
        recipient_email = mycursor.fetchone()

        # Send email only if user_info entry exists
        if recipient_email:
            recipient_email = recipient_email[0]  # Extract email from the tuple
            send_email(recipient_email, 'Flight Update', 'Your booked flight has been canceled.')

    except Exception as e:
        print(f"Error sending email on delete: {e}")

    finally:
        # Close the cursor and the connection
        mycursor.close()
        mydbconnection.close()

def send_email_on_update(flight_number_param):
    # Connect to the database
    mydbconnection = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="naee2580",
        database="flight_info"
    )

    mycursor = mydbconnection.cursor()

    try:
        # Retrieve recipient email based on flight_number
        sql_select = "SELECT email FROM user_info WHERE flight_number = %s"
        mycursor.execute(sql_select, (flight_number_param,))
        recipient_email = mycursor.fetchone()

        # Send email only if user_info entry exists
        if recipient_email:
            recipient_email = recipient_email[0]  # Extract email from the tuple
            send_email(recipient_email, 'Flight Update', 'Your booked flight details have been updated.')

    except Exception as e:
        print(f"Error sending email on update: {e}")

    finally:
        # Close the cursor and the connection
        mycursor.close()
        mydbconnection.close()
