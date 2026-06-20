import customtkinter as ctk
import requests
import json
from PIL import Image
import os
import sys
from datetime import datetime, timedelta

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

root = ctk.CTk()
root.title("Weather App")
root.attributes("-fullscreen", True)

tomorrow_date = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
tomorrows_temps = []

overmorrow_date = (datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d')
overmorrow_temps = []

day_3_date = (datetime.now() + timedelta(days=3)).strftime('%Y-%m-%d')
day_3_temps = []

day_4_date = (datetime.now() + timedelta(days=4)).strftime('%Y-%m-%d')
day_4_temps = []

day_5_date = (datetime.now() + timedelta(days=5)).strftime('%Y-%m-%d')
day_5_temps = []

bg_image = ctk.CTkImage(Image.open(resource_path("QuestionMark.png")), size=(1440, 900))
background_label = ctk.CTkLabel(root, image=bg_image, text="")
background_label.place(relx=0.5, rely=0.5, anchor="center")

place = ctk.CTkEntry(root, placeholder_text="Enter ZIP Code")
place.place(relx=0.44, rely=0.16, anchor="center")

place_label = ctk.CTkLabel(root, text="--", font=("Arial", 60, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
place_label.place(relx=0.5, rely=0.1, anchor="center")

temp_label = ctk.CTkLabel(root, text="--°F", font=("Arial", 50, "bold"), fg_color="#0b0fe6", corner_radius=10, width=00, height=40)
temp_label.place(relx=0.5, rely=0.22, anchor="center")

desc_label = ctk.CTkLabel(root, text="--", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=400, height=80)
desc_label.place(relx=0.5, rely=0.38, anchor="center")

humidity_label = ctk.CTkLabel(root, text="--% Humidity", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
humidity_label.place(relx=0.5, rely=0.53, anchor="center")

feels_like_label = ctk.CTkLabel(root, text="Feels Like: --°F", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
feels_like_label.place(relx=0.5, rely=0.29, anchor="center")

wind_label = ctk.CTkLabel(root, text="Wind: -- mph, --", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
wind_label.place(relx=0.5, rely=0.46, anchor="center")

tomorrow_label = ctk.CTkLabel(root, text="Tomorrow:\nHigh: --°F\nLow: --°F", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
tomorrow_label.place(relx=0.18, rely=0.75, anchor="center")

overmorrow_label = ctk.CTkLabel(root, text=f"{overmorrow_date}:\nHigh: --°F\nLow: --°F", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
overmorrow_label.place(relx=0.34, rely=0.75, anchor="center")

day_3_label = ctk.CTkLabel(root, text=f"{day_3_date}:\nHigh: --°F\nLow: --°F", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
day_3_label.place(relx=0.5, rely=0.75, anchor="center")

day_4_label = ctk.CTkLabel(root, text=f"{day_4_date}:\nHigh: --°F\nLow: --°F", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
day_4_label.place(relx=0.66, rely=0.75, anchor="center")

day_5_label = ctk.CTkLabel(root, text=f"{day_5_date}:\nHigh: --°F\nLow: --°F", font=("Arial", 30, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
day_5_label.place(relx=0.82, rely=0.75, anchor="center")

forecast_label = ctk.CTkLabel(root, text="5-Day Forecast", font=("Arial", 60, "bold"), fg_color="#0b0fe6", corner_radius=10, width=200, height=40)
forecast_label.place(relx=0.5, rely=0.62, anchor="center")

def update_weather(place, bg_image, background_label):
    api_key = "7d881d0dd55534343543f7732651bb01"

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?zip={place.get()}&appid={api_key}&units=imperial"
    forecast_url = f"http://api.openweathermap.org/data/2.5/forecast?zip={place.get()}&appid={api_key}&units=imperial"
    weather_response = requests.get(weather_url)
    forecast_response = requests.get(forecast_url)
    weather_data = weather_response.json()
    forecast_data = forecast_response.json()

    for chunk in forecast_data["list"]:
        if tomorrow_date in chunk["dt_txt"]:
            temp = chunk["main"]["temp"]
            tomorrows_temps.append(temp)

        if overmorrow_date in chunk["dt_txt"]:
            temp = chunk["main"]["temp"]
            overmorrow_temps.append(temp)

        if day_3_date in chunk["dt_txt"]:
            temp = chunk["main"]["temp"]
            day_3_temps.append(temp)

        if day_4_date in chunk["dt_txt"]:
            temp = chunk["main"]["temp"]
            day_4_temps.append(temp)

        if day_5_date in chunk["dt_txt"]:
            temp = chunk["main"]["temp"]
            day_5_temps.append(temp)

    tomorrow_high_temp = max(tomorrows_temps)
    tomorrow_low_temp = min(tomorrows_temps)

    overmorrow_high_temp = max(overmorrow_temps)
    overmorrow_low_temp = min(overmorrow_temps)

    day_3_high_temp = max(day_3_temps)
    day_3_low_temp = min(day_3_temps)

    day_4_high_temp = max(day_4_temps)
    day_4_low_temp = min(day_4_temps)

    day_5_high_temp = max(day_5_temps)
    day_5_low_temp = min(day_5_temps)

    temp = weather_data["main"]["temp"]
    desc = weather_data["weather"][0]["description"].title()
    humidity = weather_data["main"]["humidity"]
    name = weather_data["name"]
    feels_like = weather_data["main"]["feels_like"]
    wind_speed = weather_data["wind"]["speed"]
    wind_direction = weather_data["wind"]["deg"]

    def get_wind_direction(wind_direction):
        directions = ["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE", 
                    "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
        
        index = int((wind_direction + 11.25) / 22.5)
        return directions[index % 16]

    temp_label.configure(text=f"{temp}°F")
    desc_label.configure(text=desc)
    place_label.configure(text=name)
    humidity_label.configure(text=f"{humidity}% Humidity")
    feels_like_label.configure(text=f"Feels Like: {feels_like}°F")
    wind_label.configure(text=f"Wind: {wind_speed} mph, {get_wind_direction(wind_direction)}")

    tomorrow_label.configure(text=f"Tomorrow:\nHigh: {tomorrow_high_temp}°F\nLow: {tomorrow_low_temp}°F")
    overmorrow_label.configure(text=f"{overmorrow_date}:\nHigh: {overmorrow_high_temp}°F\nLow: {overmorrow_low_temp}°F")
    day_3_label.configure(text=f"{day_3_date}:\nHigh: {day_3_high_temp}°F\nLow: {day_3_low_temp}°F")
    day_4_label.configure(text=f"{day_4_date}:\nHigh: {day_4_high_temp}°F\nLow: {day_4_low_temp}°F")
    day_5_label.configure(text=f"{day_5_date}:\nHigh: {day_5_high_temp}°F\nLow: {day_5_low_temp}°F")
    snow = ["Snow", "Sleet"]
    atmosphere = ["Mist", "Smoke", "Haze", "Fog", "Sand", "Dust", "Volcanic Ash", "Squalls", "Tornado"]
    rain = ["Drizzle", "Shower", "Rain"]

    if "--" in desc:
        bg_image = ctk.CTkImage(Image.open(resource_path("QuestionMark.png")), size=(1440, 900))
        background_label.configure(image=bg_image)

    if "Clear" in desc:
        bg_image = ctk.CTkImage(Image.open(resource_path("Clear.jpg")), size=(1440, 900))
        background_label.configure(image=bg_image)
    
    if "Clouds" in desc:
        bg_image = ctk.CTkImage(Image.open(resource_path("Cloud.jpg")), size=(1440, 900))
        background_label.configure(image=bg_image)

    if any(word in desc for word in atmosphere):
        bg_image = ctk.CTkImage(Image.open(resource_path("Atmosphere.jpg")), size=(1440, 900))

    if any(word in desc for word in snow):
        bg_image = ctk.CTkImage(Image.open(resource_path("Snow.jpg")), size=(1440, 900))
        background_label.configure(image=bg_image)

    if any(word in desc for word in rain):
        bg_image = ctk.CTkImage(Image.open(resource_path("Rain.jpg")), size=(1440, 900))
        background_label.configure(image=bg_image)

update_weather_btn = ctk.CTkButton(root, text="Update Weather", command=lambda:update_weather(place, bg_image, background_label))
update_weather_btn.place(relx=0.56, rely=0.16, anchor="center")

root.mainloop()