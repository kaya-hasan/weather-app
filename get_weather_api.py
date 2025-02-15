import requests
import config


while True:
  city_name = input("Enter city name (or type 'exit' to quit) ")
  if city_name.lower() == 'exit':
    print('Goodbye!')
    break

  url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={config.api_key}&units=metric'


  response = requests.get(url)
  if response.status_code == 200:
    data = response.json()
    print('weather is',data["weather"][0]['description'])
    print('temperature is',data["main"]['temp'])
    print('temperature feels like',data["main"]['feels_like'])
    print('humidity is',data["main"]['humidity'])
  else:
    print("failed")