import requests

API_KEY = "eceadc2fd416eb132a02b68b888057f8"

def fetch_data():
  url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=New York"
  
  try:
    print("Fetching data from weatherstack...")  
    response = requests.get(url)
    response.raise_for_status()
    print("API response received successfully!")  
    return response.json()
  except requests.exceptions.RequestException as e:
    print(f"An error occured: {e}")
    raise

def mock_fetch_data():
  return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2025-06-21 03:03', 'localtime_epoch': 1750474980, 'utc_offset': '-4.0'}, 'current': {'observation_time': '07:03 AM', 'temperature': 23, 'weather_code': 116, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0004_black_low_cloud.png'], 'weather_descriptions': ['Partly Cloudy '], 'astro': {'sunrise': '05:25 AM', 'sunset': '08:31 PM', 'moonrise': '02:00 AM', 'moonset': '04:33 PM', 'moon_phase': 'Waning Crescent', 'moon_illumination': 26}, 'air_quality': {'co': '525.4', 'no2': '44.955', 'o3': '45', 'so2': '16.28', 'pm2_5': '28.675', 'pm10': '29.045', 'us-epa-index': '2', 'gb-defra-index': '2'}, 'wind_speed': 6, 'wind_degree': 275, 'wind_dir': 'W', 'pressure': 1018, 'precip': 0, 'humidity': 57, 'cloudcover': 0, 'feelslike': 25, 'uv_index': 0, 'visibility': 16, 'is_day': 'no'}}
  
