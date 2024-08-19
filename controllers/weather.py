from modules import database as database
from modules import http as http
from modules import math_funcs as math_funcs
from dotenv import load_dotenv
import pytest
import datetime
import json
import os
load_dotenv()
MathFuncs = math_funcs.MathFuncs()

class WeatherController:
    def __init__(self) -> None:
        self.http = http.HttpClient()
        self.db = database.DatabaseClient()
        self.GEO_API_URL = os.getenv('GEO_LOCATION_API_URL')
        self.WEATHER_API_ONE_CALL_URL = os.getenv('WEATHER_API_ONE_CALL_URL')
        self.WEATHER_API_URL = os.getenv('WEATHER_API_URL')
        self.WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')
        self.APP_ID = '&appid=' + self.WEATHER_API_KEY


    def get_weather(self, city: str, date: str) -> dict:
        """
        Get Weather for a given city and date
        """
        try:
            converted_city_to_lat_lon = self.fetch_lat_lon(city)
            weather_for_city = self.fetch_weather_one_call(converted_city_to_lat_lon, date)

            # Check here first if weather data is already in the database
            
            try:
                weather_data = json.loads(weather_for_city)
                weather_data['city'] = city
                weather_data['date'] = date
                print(weather_data)
                self.db.add_weather_data(weather_data)
            except Exception as e:
                print(f'Error adding weather data to database: {str(e)}')
    

            return {
                'sucess': True,
                'city': city,
                'date': date,
                'weather': weather_for_city
            }
        except Exception as e:
            return {
                'error': str(e),
                'status': 'error'
            }
        
    def test_get_weather(self, city: str, date: str) -> dict:
        """
        Test Get Weather for a given city and date
        """
        try:
            converted_city_to_lat_lon = self.fetch_lat_lon(city)
            weather_for_city = self.fetch_weather_one_call(converted_city_to_lat_lon, date)

            try: 
                # Assert if the min_temp less than max_temp
                weather_data = json.loads(weather_for_city)
                assert weather_data['min_temp'] < weather_data['max_temp'], 'Min Temp is less than Max Temp'
                assert weather_data['average_mean_temp'] < weather_data['max_temp'], 'Average Mean Temp is less than Max Temp'
                assert weather_data['average_mode_temp'] < weather_data['max_temp'], 'Average Mode Temp is less than Max Temp'
                assert weather_data['average_mean_humidity'] < 100, 'Average Mean Humidity is less than 100'
            except Exception as e:
                return {
                    'sucess': False,
                    'error': str(e),
                    'status': 'error',
                    'message': 'Test Failed'
                }

            return {
                'sucess': True,
                'city': city,
                'date': date,
                'weather': weather_for_city
            }
        except Exception as e:
            return {
                'error': str(e),
                'status': 'error'   
            }
        
    
    def fetch_lat_lon(self, city: str) -> dict:
        """
        Fetch Latitude and Longitude for a given city, return dict with lat and lon
        """
        try:
            formatted_url = f'{self.GEO_API_URL}{city}&limit=1&appid={self.WEATHER_API_KEY}'
            geo_location = self.http.get(formatted_url)
            return {
                'latitute': MathFuncs.round_cordinates(geo_location[0]['lat']),
                'longitude': MathFuncs.round_cordinates(geo_location[0]['lon']),
            }
        except Exception as e:
            return {
                'error': str(e),
                'status': 'error'
            }

    def fetch_weather_one_call(self, city: str, date: str) -> dict:
        """
        Fetch Weather for a given city and date, return dict with weather details
        """
        try:
            formatted_url = f'{self.WEATHER_API_ONE_CALL_URL}lat={city["latitute"]}&lon={city["longitude"]}&cnt=1&exclude=hourly,minutely&units=metric{self.APP_ID}'
            weather_data = self.http.get(formatted_url)
            weather = self.parse_weather_data(weather_data)
            return json.dumps(weather)
        except Exception as e:
            return {
                'error': str(e),
                'status': 'error'
            }
        
    def parse_weather_data(self, weather_data: dict) -> str:
        """
        Parse Weather Data to return only temperature details for each day.
        Returns a JSON string with temperature details.
        """
        for day in weather_data.get('daily', []):
            date = MathFuncs.convert_epoch_to_date(day['dt'])
            min_temp = day['temp']['min']
            max_temp = day['temp']['max']
            average_mean_temp = MathFuncs.calculate_mean_average([min_temp, max_temp, day['temp']['day'], day['temp']['night'], day['temp']['eve'], day['temp']['morn']])
            average_mode_temp = MathFuncs.calculate_mode_average([min_temp, max_temp, day['temp']['day'], day['temp']['night'], day['temp']['eve'], day['temp']['morn']])
            average_mean_humidity = MathFuncs.calculate_mean_average([day['humidity']])
            average_mode_humidity = MathFuncs.calculate_mode_average([day['humidity']])

            payload = json.dumps({
                'date': date,
                'min_temp': min_temp,
                'max_temp': max_temp,
                'average_mean_temp': average_mean_temp,
                'average_mode_temp': average_mode_temp,
                'average_mean_humidity': average_mean_humidity,
                'average_mode_humidity': average_mode_humidity,
            })
            response = json.loads(payload)
        # Convert list of dictionaries to JSON string without slashes
        return response

    
    