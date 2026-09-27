import requests

API_KEY = "6b33a005eea84a5322483a7c12b825c5"


def get_weather():
    city = input("\nEnter City Name: ")

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        city_name = data["name"]
        country = data["sys"]["country"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        humidity = data["main"]["humidity"]
        weather = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]

        print("\n==============================")
        print("       WEATHER REPORT")
        print("==============================")
        print(f"City: {city_name}, {country}")
        print(f"Temperature: {temperature}°C")
        print(f"Feels Like: {feels_like}°C")
        print(f"Weather: {weather}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
        print("==============================")

    elif response.status_code == 404:
        print("\nCity not found!")

    elif response.status_code == 401:
        print("\nInvalid API key!")

    else:
        print("\nSomething went wrong!")


while True:
    print("\n===== WEATHER APPLICATION =====")

    get_weather()

    choice = input("\nCheck another city? (y/n): ").strip().lower()

    if choice != "y":
        print("\nThank You For Using Weather Application!")
        break