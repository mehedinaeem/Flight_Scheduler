import sys
import requests
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem


class FlightInfoApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Flight Information')
        self.setGeometry(100, 100, 600, 400)

        self.table = QTableWidget(self)
        self.table.setGeometry(50, 50, 500, 300)
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(['Flight Number', 'Destination', 'Time'])

        self.get_flight_information()

    def get_flight_information(self):
        url = "https://flight-info-api.p.rapidapi.com/schedules"

        querystring = {
            "DepartureAirport": "DAC",
            "ArrivalDateTime": "2023-11-21T12:00",
            "CodeType": "IATA",
            "version": "v2"
        }

        headers = {
            "X-RapidAPI-Key": "78310b8c57mshcf3285739dee2d8p1e00aajsn10f7a10af72f",
            "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            flight_data = response.json()

            # Populate the table with flight information
            if 'data' in flight_data and flight_data['data']:
                self.table.setRowCount(len(flight_data['data']))
                for row, flight in enumerate(flight_data['data']):
                    flight_number = QTableWidgetItem(flight['flightNumber'])
                    destination = QTableWidgetItem(flight['destination'])
                    time = QTableWidgetItem(flight['arrivalTime'])
                    self.table.setItem(row, 0, flight_number)
                    self.table.setItem(row, 1, destination)
                    self.table.setItem(row, 2, time)
            else:
                print("No flight information available for the specified criteria.")
        else:
            print("Failed to fetch flight information. Error:", response.text)


def main():
    app = QApplication(sys.argv)
    window = FlightInfoApp()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
