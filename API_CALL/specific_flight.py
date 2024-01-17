import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton
import requests

class FlightInfoApp(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Flight Information App')
        self.setGeometry(100, 100, 800, 600)

        self.create_widgets()
        self.setup_layout()

    def create_widgets(self):
        self.flight_label = QLabel('Enter Flight Code:')
        self.flight_code_input = QTextEdit()
        self.search_button = QPushButton('Search')
        self.result_label = QLabel('')
        self.result_text = QTextEdit()

        self.search_button.clicked.connect(self.search_flight)

    def setup_layout(self):
        layout = QVBoxLayout()
        layout.addWidget(self.flight_label)
        layout.addWidget(self.flight_code_input)
        layout.addWidget(self.search_button)
        layout.addWidget(self.result_label)
        layout.addWidget(self.result_text)

        self.setLayout(layout)

    def search_flight(self):
        flight_code = self.flight_code_input.toPlainText().strip().upper()

        if not flight_code:
            self.result_label.setText('Please enter a valid flight code.')
            return

        url = "https://flight-info-api.p.rapidapi.com/status"
        querystring = {
            "DepartureAirport": "DAC",
            "DepartureDateTime": "2023-11-20T12:00/2023-11-25T12:00",
            "CodeType": "IATA",
            "FlightType": "Scheduled",
            "version": "v2",
            "ServiceType": "Passenger"
        }

        headers = {
            "X-RapidAPI-Key": "78310b8c57mshcf3285739dee2d8p1e00aajsn10f7a10af72f",
            "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)

        if response.status_code == 200:
            try:
                flight_data = response.json()

                if 'Flights' in flight_data:
                    matching_flights = [flight for flight in flight_data['Flights'] if flight['Flight']['Code'] == flight_code]

                    if matching_flights:
                        self.result_label.setText(f"Flight {flight_code} Details:")
                        self.result_text.setPlainText(str(matching_flights))
                    else:
                        self.result_label.setText(f"No data found for flight {flight_code}.")
                        self.result_text.clear()
                else:
                    self.result_label.setText("Invalid data format received from the API.")
            except ValueError as e:
                self.result_label.setText("Error decoding JSON: " + str(e))
        else:
            self.result_label.setText(f"Failed to retrieve data. Status code: {response.status_code}")
            self.result_text.setPlainText(f"Error message: {response.text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FlightInfoApp()
    ex.show()
    sys.exit(app.exec_())
