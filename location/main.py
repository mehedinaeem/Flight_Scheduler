import requests

def get_location_by_phone_number(phone_number, api_key):
    base_url = "https://maps.googleapis.com/maps/api/geocode/json"
    
    params = {
        'address': phone_number,
        'key': api_key,
    }

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if data['status'] == 'OK':
            # Extracting latitude and longitude from the result
            location = data['results'][0]['geometry']['location']
            latitude = location['lat']
            longitude = location['lng']
            
            return latitude, longitude
        else:
            print(f"Error: {data['status']}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage
phone_number = "+8801943806813"
api_key = "AIzaSyAEJ7sycPSbvVmV-d4CbYj7-B-uaLyem2o"

location = get_location_by_phone_number(phone_number, api_key)

if location:
    print(f"Latitude: {location[0]}, Longitude: {location[1]}")
else:
    print("Unable to retrieve location.")
