import requests

API_KEY = "YOUR_API_KEY"

def get_weather(city="Istanbul"):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

    try:
        res = requests.get(url).json()
        weather = res["weather"][0]["main"]
        return weather
    except:
        return "sunny"