import requests

url = "https://flight-info-api.p.rapidapi.com/status"

querystring = {"DepartureAirport":"DAC","DepartureDateTime":"2023-11-20[T12:00]","CodeType":"IATA","FlightType":"Scheduled","version":"v2","ServiceType":"Passenger"}

headers = {
	"X-RapidAPI-Key": "78310b8c57mshcf3285739dee2d8p1e00aajsn10f7a10af72f",
	"X-RapidAPI-Host": "flight-info-api.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())