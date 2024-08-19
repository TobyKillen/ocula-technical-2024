from typing import Optional, Union
from fastapi import FastAPI
from controllers import weather as WeatherControllerClass
from datetime import datetime

app = FastAPI()
WeatherController = WeatherControllerClass.WeatherController()

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.get("/weather/{city}")
@app.get("/weather/{city}/{date}")
def get_weather_for_city(city: str, date: Optional[str] = None) -> Union[dict, str]:
    # Default date to today if not provided
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')  # Format as 'YYYY-MM-DD'

    # Optional: Add validation for City and Date (e.g., valid date and city)
    # Validate City Name if it's not ISO 3166 country code
    try:
        weather = WeatherController.get_weather(city, date)
        return weather
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }

@app.get("/weather/{city}/test")
@app.get("/weather/{city}/{date}/test")
def test_get_weather_for_city(city: str, date: Optional[str] = None) -> Union[dict, str]:
    # Default date to today if not provided
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
        
    try:
        weather = WeatherController.test_get_weather(city, date)
        return weather
    except Exception as e:
        return {
            'error': str(e),
            'status': 'error'
        }