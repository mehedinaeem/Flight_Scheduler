import smtplib

def send_email(to_email, subject, message):
    HOST = "smtp-mail.outlook.com"
    PORT = 587
    FROM_EMAIL = "mahadinaeem00@outlook.com"
    PASSWORD = "naeem2580NAEEM"

    try:
        smtp = smtplib.SMTP(HOST, PORT)
        smtp.starttls()
        smtp.login(FROM_EMAIL, PASSWORD)

        email_message = f"Subject: {subject}\n\n{message}"

        smtp.sendmail(FROM_EMAIL, to_email, email_message)
        smtp.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
