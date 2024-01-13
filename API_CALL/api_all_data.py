# Assuming 'flight_data' contains the provided flight data dictionary
flight_data = {
    'carrier': {'iata': 'BG', 'icao': 'BBC'},
    'serviceSuffix': '',
    'flightNumber': 339,
    'sequenceNumber': 1,
    'flightType': 'Scheduled',
    'departure': {
        'airport': {'iata': 'DAC', 'icao': 'VGHS'},
        'terminal': '2',
        'date': {'local': '2024-01-02', 'utc': '2024-01-01'},
        'time': {'local': '01:30', 'utc': '19:30'}
    },
    'arrival': {
        'airport': {'iata': 'RUH', 'icao': 'OERK'},
        'terminal': '1',
        'date': {'local': '2024-01-02', 'utc': '2024-01-02'},
        'time': {'local': '05:10', 'utc': '02:10'}
    },
    'elapsedTime': 400,
    'aircraftType': {'iata': '773'},
    'serviceType': {'iata': 'J'},
    'segmentInfo': {
        'numberOfStops': 0,
        'intermediateAirports': {'iata': []}
    },
    'codeshare': {
        'jointOperationAirlineDesignators': [],
        'marketingFlights': []
    },
    'scheduleInstanceKey': '8147915c0a32173b8bd6cc7a33a33cc590c7623e23ddcb3706fcab503c54d53a',
    'statusKey': 'c1ddf0b876899d1804bfc7f50fc578303311c88d49dd65d210edea2feab38eba',
    'statusDetails': [
        {
            'state': 'Landed',
            'updatedAt': '2024-01-02T02:07:46.237',
            'equipment': {
                'aircraftRegistrationNumber': 'S2AFP',
                'actualAircraftType': {'iata': '77W', 'icao': 'B77W'}
            },
            'departure': {
                'actualTime': {'offGround': {'local': '2024-01-02T01:43:00+06:00', 'utc': '2024-01-01T19:43:00+00:00'}},
                'airport': {'iata': 'DAC', 'icao': 'VGHS'}
            },
            'arrival': {
                'actualTime': {'onGround': {'local': '2024-01-02T05:06:00+03:00', 'utc': '2024-01-02T02:06:00+00:00'}},
                'airport': {'iata': 'RUH', 'icao': 'OERK'}
            }
        }
    ]
}

# Extracting the 'statusDetails' field
status_details = flight_data.get('statusDetails', [])

# Check if there are status details available
if status_details:
    for status in status_details:
        # Get scheduled and actual departure times
        scheduled_departure = flight_data['departure']['time']['utc']
        actual_departure = status['departure']['actualTime']['offGround']['utc']

        # Get scheduled and actual arrival times
        scheduled_arrival = flight_data['arrival']['time']['utc']
        actual_arrival = status['arrival']['actualTime']['onGround']['utc']

        # Compare scheduled and actual times for departure and arrival
        if scheduled_departure != actual_departure:
            print("Flight departure is delayed!")
            print("Scheduled Departure:", scheduled_departure)
            print("Actual Departure:", actual_departure)

        if scheduled_arrival != actual_arrival:
            print("Flight arrival is delayed!")
            print("Scheduled Arrival:", scheduled_arrival)
            print("Actual Arrival:", actual_arrival)

        if scheduled_departure == actual_departure and scheduled_arrival == actual_arrival:
            print("The flight is on time.")
else:
    print("No status details available for this flight.")
