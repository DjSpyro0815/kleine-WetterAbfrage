import requests

api_key = "84fb584c49d62a0a6f85782a5803e98f"
city = input("Moin Moin bitte gib deine Stadt hier ein\n")
# api.openweathermap.org/data/2.5/weather?q={city name},{state code},{country code}&appid={API key}

url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

data = requests.get(url).json()
Temperatur = data['main']['temp']
Luftfeuchtigkeit = data['main']['humidity']

print(f'in {city} beträgt die {Temperatur}. Die Luftfeuchtigkeit beträgt {Luftfeuchtigkeit}')