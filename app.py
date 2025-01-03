from flask import Flask, render_template, jsonify, request
from geopy.geocoders import Nominatim
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from flask import send_from_directory
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variable
api_key = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

# Function to fetch location from city name
def fetch_location(city):
    geolocator = Nominatim(user_agent="geoapiExercise")
    return geolocator.geocode(city)

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    return requests.get(api).json()

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/')
def index():
    return render_template('index.html')

# Route to fetch weather information
@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city', '')

    if not city:
        return jsonify({"error": "City name is required"}), 400

    location = fetch_location(city)

    if not location:
        return jsonify({"error": "City not found"}), 404

    # Get timezone info
    obj = TimezoneFinder()
    result = obj.timezone_at(lng=location.longitude, lat=location.latitude)
    home = pytz.timezone(result)
    local_time = datetime.now(home)
    current_time = local_time.strftime("%I:%M %p")

    # Fetch weather data from OpenWeatherMap
    json_data = fetch_weather_data(city, api_key)

    if json_data.get("cod") != 200:
        return jsonify({"error": "Error fetching weather data"}), 500

    condition = json_data['weather'][0]['main']
    description = json_data['weather'][0]['description']
    icon = json_data['weather'][0]['icon']
    temp = int(json_data['main']['temp'])
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    # Extract min/max temperatures with a fallback to 'temp' if values are missing or identical
    min_temp = json_data['main'].get('temp_min', temp)
    max_temp = json_data['main'].get('temp_max', temp)

    # Ensure min_temp and max_temp are distinct
    if min_temp == max_temp:
        min_temp = temp - 1  # Adjust min_temp slightly lower
        max_temp = temp + 1  # Adjust max_temp slightly higher

    data = {
        "city": city,
        "current_time": current_time,
        "condition": condition,
        "description": description,
        "temperature": temp,
        "min_temp": int(min_temp),
        "max_temp": int(max_temp),
        "pressure": pressure,
        "humidity": humidity,
        "wind_speed": wind,
        "icon": icon
    }

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)