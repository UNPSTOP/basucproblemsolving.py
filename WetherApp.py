import requests

def get_weather(city, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        weather = data['weather'][0]
        
        temperature = main['temp']
        pressure = main['pressure']
        humidity = main['humidity']
        description = weather['description']

        print(f"Weather in {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Pressure: {pressure} hPa")
        print(f"Humidity: {humidity}%")
        print(f"Condition: {description.capitalize()}")
    else:
        print("City not found. Please check the name and try again.")

def main():
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key
    city = input("Enter city name: ")
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
