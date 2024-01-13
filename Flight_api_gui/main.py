import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QFormLayout
from PyQt5.QtGui import QIcon, QTextCharFormat
from PyQt5.QtCore import Qt
from flight import search_flight
from user import book_flight

class FlightScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Flight Scheduler")
        self.setGeometry(600, 300, 800, 500)
        self.setWindowIcon(QIcon('D:/Flight_Scheduler/Flight_api_gui/asset/plane.png'))

        main_layout = QHBoxLayout()

        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(self.backgroundRole(), Qt.gray)
        self.setPalette(palette)

        left_layout = QFormLayout()
        right_layout = QVBoxLayout()

        self.label_airport = QLabel("Enter airport name (e.g., DAC): ")
        self.input_airport = QLineEdit()
        self.input_airport.setStyleSheet("background-color:#9EAE9D; color:black;font-size:25px")
        self.input_airport.setFixedSize(200, 30)
        left_layout.setFormAlignment(Qt.AlignTop)
        left_layout.setLabelAlignment(Qt.AlignRight)
        left_layout.addRow(self.label_airport, self.input_airport)

        self.label_date = QLabel("Enter date (YYYY-MM-DD): ")
        self.input_date = QLineEdit()
        self.input_date.setFixedSize(200, 30)
        self.input_date.setStyleSheet("background-color:#9EAE9D; color:black;font-size:25px")
        left_layout.addRow(self.label_date, self.input_date)

        self.button_search = QPushButton("Search Flight")
        self.button_search.setStyleSheet("background-color:#A447D7; color:black;font-size:20px")
        self.button_search.setFixedSize(150, 40)
        self.button_search.clicked.connect(self.search_flight_clicked)
        left_layout.addWidget(self.button_search)

        self.label_flight_info = QLabel("<b>Flight Information:</b>")
        self.label_flight_info.setStyleSheet("font-size:30px")
        right_layout.addWidget(self.label_flight_info)

        self.text_flight_info = QTextEdit()
        self.text_flight_info.setReadOnly(True)
        right_layout.addWidget(self.text_flight_info)

        self.button_book = QPushButton("Get flight Update")
        self.button_book.setFixedSize(200, 30)
        self.button_book.setStyleSheet("background-color:#A447D7; color:black;font-size:20px")
        self.button_book.clicked.connect(self.book_flight_clicked)
        right_layout.addWidget(self.button_book)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

    def search_flight_clicked(self):
        airport_name = self.input_airport.text()
        date_str = self.input_date.text()

        flight_info = search_flight(airport_name, date_str)
        self.display_flight_info(flight_info)

    def display_flight_info(self, flight_info):
        self.text_flight_info.clear()

        flight_list = flight_info.split("-------------------------------\n")
        for i, flight in enumerate(flight_list):
            format = QTextCharFormat()
            if i % 2 == 0:
                format.setBackground(Qt.red)
            else:
                format.setBackground(Qt.green)

            # Customize the formatting for each flight detail
            formatted_text = ""
            details = flight.strip().split("\n")
            for detail in details:
                if ":" in detail:
                    key, value = detail.split(":", 1)
                    formatted_text += f"<b>{key}:</b> {value.strip()}<br>"
                else:
                    formatted_text += f"{detail.strip()}<br>"

            formatted_text = f"<span style='background-color:{format.background().color().name()}; font-size:18px;'>{formatted_text}</span><br>"
            self.text_flight_info.insertHtml(formatted_text)

    def book_flight_clicked(self):
        flight_number, ok = QInputDialog.getText(self, "Flight Number", "Enter your flight number:")
        if ok:
            name, ok = QInputDialog.getText(self, "Name", "Enter your name:")
            if ok:
                phone, ok = QInputDialog.getText(self, "Phone Number", "Enter your phone number:")
                if ok:
                    email, ok = QInputDialog.getText(self, "Email", "Enter your email:")
                    if ok:
                        book_flight(flight_number, name, phone, email)
                        self.text_flight_info.setPlainText("Flight booked successfully!")

def main():
    app = QApplication(sys.argv)
    scheduler = FlightScheduler()
    scheduler.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
