# main.py
from flight import search_flight
from user import book_flight

def main():
    while True:
        print("1. Search Flight")
        print("2. Book a flight")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            airport_name = input("Enter airport name (e.g., DAC): ")
            date_str = input("Enter date (YYYY-MM-DD): ")
            search_flight(airport_name, date_str)

        elif choice == "2":
            book_flight()

        elif choice == "3":
            break

if __name__ == "__main__":
    main()
