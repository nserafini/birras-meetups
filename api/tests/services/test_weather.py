from datetime import datetime
from meetups.services.weather import WeatherService
from unittest.mock import patch

@patch('meetups.services.weather.WeatherService.get_day')
def test_get_temperature(mock_api_weather):
    mock_api_weather.return_value = {"currently": {"temperature": 10.5}}
    ts = datetime.now().strftime("%s")
    temperature = WeatherService.get_temperature(ts)
    assert temperature == 10.5