# data.py

# Import necessary libraries for making API requests, assuming using requests library
import requests

def get_flight_details_by_number(flight_number):
    # Replace this URL and API call with your actual API endpoint
    url = f"https://your-api-url.com/flights/{flight_number}"

    # Make a GET request to fetch flight details
    try:
        response = requests.get(url)
        if response.status_code == 200:
            # Process the response and extract flight details
            flight_info = response.json()
            return flight_info
        else:
            print(f"Failed to fetch flight details. Status code: {response.status_code}")
            return None
    except requests.RequestException as e:
        print(f"Request exception: {e}")
        return None
