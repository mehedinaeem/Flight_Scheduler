class FlightAdmin:
    def __init__(self):
        self.flights = []  #use list
        self.available_seats = {}    #use dict
        
    #this for add flight
    def add_flight(self, flight_details, total_seats):
        flight_id = flight_details['id']
        self.flights.append(flight_details)
        self.available_seats[flight_id] = list(range(1, total_seats + 1))
        print("Flight added:", flight_details)

    #this method for update flight
    def update_flight(self, flight_id, updated_details):
        for flight in self.flights:
            if flight['id'] == flight_id:
                flight.update(updated_details)
                print(f"Flight {flight_id} updated:", updated_details)

    #its for delete flight
    def delete_flight(self, flight_id):
        self.flights = [flight for flight in self.flights if flight['id'] != flight_id]
        if flight_id in self.available_seats:
            del self.available_seats[flight_id]
        print(f"Flight {flight_id} deleted.")

    #its for show all flight
    def get_all_flights(self):
        return self.flights

    #available seat
    def get_available_seats(self, flight_id):
        return self.available_seats.get(flight_id, [])

    #for booking seat
    def book_seat(self, flight_id, seat_number):
        if flight_id in self.available_seats and seat_number in self.available_seats[flight_id]:
            self.available_seats[flight_id].remove(seat_number)
            print(f"Seat {seat_number} booked for Flight {flight_id}.")
        else:
            print(f"Seat {seat_number} is not available for Flight {flight_id}.")
