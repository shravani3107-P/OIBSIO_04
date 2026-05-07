# Weather App in Python

## Description

This is a simple command-line Weather App built using Python.
It fetches live weather data for a user-specified city using the OpenWeatherMap API and displays:

* Temperature
* Humidity
* Weather condition

The app uses the `requests` library to connect to the weather API.

---

## Features

* User enters any city name
* Fetches live weather details
* Displays temperature in Celsius
* Shows humidity percentage
* Displays weather condition
* Handles invalid city names

---

## Requirements

Before running the program, install Python and the required library.

### Install requests library

Open Command Prompt and run:

```bash
pip install requests
```

---

## How to Get API Key

1. Go to [OpenWeatherMap](https://openweathermap.org/api?utm_source=chatgpt.com)
2. Create a free account
3. Generate your API key
4. Copy the API key
5. Replace:

```python
API_KEY = "YOUR_API_KEY"
```

with your actual API key.

---

## How to Run

1. Open Python IDLE
2. Create a new file
3. Paste the Python code
4. Save as:

```bash
weather.py
```

5. Press **F5** to run

---

## Example Output

```yaml
Enter city name: Mumbai

Weather Report
City: Mumbai
Temperature: 30°C
Humidity: 75%
Condition: clear sky
```

---

## Technologies Used

* Python
* Requests Library
* OpenWeatherMap API

---

## Note

* Internet connection is required
* A valid API key is required

---

## Author

Created as a simple Python weather application project.
