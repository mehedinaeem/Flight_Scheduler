import requests

url = "https://flight-info-api.p.rapidapi.com/status"

# Update the DepartureDateTime format
querystring = {
    "DepartureAirport": "DAC",
    "DepartureDateTime": "2023-11-20T12:00/2023-11-25T12:00",  # Update the format here
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
        print(flight_data)  # Display the entire response for inspection
    except ValueError as e:
        print("Error decoding JSON:", e)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")
    print(f"Error message: {response.text}")
