from tkinter import *
import requests #pip install requests
import json
from datetime import datetime
 
#Tkinter window
root =Tk()
root.geometry("500x500")
root.resizable(0,0)
root.title("Weather App")
 
#Initializing variables
city_value = StringVar()
curcity=StringVar()


def current_location():
    global curcity
    #Using ipstack API
    send_url = "http://api.ipstack.com/check?access_key=2fc3bd945ae59f22634588ab06506a3a"
    geo_req = requests.get(send_url)
    geo_json = json.loads(geo_req.text)
    latitude = geo_json['latitude']
    longitude = geo_json['longitude']
    curcity = geo_json['city']
    showWeather(1)
 
def time_format(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()
 
def showWeather(n=0):
    if n==1:
        city_name=curcity
        api_key = "69b3ff78255bd74c49d78f0a02212b2b" 
    
        # Using Openweathermap API
        weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    
        # Get the response from fetched url
        response = requests.get(weather_url)
    
        # Loading the json data 
        weather_info = response.json()
    
        #to clear the text field for every new output
        tfield.delete("1.0", "end") 
    
        #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
        if weather_info['cod'] == 200:
            kelvin = 273
            country = weather_info['sys']['country']

            temp = int(weather_info['main']['temp'] - kelvin)
            feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']
            lat = weather_info['coord']['lat']
            lon = weather_info['coord']['lon']
            sunrise_time = time_format(sunrise + timezone)
            sunset_time = time_format(sunset + timezone)
            
            weather = f"\nWeather of: {city_name}\nCountry (code): {country}\nLatitude of current location: {lat}\nLongitude of current location: {lon}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nDescription: {description}"
        else:
            weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    
    
        #To insert values to be displayed in the text field 
        tfield.insert(INSERT, weather) 
    else:
        city_name=city_value.get()

        api_key = "69b3ff78255bd74c49d78f0a02212b2b" 
    
        # Using Openweathermap API
        weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    
        # Get the response from fetched url
        response = requests.get(weather_url)
    
        # Loading the json data 
        weather_info = response.json()
    
        #to clear the text field for every new output
        tfield.delete("1.0", "end") 
    
        #as per API documentation, if the cod is 200, it means that weather data was successfully fetched
        if weather_info['cod'] == 200:
            kelvin = 273
            country = weather_info['sys']['country']
            temp = int(weather_info['main']['temp'] - kelvin)
            feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
            pressure = weather_info['main']['pressure']
            humidity = weather_info['main']['humidity']
            sunrise = weather_info['sys']['sunrise']
            sunset = weather_info['sys']['sunset']
            timezone = weather_info['timezone']
            cloudy = weather_info['clouds']['all']
            description = weather_info['weather'][0]['description']
    
            sunrise_time = time_format(sunrise + timezone)
            sunset_time = time_format(sunset + timezone)
            
            weather = f"\nWeather of: {city_name}\nCountry (code): {country}\nTemperature (Celsius): {temp}°\nFeels like in (Celsius): {feels_like_temp}°\nPressure: {pressure} hPa\nHumidity: {humidity}%\nSunrise at {sunrise_time} and Sunset at {sunset_time}\nCloud: {cloudy}%\nDescription: {description}"
        else:
            weather = f"\n\tWeather for '{city_name}' not found!\n\tKindly Enter valid City Name !!"
    
    
        #To insert values to be displayed in the text field 
        tfield.insert(INSERT, weather)   
 
def exit():
    root.destroy()
 
city_head= Label(root, text = 'Enter City Name', font = 'Arial 12 bold').pack(pady=10)
 
inp_city = Entry(root, textvariable = city_value,  width = 24, font='Arial 14 bold').pack()
 
 
Button(root, command = showWeather, text = "Check Weather", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=2, pady=2).pack(pady= 5)
Button(root, command = current_location, text = "Use current location", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=2, pady=2).pack(pady=5)
Button(root, command = exit, text="EXIT", font="Arial 10", bg='lightblue', fg='black', activebackground="teal", padx=2, pady=2).pack(pady=5)

weather_now = Label(root, text = "The current weather is:", font = 'arial 12 bold').pack(pady=10)
 
tfield = Text(root, width=46, height=13)
tfield.pack()

root.mainloop()