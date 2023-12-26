import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout, QFormLayout, QSpacerItem, QSizePolicy
from flight import search_flight
from user import book_flight
from PyQt5.QtCore import Qt  # Import Qt module for alignment flags

class FlightScheduler(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Flight Scheduler")
        self.setFixedSize(800, 600)  # Set the fixed size of the window

        main_layout = QHBoxLayout()

        left_layout = QFormLayout()
        right_layout = QVBoxLayout()

        self.label_airport = QLabel("Enter airport name (e.g., DAC): ")
        self.input_airport = QLineEdit()
        self.input_airport.setFixedSize(200, 30)

        # Adjusting the horizontal spacing between the label and input box
        left_layout.setFormAlignment(Qt.AlignTop)  # Align to the top
        left_layout.setLabelAlignment(Qt.AlignRight)  # Align labels to the right

        left_layout.addRow(self.label_airport, self.input_airport)

        self.label_date = QLabel("Enter date (YYYY-MM-DD): ")
        self.input_date = QLineEdit()
        self.input_date.setFixedSize(200, 30)

        left_layout.addRow(self.label_date, self.input_date)

        self.button_search = QPushButton("Search Flight")
        self.button_search.setFixedSize(200, 30)
        self.button_search.clicked.connect(self.search_flight_clicked)
        
        left_layout.addWidget(self.button_search)

        self.label_flight_info = QLabel("Flight Information:")
        right_layout.addWidget(self.label_flight_info)

        self.text_flight_info = QTextEdit()
        right_layout.addWidget(self.text_flight_info)

        self.button_book = QPushButton("Book a Flight")
        self.button_book.setFixedSize(200, 30)
        self.button_book.clicked.connect(self.book_flight_clicked)
        right_layout.addWidget(self.button_book)

        main_layout.addLayout(left_layout)
        main_layout.addLayout(right_layout)

        self.setLayout(main_layout)

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
