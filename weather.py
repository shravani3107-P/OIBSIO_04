import requests

# Enter your API key here
API_KEY = "9574c8824e1e773f089d7c40170aa06c"

# Ask user for city name
city = input("Enter city name: ")

# API URL
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

# Get data
response = requests.get(url)
data = response.json()

# Check if city exists
if data["cod"] == 200:
    temp = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    condition = data["weather"][0]["description"]

    print("\nWeather Report")
    print("City:", city)
    print("Temperature:", temp, "°C")
    print("Humidity:", humidity, "%")
    print("Condition:", condition)

else:
    print("City not found. Please try again.")
