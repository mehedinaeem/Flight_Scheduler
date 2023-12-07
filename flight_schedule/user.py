from datetime import datetime

class User:
    def __init__(self):
        self.booked_seats = {}

    #flight khuja
    def search_flights(self, search_criteria, flights, admin):
        results = []
        for flight in flights:
            if all(flight[key] == value for key, value in search_criteria.items()):
                results.append(flight)
        return results

    def subscribe_to_delay_notifications(self, flight_id, email):
        # Placeholder for subscribing to delay notifications
        print(f"Subscribed to delay notifications for Flight {flight_id} at {email}")

    def book_flight_seat(self, flight_id, seat_number):
        if flight_id not in self.booked_seats:
            self.booked_seats[flight_id] = []

        if seat_number not in self.booked_seats[flight_id]:
            self.booked_seats[flight_id].append(seat_number)
            print(f"Seat {seat_number} booked for Flight {flight_id}.")
        else:
            print(f"Seat {seat_number} is already booked for Flight {flight_id}.")

    def show_available_seats(self, flight_id, admin):
        available_seats = admin.get_available_seats(flight_id)
        if available_seats:
            print(f"Available seats for Flight {flight_id}: {available_seats}")
        else:
            print(f"No available seats for Flight {flight_id}.")
