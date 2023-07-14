import requests
from datetime import datetime

def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.strftime("%I:%M %p")

def showWeather():
    api_key = "95f00ca96e2f6b24123fa17b88124225"
    city_name = input("Enter the city name: ")

    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

    response = requests.get(weather_url)
    weather_info = response.json()

    if weather_info['cod'] == 200:
        kelvin = 273.15

        temp = int(weather_info['main']['temp'] - kelvin)
        feels_like_temp = int(weather_info['main']['feels_like'] - kelvin)
        pressure = weather_info['main']['pressure']
        humidity = weather_info['main']['humidity']
        wind_speed = weather_info['wind']['speed'] * 2.23694
        sunrise = weather_info['sys']['sunrise']
        sunset = weather_info['sys']['sunset']
        description = weather_info['weather'][0]['description']
        timezone = weather_info['timezone']

        sunrise_time = time_format_for_location(sunrise + timezone)
        sunset_time = time_format_for_location(sunset + timezone)

        print(f"\nCurrent Weather for {city_name}:")
        print(f"Temperature: {temp}°C")
        print(f"Feels Like: {feels_like_temp}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} mph")
        print(f"Sunrise: {sunrise_time}")
        print(f"Sunset: {sunset_time}")
        print(f"Weather Condition: {description}")
    else:
        print(f"\nWeather for city '{city_name}' not found!\nPlease enter a valid city name.")

showWeather()
