import smtplib
import getpass

HOST = "smtp-mail.outlook.com"
PORT = 587

FROM_EMAIL = "mahadinaeem00@outlook.com"
TO_EMAIL = "mehedinaeem00@gmail.com"

try:
    # PASSWORD = getpass.getpass(prompt="Enter password: ")
    PASSWORD=""

    MESSAGE = """Subject: Test
    Testing use smtplib
    Sincerely
    Naeem """

    smtp = smtplib.SMTP(HOST, PORT)
    smtp.starttls()
    smtp.login(FROM_EMAIL, PASSWORD)
    smtp.sendmail(FROM_EMAIL, TO_EMAIL, MESSAGE)
    smtp.quit()
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")
