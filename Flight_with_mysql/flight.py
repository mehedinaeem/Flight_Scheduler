import requests
import mysql.connector
from datetime import datetime, timedelta

class Flight():
        # Function to insert data into the MySQL database
    def insert_data(flight_data):
        my_db = "flight_info"
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="naee2580",
                database=my_db
            )

            cursor = connection.cursor()

            for flight in flight_data:
                # Extract flight details
                flight_number = flight.get('flightNumber')
                departure_time = flight.get(
                    'departure', {}).get('time', {}).get('local')
                departure_date = flight.get(
                    'departure', {}).get('date', {}).get('local')
                arrival_place = flight.get('arrival', {}).get(
                    'airport', {}).get('iata')
                arrival_date = flight.get('arrival', {}).get(
                    'date', {}).get('local')
                arrival_time = flight.get('arrival', {}).get(
                    'time', {}).get('local')
                aircraft_type = flight.get('aircraftType', {}).get('iata')
                airline = flight.get('carrier', {}).get('iata')
                estimated_time = flight.get('elapsedTime')

                # Format departure_time to 'YYYY-MM-DD HH:MM:SS'
                departure_datetime_str = f"{departure_date} {departure_time}"
                departure_datetime = datetime.strptime(
                    departure_datetime_str, "%Y-%m-%d %H:%M")
                formatted_departure_time = departure_datetime.strftime(
                    "%Y-%m-%d %H:%M:%S")

                # Format arrival_time to 'YYYY-MM-DD HH:MM:SS'
                arrival_datetime_str = f"{arrival_date} {arrival_time}"
                arrival_datetime = datetime.strptime(
                    arrival_datetime_str, "%Y-%m-%d %H:%M")
                formatted_arrival_time = arrival_datetime.strftime(
                    "%Y-%m-%d %H:%M:%S")

                # SQL query to insert data into the database
                sql = "INSERT INTO flight (flight_number, departure_time, departure_date, arrival_place, arrival_date, arrival_time, aircraft_type, airline, estimated_time) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                values = (flight_number, formatted_departure_time, departure_date, arrival_place,
                        arrival_date, formatted_arrival_time, aircraft_type, airline, estimated_time)

                cursor.execute(sql, values)

            connection.commit()

        except Exception as e:
            print("Error inserting data into the database:", e)

        finally:
            if connection.is_connected():
                print("Successfully inserted")
                cursor.close()
                connection.close()

    # Get user input for airport name
    airport_name = input("Enter airport name (e.g., DAC): ")

    # Get user input for date
    date_str = input("Enter date (YYYY-MM-DD): ")

    # Set the start time as the current time
    current_time = datetime.now()
    start_time = current_time.strftime("%H:%M:%S")

    # Set the end time as 24:00:00
    end_time = "23:59:59"

    # Concatenate date and time for API request
    start_datetime_str = f"{date_str}T{start_time}"
    end_datetime_str = f"{date_str}T{end_time}"

    # Your API request code goes here
    url = "https://flight-info-api.p.rapidapi.com/status"
    querystring = {
        "DepartureAirport": airport_name,
        "DepartureDateTime": f"{start_datetime_str}/{end_datetime_str}",
        "CodeType": "IATA",
        "FlightType": "Scheduled",
        "version": "v2",
        "ServiceType": "Passenger"
    }

    headers = {
        "X-RapidAPI-Key": "f4776d460fmsh142cb1ff92d3e5ep1bed97jsnb16240ac25f8",
        "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Assuming flight_data is your list of flights
    if response.status_code == 200:
        try:
            flight_data = response.json().get('data', [])
            insert_data(flight_data)

            for flight in flight_data:
                # Print flight details as before
                flight_number = flight.get('flightNumber')
                departure_time = flight.get(
                    'departure', {}).get('time', {}).get('local')
                departure_date = flight.get(
                    'departure', {}).get('date', {}).get('local')
                arrival_place = flight.get('arrival', {}).get(
                    'airport', {}).get('iata')
                arrival_date = flight.get('arrival', {}).get(
                    'date', {}).get('local')
                arrival_time = flight.get('arrival', {}).get(
                    'time', {}).get('local')
                aircraft_type = flight.get('aircraftType', {}).get('iata')
                airline = flight.get('carrier', {}).get('iata')
                estimated_time = flight.get('elapsedTime')

                print(f"Flight Number: {flight_number}")
                print(f"Departure Time: {departure_time}")
                print(f"Departure Date: {departure_date}")
                print(f"Arrival Place: {arrival_place}")
                print(f"Arrival Date: {arrival_date}")
                print(f"Arrival Time: {arrival_time}")
                print(f"Aircraft Type: {aircraft_type}")
                print(f"Airline: {airline}")
                print(f"Estimated Time: {estimated_time} minutes")
                print("-------------------------------")

        except ValueError as e:
            print("Error decoding JSON:", e)
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        print(f"Error message: {response.text}")