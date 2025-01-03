from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim
from tkinter import messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Retrieve the API key from environment variable
api_key = os.getenv("WEATHER_API_KEY")

root = Tk()
root.title("Weather APP")
root.geometry("900x500+300+200")
root.resizable(False, False)

# Function to fetch location from city name
def fetch_location(city):
    geolocator = Nominatim(user_agent="geoapiExercise")
    return geolocator.geocode(city)

# Function to fetch weather data from OpenWeatherMap API
def fetch_weather_data(city, api_key):
    api = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    return requests.get(api).json()

# Function to update the UI with weather data
def update_weather_ui(json_data, wind, humidity, description, pressure, temp, condition):
    t.config(text=f"{temp}°C")
    c.config(text=f"{condition} | Feels like {temp}°C")
    w.config(text=f"{wind} km/h")
    h.config(text=f"{humidity}%")
    d.config(text=f"{description}")
    p.config(text=f"{pressure} hPa")

# Main function to get the weather information
def getWeather():
    try:
        city = textfield.get().strip()

        if not city:
            messagebox.showerror("Error", "City name cannot be empty!")
            return

        # Fetch location details based on city
        location = fetch_location(city)

        if not location:
            messagebox.showerror("Error", "City not found!")
            return

        # Get the timezone of the location
        obj = TimezoneFinder()
        result = obj.timezone_at(lng=location.longitude, lat=location.latitude)

        # Get local time in the specified timezone
        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        # Fetch weather data from the API
        json_data = fetch_weather_data(city, api_key)

        if json_data.get("cod") != 200:
            error_message = json_data.get("message", "Unknown error occurred")
            messagebox.showerror("Error", f"City not found or API error: {error_message}")
            return

        # Extract data from the API response
        condition = json_data['weather'][0]['main']
        description = json_data['weather'][0]['description']
        temp = int(json_data['main']['temp'] - 273.15)
        pressure = json_data['main']['pressure']
        humidity = json_data['main']['humidity']
        wind = json_data['wind']['speed']

        # Update the UI with extracted data
        update_weather_ui(json_data, wind, humidity, description, pressure, temp, condition)

    except requests.exceptions.RequestException as req_error:
        messagebox.showerror("Error", f"Network error: {req_error}")
    except KeyError as key_error:
        messagebox.showerror("Error", f"Unexpected response format: {key_error}")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

# Search Box
Search_image = PhotoImage(file="static/images/search.png")
myimage = Label(image=Search_image)
myimage.place(x=20, y=20)

textfield = tk.Entry(root, justify="center", width=17, font=("poppins", 25, "bold"), bg="#404040", border=0, fg="white")
textfield.place(x=50, y=40)
textfield.focus()

Search_icon = PhotoImage(file="static/images/search_icon.png")
myimage_icon = Button(image=Search_icon, borderwidth=0, cursor="hand2", bg="#404040", command=getWeather)
myimage_icon.place(x=400, y=34)

# Logo
Logo_image = PhotoImage(file="static/images/logo.png")
logo = Label(image=Logo_image)
logo.place(x=150, y=100)

# Bottom Box
Frame_image = PhotoImage(file="static/images/box.png")
frame_myimage = Label(image=Frame_image)
frame_myimage.pack(padx=5, pady=5, side=BOTTOM)

# Time
name = Label(root, font=("arial", 15, "bold"))
name.place(x=30, y=100)
clock = Label(root, font=("Helvetica", 20))
clock.place(x=30, y=130)

# Labels for weather information
label1 = Label(root, text="WIND", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label1.place(x=120, y=400)

label2 = Label(root, text="HUMIDITY", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label2.place(x=250, y=400)

label_desc = Label(root, text="DESCRIPTION", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_desc.place(x=430, y=400)

label_pressure = Label(root, text="PRESSURE", font=("Helvetica", 15, "bold"), fg="white", bg="#1ab5ef")
label_pressure.place(x=650, y=400)

# Labels for weather data
t = Label(font=("arial", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("arial", 15, "bold"))
c.place(x=400, y=250)

w = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
w.place(x=120, y=430)
h = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
h.place(x=280, y=430)
d = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
d.place(x=450, y=430)
p = Label(text="...", font=("arial", 20, "bold"), bg="#1ab5ef")
p.place(x=670, y=430)

root.mainloop()