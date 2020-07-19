import requests
from meetups.core.config import settings

class WeatherService:
    @classmethod
    def get_temperature(cls, ts):
        response = cls.get_day(ts)
        temperature = response['currently']['temperature']
        return temperature

    @classmethod
    def get_day(cls, ts):
        url = settings.RAPID_API_URL
        coord = settings.RAPID_API_COORD
        endpoint = f"{url}/{coord},{ts}"
        headers = {
            'x-rapidapi-host': settings.RAPID_API_HOST,
            'x-rapidapi-key': settings.RAPID_API_KEY
        }
        params = {"units":"auto"}
        response = requests.get(endpoint, headers=headers, params=params).json()
        return response