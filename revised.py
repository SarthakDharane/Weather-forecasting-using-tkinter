from tkinter import *
import requests
import json
import datetime
from PIL import Image, ImageTk

root = Tk()
root.title("Weather App")
root.geometry("450x700")
root['background'] = "white"

dt = datetime.datetime.now()
date = Label(root, text=dt.strftime('%A--'), bg='white', font=("bold", 15))
date.place(x=5, y=130)
month = Label(root, text=dt.strftime('%m %B'), bg='white', font=("bold", 15))
month.place(x=100, y=130)

hour = Label(root, text=dt.strftime('%I:%M %p'), bg='white', font=("bold", 15))
hour.place(x=10, y=160)

city_name = StringVar()
city_entry = Entry(root, textvariable=city_name, width=45)
city_entry.grid(row=1, column=0, ipady=10, stick=W+E+N+S)

def get_weather():
    api_url = f//enter API here"
    try:
        api_request = requests.get(api_url)
        api = api_request.json()
        
        if api['cod'] == 200:
            y = api['main']
            current_temprature = y['temp']
            humidity = y['humidity']
            tempmin = y['temp_min']
            tempmax = y['temp_max']

            x = api['coord']
            longtitude = x['lon']
            latitude = x['lat']
            
            z = api['sys']
            country = z['country']
            citi = api['name']

            lable_temp.config(text=f"{current_temprature}°C")
            lable_humidity.config(text=f"{humidity}%")
            max_temp.config(text=f"{tempmax}°C")
            min_temp.config(text=f"{tempmin}°C")
            lable_lon.config(text=f"{longtitude}")
            lable_lat.config(text=f"{latitude}")
            lable_country.config(text=country)
            lable_citi.config(text=citi)
        else:
            lable_citi.config(text="City Not Found")

    except Exception as e:
        lable_citi.config(text="Network Error")

city_nameButton = Button(root, text="Search", command=get_weather)
city_nameButton.grid(row=1, column=1, padx=5, stick=W+E+N+S)

lable_citi = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_citi.place(x=10, y=63)
lable_country = Label(root, text="...", width=0, bg='white', font=("bold", 15))
lable_country.place(x=135, y=63)
lable_lon = Label(root, text="...", width=0, bg='white', font=("Helvetica", 15))
lable_lon.place(x=25, y=95)
lable_lat = Label(root, text="...", width=0, bg='white', font=("Helvetica", 15))
lable_lat.place(x=95, y=95)
lable_temp = Label(root, text="...", width=0, bg='white', font=("Helvetica", 110), fg='black')
lable_temp.place(x=18, y=220)
humi = Label(root, text="Humidity:", bg='white', font=("bold", 15))
humi.place(x=3, y=400)
lable_humidity = Label(root, text="...", bg='white', font=("bold", 15))
lable_humidity.place(x=107, y=400)
maxi = Label(root, text="Max. Temp.:", bg='white', font=("bold", 15))
maxi.place(x=3, y=430)
max_temp = Label(root, text="...", bg='white', font=("bold", 15))
max_temp.place(x=128, y=430)
mini = Label(root, text="Min. Temp.:", bg='white', font=("bold", 15))
mini.place(x=3, y=460)
min_temp = Label(root, text="...", bg='white', font=("bold", 15))
min_temp.place(x=128, y=460)
note = Label(root, text="All temperatures in degree Celsius", bg='white', font=("italic", 10))
note.place(x=95, y=495)

root.mainloop()
