import requests
import json

# Set the API key
API_KEY = "YOUR_API_KEY"

# Set the departure and arrival airports
departure_airport = "ASU"
arrival_airport = "EWR"

# Set the month and year
month = 11
year = 2023

# Get the flight information
url = "https://api.flightstats.com/flex/flights/v1/json/flights/list?departureAirport={departure_airport}&arrivalAirport={arrival_airport}&month={month}&year={year}&apiKey={API_KEY}".format(
    departure_airport=departure_airport,
    arrival_airport=arrival_airport,
    month=month,
    year=year,
    API_KEY=API_KEY,
)

response = requests.get(url)

# Check the response status code
if response.status_code == 200:
    # The request was successful
    flights = json.loads(response.content)

    # Print the flight information
    for flight in flights:
        print(flight["flightNumber"], flight["departureAirport"], flight["arrivalAirport"], flight["departureDate"], flight["arrivalDate"])

else:
    # The request failed
    print("Request failed with status code:", response.status_code)
                  