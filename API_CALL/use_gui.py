import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QPushButton, QInputDialog

class FlightInfoApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Flight Information')
        self.setGeometry(100, 100, 800, 600)

        self.text_output = QTextEdit()
        self.text_output.setReadOnly(True)

        self.btn_get_info = QPushButton('Get Flight Information')
        self.btn_get_info.clicked.connect(self.get_flight_info)

        layout = QVBoxLayout()
        layout.addWidget(self.text_output)
        layout.addWidget(self.btn_get_info)

        self.setLayout(layout)

    def get_flight_info(self):
        # Create a list to store the flight information for each flight.
        flights = []

        # Get the list of flight numbers from the user.
        flight_numbers = self.input_flight_numbers()

        # Iterate over the list of flight numbers and retrieve the flight
        # information for each flight.
        for flight_number in flight_numbers:
            url = "https://flight-info-api.p.rapidapi.com/status"
            querystring = {
                "DepartureAirport": "DAC",
                "DepartureDateTime": "2023-11-20T12:00/2023-11-25T12:00",
                "CodeType": "IATA",
                "FlightType": "Scheduled",
                "version": "v2",
                "ServiceType": "Passenger",
                "flightNumber": flight_number
            }
            headers = {
                "X-RapidAPI-Key": "78310b8c57mshcf3285739dee2d8p1e00aajsn10f7a10af72f",
                "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
            }

            response = requests.get(url, headers=headers, params=querystring)

            if response.status_code == 200:
                try:
                    flight_data = response.json()
                    flights.append(flight_data)
                except ValueError as e:
                    self.text_output.setText(f"Error decoding JSON: {e}")
            else:
                self.text_output.setText(f"Failed to retrieve data. Status code: {response.status_code}\nError message: {response.text}")

        # Update the output loop to display the flight information for each
        # flight in the list.
        output = ""
        for flight in flights:
            flight_number = flight.get('flightNumber')
            departure_time = flight.get('departure', {}).get('time', {}).get('local')
            departure_date = flight.get('departure', {}).get('date', {}).get('local')
            arrival_place = flight.get('arrival', {}).get('airport', {}).get('iata')
            arrival_date = flight.get('arrival', {}).get('date', {}).get('local')
            arrival_time = flight.get('arrival', {}).get('time', {}).get('local')
            aircraft_type = flight.get('aircraftType', {}).get('iata')
            airline = flight.get('carrier', {}).get('iata')
            estimated_time = flight.get('elapsedTime')

            output += f"Flight Number: {flight_number}\n"
            output += f"Departure Time: {departure_time}\n"
            output += f"Departure Date: {departure_date}\n"
            output += f"Arrival Place: {arrival_place}\n"
            output += f"Arrival Date: {arrival_date}\n"
            output += f"Arrival Time: {arrival_time}\n"
            output += f"Aircraft Type: {aircraft_type}\n"
            output += f"Airline: {airline}\n"
            output += f"Estimated Time: {estimated_time} minutes\n"
            output += "-------------------------------\n"

        self.text_output.setText(output)

    def input_flight_numbers(self):
        # Function to take user input for flight numbers.
        flight_numbers, ok_pressed = QInputDialog.getText(self, "Enter Flight Numbers",
                                                         "Enter flight numbers separated by comma (,):")

        # Split the input by comma and remove any leading/trailing spaces.
        flight_numbers = [num.strip() for num in flight_numbers.split(',') if num.strip()]
        return flight_numbers

def main():
    app = QApplication(sys.argv)
    window = FlightInfoApp()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
