# flight.py
import requests
from datetime import datetime

def search_flight(departure_airport, date_str, destination_airport=None):
    current_time = datetime.now()
    start_time = current_time.strftime("%H:%M:%S")
    end_time = "23:59:59"

    start_datetime_str = f"{date_str}T{start_time}"
    end_datetime_str = f"{date_str}T{end_time}"

    url = "https://flight-info-api.p.rapidapi.com/status"
    querystring = {
        "DepartureAirport": departure_airport,
        "DepartureDateTime": f"{start_datetime_str}/{end_datetime_str}",
        "CodeType": "IATA",
        "FlightType": "Scheduled",
        "version": "v2",
        "ServiceType": "Passenger"
    }

    # Include destination_airport in the querystring if provided
    if destination_airport:
        querystring["ArrivalAirport"] = destination_airport

    headers = {
        # "X-RapidAPI-Key": "78310b8c57mshcf3285739dee2d8p1e00aajsn10f7a10af72f",
        # "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
        
        'X-RapidAPI-Key': 'caef7ec3d5mshdc125174597db07p13a68djsn7b31cb74238b',
    'X-RapidAPI-Host': 'flight-info-api.p.rapidapi.com'
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        try:
            flight_info = ""
            flight_data = response.json().get('data', [])

            if not flight_data:
                return "No flights available for the specified route."

            for flight in flight_data:
                # Print flight details as before
                flight_number = flight.get('flightNumber')
                departure_time = flight.get('departure', {}).get('time', {}).get('local')
                departure_date = flight.get('departure', {}).get('date', {}).get('local')
                arrival_place = flight.get('arrival', {}).get('airport', {}).get('iata')
                arrival_date = flight.get('arrival', {}).get('date', {}).get('local')
                arrival_time = flight.get('arrival', {}).get('time', {}).get('local')
                aircraft_type = flight.get('aircraftType', {}).get('iata')
                airline = flight.get('carrier', {}).get('iata')
                estimated_time = flight.get('elapsedTime')

                flight_info += f"Flight Number: {flight_number}\n"
                flight_info += f"Departure Time: {departure_time}\n"
                flight_info += f"Departure Date: {departure_date}\n"
                flight_info += f"Arrival Place: {arrival_place}\n"
                flight_info += f"Arrival Date: {arrival_date}\n"
                flight_info += f"Arrival Time: {arrival_time}\n"
                flight_info += f"Aircraft Type: {aircraft_type}\n"
                flight_info += f"Airline: {airline}\n"
                flight_info += f"Estimated Time: {estimated_time} minutes\n"

                # Extracting the 'statusDetails' field
                status_details = flight.get('statusDetails', [])

                # Check if there are status details available
                if status_details:
                    for status in status_details:
                        # Get scheduled and actual departure times
                        scheduled_departure = flight['departure']['time']['utc']

                        # Use get method to handle potential missing keys
                        actual_time_info = status.get('departure', {}).get('actualTime', {}).get('offGround', {})
                        actual_departure = actual_time_info.get('utc', 'Not available')

                        # Compare scheduled and actual times for departure
                        if scheduled_departure != actual_departure:
                            flight_info += f"Delayed!\n"
                            # flight_info += f"Scheduled Departure: {scheduled_departure}\n"
                            # flight_info += f"Actual Departure: {actual_departure}\n"
                        else:
                            flight_info += "The flight is on time.\n"
                else:
                    flight_info += "No status details available for this flight.\n"

                flight_info += "-------------------------------\n"

            return flight_info

        except ValueError as e:
            return f"Error decoding JSON: {e}"
    else:
        return f"Failed to retrieve data. Status code: {response.status_code}\nError message: {response.text}"
