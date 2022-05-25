from flask import json


class WeatherInfoDto:
    city: str
    temperature: float
    current_date: str

    def __init__(self, city: str, temperature: float, current_date: str) -> None:
        self.city = city
        self.temperature = temperature
        self.current_date = current_date


    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                          sort_keys=True, indent=4)