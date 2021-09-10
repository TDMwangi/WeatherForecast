import tkinter as tk
#from tkinter import font
import requests
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")

def format_response(weather):
    try:
        name = weather['name']
        country = weather['sys']['country']
        desc = weather['weather'][0]['description']
        timezone = weather['timezone']
        temp = weather['main']['temp']
        final_str = 'City: %s \nCountry: %s \nCondition: %s \nTimezone: %s \nTemperature (°C): %s' % (name, country, desc, timezone, temp)
    except:
        final_str = 'Error occurred while retrieving data'
    return final_str

def get_weather(city):
    weather_key = f"{API_KEY}"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"APPID": weather_key, "q": city, "units": "celsius"}
    response = requests.get(url, params = params)
    weather = response.json()
    label['text'] = format_response(weather)

window = tk.Tk()
window.title("Weather Forecast")

WIDTH = 800
HEIGHT = 700
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (WIDTH / 2)
y_coordinate = (screen_height / 2) - (HEIGHT / 2)
window.geometry("%dx%d+%d+%d" % (WIDTH, HEIGHT, x_coordinate, y_coordinate))
#canvas = tk.Canvas(window, height=HEIGHT, width=WIDTH)
#canvas.pack()

window.iconbitmap("bg_icon.ico")

background_image = tk.PhotoImage(file="bg.png")
background_label = tk.Label(window, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(window, bg="#80c1ff", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

entry = tk.Entry(frame, font=("Calibri", 18))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Show Weather", font=("Calibri", 16), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lower_frame = tk.Frame(window, bg="#80c1ff", bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lower_frame, font=("Calibri", 18))
label.place(relwidth=1, relheight=1)

window.mainloop()