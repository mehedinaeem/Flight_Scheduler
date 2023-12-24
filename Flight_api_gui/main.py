import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog
from flight import search_flight
from user import book_flight

class FlightScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Flight Scheduler")

        layout = QVBoxLayout()

        self.label_airport = QLabel("Enter airport name (e.g., DAC): ")
        self.input_airport = QLineEdit()
        layout.addWidget(self.label_airport)
        layout.addWidget(self.input_airport)

        self.label_date = QLabel("Enter date (YYYY-MM-DD): ")
        self.input_date = QLineEdit()
        layout.addWidget(self.label_date)
        layout.addWidget(self.input_date)

        self.button_search = QPushButton("Search Flight")
        self.button_search.clicked.connect(self.search_flight_clicked)
        layout.addWidget(self.button_search)

        self.label_flight_info = QLabel("Flight Information:")
        layout.addWidget(self.label_flight_info)

        self.text_flight_info = QTextEdit()
        layout.addWidget(self.text_flight_info)

        self.button_book = QPushButton("Book a Flight")
        self.button_book.clicked.connect(self.book_flight_clicked)
        layout.addWidget(self.button_book)

        self.setLayout(layout)

    def search_flight_clicked(self):
        airport_name = self.input_airport.text()
        date_str = self.input_date.text()

        flight_info = search_flight(airport_name, date_str)
        self.text_flight_info.setPlainText(flight_info)

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
