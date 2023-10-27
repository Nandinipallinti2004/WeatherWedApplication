import requests

api_key = '655863c54c0b66301309b998b32df694'
api_endpoint = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_data(city):
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = requests.get(api_endpoint, params=params)
        response.raise_for_status()
        weather_data = response.json()
        return weather_data
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None

def display_weather_info(weather_data):
    if weather_data:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Conditions: {description}")
    else:
        print("Unable to fetch weather data.")

def main():
    print("Welcome to the Weather App!")
    city = input("Enter the name of the city: ")
    
    weather_data = get_weather_data(city)

    print("\nWeather Information:")
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()
