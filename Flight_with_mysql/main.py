"""
    **search flight
            Enter airport
            Enter date
            
    **booked flight
            Enter name
            Enter phone number
            Enter Email
"""

def main():
    while True:
        print("1. Search Flight")
        print("2. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            airport=input("Enter airport:")
            date=input("Enter Date: ")
            """
                see here the flight
                Then Booked flight
                just call flight.fy for do that
            """
            print("Booked Fight:")
            name=input("Enter Name:")
            number=int(input("Enter your phone number:"))
            mail=input("Enter your email:")
            """
                Then store that data in database
            """
if __name__ == "__main__":
    main()