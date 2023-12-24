# flight.py
import requests
from datetime import datetime


def search_flight(airport_name, date_str):
    current_time = datetime.now()
    start_time = current_time.strftime("%H:%M:%S")
    end_time = "23:59:59"

    start_datetime_str = f"{date_str}T{start_time}"
    end_datetime_str = f"{date_str}T{end_time}"

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
        # "X-RapidAPI-Key": "f4776d460fmsh142cb1ff92d3e5ep1bed97jsnb16240ac25f8",
        # "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"

        # its from naeem_22102024@jkkniu.edu.bd
        "X-RapidAPI-Key": "4cb961a223msh26181b7f2f5b205p1da763jsn1a17a4430b25",
        "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        try:
            flight_info = ""

            flight_data = response.json().get('data', [])
            for flight in flight_data:
                # Extract flight details as needed
                flight_number = flight.get('flightNumber')
                departure_time = flight.get(
                    'departure', {}).get('time', {}).get('local')
                # Add more flight details as required

                # Concatenate flight information
                flight_info += f"Flight Number: {flight_number}\n"
                flight_info += f"Departure Time: {departure_time}\n"
                # Append more flight details

                flight_info += "-------------------------------\n"

            return flight_info

        except ValueError as e:
            return f"Error decoding JSON: {e}"
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}\nError message: {response.text}"
