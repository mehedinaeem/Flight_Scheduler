from admin import FlightAdmin
from user import User
from datetime import datetime  #For import date & time

def main():
    # make object 
    admin = FlightAdmin()
    user = User()

    while True:
        print("1. Admin Panel")
        print("2. User Panel")
        print("3. Exit")
        choice = input("Enter your choice: ")
        

#------------------------------Admin panel---------------------------------------------------
        if choice == "1":
            # Admin Panel
            print("1. Add Flight")
            print("2. Update Flight")
            print("3. Delete Flight")
            admin_choice = input("Enter your admin choice: ")

            if admin_choice == "1":
                
                # store flight details in a dictionary
                
                flight_details = {
                    'id': input("Flight ID: "),
                    'name': input("Flight Name: "),
                    'date': input("Date (YYYY-MM-DD): "),  # Change to date input
                    'depurtime_time':input("Departure Time: "),
                    'destination': input("Destination: "),
                }
                
                #its out of dict before it changing time to time
                total_seats = int(input("Total Seats: "))
                admin.add_flight(flight_details, total_seats)

            elif admin_choice == "2":
                #update a specific flight
                flight_id = input("Enter the Flight ID to update: ")
                updated_details = {
                    'name': input("New Flight Name: "),
                    'date': input("New Date (YYYY-MM-DD): "),  # Change to date input
                    'depurtime_time':input("New departure Time: "),
                    'destination': input("New Destination: "),
                }
                admin.update_flight(flight_id, updated_details)

            elif admin_choice == "3":
                flight_id = input("Enter the Flight ID to delete: ")
                admin.delete_flight(flight_id)
                
                
#----------------------------------------User part-------------------------------

        elif choice == "2":
            print("User Panel")
            print("1. Search Flights")
            print("2. Subscribe to Delay Notifications")
            print("3. Book a Seat")
            print("4. Show Available Seats")
            user_choice = input("Enter your user choice: ")

            if user_choice == "1":
                search_criteria = {
                    'destination': input("Enter Destination: "),
                    'date': input("Enter Date (YYYY-MM-DD): "),  # Change to date input
                }
                flights = admin.get_all_flights()
                search_results = user.search_flights(search_criteria, flights, admin)
                
                print("Search Results:")
                # for result in search_results:
                #     print(result)
                if search_results:
                    for result in search_results:
                        print(result)
                else:
                    print("No flight available")

            elif user_choice == "2":
                #TODO: send notification if delay
                flight_id = input("Enter Flight ID to subscribe to delay notifications: ")
                email = input("Enter your email: ")
                user.subscribe_to_delay_notifications(flight_id, email)

            elif user_choice == "3":
                flight_id = input("Enter Flight ID to book a seat: ")
                seat_number = int(input("Enter the seat number: "))
                admin.book_seat(flight_id, seat_number)

            elif user_choice == "4":
                flight_id = input("Enter Flight ID to show available seats: ")
                user.show_available_seats(flight_id, admin)

        elif choice == "3":
            print("Exiting the application.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
