import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def delay_email(email, flight_number):
    # Set up SMTP server configuration
    smtp_server = "smtp-mail.outlook.com"  # Update with your SMTP server
    smtp_port = 587  # Update with your SMTP port
    sender_email = "mahadinaeem00@outlook.com"  # Update with your email
    sender_password = "naeem2580NAEEM"  # Update with your email password

    # Create message object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = "Flight Delay Notification"

    # Email body
    body = f"Dear Passenger, your flight with number {
        flight_number} has been delayed."
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Create SMTP session and send the email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Delay notification email sent successfully!")
        server.quit()
    except Exception as e:
        print(f"Failed to send delay notification email: {e}")


def get_emails():
    try:
        mydbconnection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="naee2580",
            database="flight_info"  # Update with your database name
        )

        mycursor = mydbconnection.cursor()

        mycursor.execute("SELECT email FROM user_info")

        emails = mycursor.fetchall()

        # Extracting emails from the fetched data
        email_list = [email[0] for email in emails]

        return email_list

    except mysql.connector.Error as error:
        print(f"Error: {error}")
        return []

    finally:
        if 'mycursor' in locals() and mycursor:
            mycursor.close()
        if 'mydbconnection' in locals() and mydbconnection:
            mydbconnection.close()


def check_delay(email_list, flight_info):
    # Function to check for flight delays and send notifications
    for flight in flight_info:
        # Replace with the key for scheduled arrival time in your flight_info
        scheduled_arrival_str = flight.get('Scheduled Arrival')
        # Replace with the key for actual arrival time in your flight_info
        actual_arrival_str = flight.get('Actual Arrival')

        if scheduled_arrival_str and actual_arrival_str:
            scheduled_arrival = datetime.strptime(
                scheduled_arrival_str, '%Y-%m-%d %H:%M:%S')
            actual_arrival = datetime.strptime(
                actual_arrival_str, '%Y-%m-%d %H:%M:%S')

            if actual_arrival > scheduled_arrival:
                # Replace with the key for flight number in your flight_info
                flight_number = flight.get('Flight Number')
                delayed_flight_info = f"Flight {flight_number} has been delayed.\nScheduled Arrival: {
                    scheduled_arrival}\nActual Arrival: {actual_arrival}"
                # Send delay notifications to each email in the email_list
                for email in email_list:
                    delay_email(email, flight_number, delayed_flight_info)
