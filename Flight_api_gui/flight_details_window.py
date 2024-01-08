# flight_details_window.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTextEdit


class FlightDetailsWindow(QWidget):
    def __init__(self, flight_details):
        super().__init__()
        self.flight_details = flight_details
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Flight Details")
        self.setGeometry(600, 300, 600, 400)

        layout = QVBoxLayout()

        self.text_flight_details = QTextEdit()
        self.text_flight_details.setReadOnly(True)
        layout.addWidget(self.text_flight_details)

        self.display_flight_details()

        self.setLayout(layout)

    def display_flight_details(self):
        flight_info = "\n".join([f"{key}: {value}" for key, value in self.flight_details.items()])
        self.text_flight_details.setPlainText(flight_info)
