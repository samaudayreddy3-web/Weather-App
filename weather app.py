import requests

API_KEY = "YOUR_API_KEY"

print("==============================")
print("       WEATHER APP")
print("==============================")

city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": API_KEY,
    "units": "metric"
}

try:
    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:

        print("\n------------------------------")
        print("Weather Information")
        print("------------------------------")

        print("City       :", data["name"])
        print("Temperature:", round(data["main"]["temp"]), "°C")
        print("Weather    :", data["weather"][0]["description"])
        print("Humidity   :", data["main"]["humidity"], "%")
        print("Wind Speed :", data["wind"]["speed"], "m/s")

        print("------------------------------")
        print("Thank you for using Weather App!")

    else:
        print("\nCity not found.")
        print("Please enter a valid city name.")

except Exception:
    print("\nSomething went wrong.")
    print("Please check your internet connection.")ss