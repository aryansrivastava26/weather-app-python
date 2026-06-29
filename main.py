import os
import requests
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read the API key from .env
API_KEY = os.getenv("API_KEY")

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print("\n------ Weather Report ------")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels Like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"].title())
    print("Wind Speed:", data["wind"]["speed"], "m/s")

else:
    print("❌ City not found or API key is invalid.")