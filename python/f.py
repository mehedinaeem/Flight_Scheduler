import requests

url = "https://flight-info-api.p.rapidapi.com/status"

querystring = {
    "DepartureAirport": "DAC",
    "DepartureDateTime": "2023-11-20T12:00/2023-11-22T12:00",
    # "DepartureDateTime": "2023-11-20[T12:00]",
    "CodeType": "IATA",
    # "FlightType": "Scheduled",
    "version": "v2",
    # "ServiceType": "Passenger"
}

headers = {
    "X-RapidAPI-Key": "78310b8c57mshcf3285739dee2d8p1e00aajsn10f7a10af72f",
    "X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

if response.status_code == 200:
    try:
        flight_data = response.json()
        flights = flight_data.get('data', [])

        for flight in flights:
            flight_number = flight.get('flightNumber')
            departure_airport = flight.get('departure', {}).get('airport', {}).get('iata')
            departure_date = flight.get('departure', {}).get('date', {}).get('local')
            arrival_place = flight.get('arrival', {}).get('airport', {}).get('iata')
            arrival_date = flight.get('arrival', {}).get('date', {}).get('local')
            arrival_time = flight.get('arrival', {}).get('time', {}).get('local')
            flight_type = flight.get('flightType')

            print(f"Flight Number: {flight_number}")
            print(f"Departure Airport: {departure_airport}")
            print(f"Departure Date: {departure_date}")
            print(f"Arrival Place: {arrival_place}")
            print(f"Arrival Date: {arrival_date}")
            print(f"Arrival Time: {arrival_time}")
            print(f"Flight Type: {flight_type}")
            print("-------------------------------")

    except ValueError as e:
        print("Error decoding JSON:", e)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(f"Error message: {response.text}")
