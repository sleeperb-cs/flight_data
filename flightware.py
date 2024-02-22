import requests
import datetime
import dateutil.parser

# Replace with your actual API key
api_key = "YOUR_API_KEY"

# Get the current date
today = datetime.date.today()

# Get the first and last days of November
first_day = datetime.date(today.year, 11, 1)
last_day = datetime.date(today.year, 11, 30)

# Set the origin and destination airports
origin = "ASU"
destination = "EWR"

# Construct the FlightAware API URL
url = f"https://aeroapi.flightaware.com/aeroapi/flights/scheduled?origin={origin}&destination={destination}&start={first_day}&end={last_day}&api_key={api_key}"

# Make the API request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()

    # Iterate through the flights
    for flight in data["scheduled_flights"]:
        # Get the flight details
        flight_number = flight["ident"]
        airline = flight["operator"]
        departure_time = dateutil.parser.parse(flight["departuretime"])
        arrival_time = dateutil.parser.parse(flight["arrivaltime"])

        # Print the flight details
        print(f"Flight: {flight_number}")
        print(f"Airline: {airline}")
        print(f"Departure time: {departure_time}")
        print(f"Arrival time: {arrival_time}")
        print("-" * 20)

else:
    # Print an error message
    print("Failed to retrieve flight data. Status code:", response.status_code)
                  