from typing import List


class Clouds:
    all: int

    def __init__(self, all: int) -> None:
        self.all = all


class Coord:
    lon: float
    lat: float

    def __init__(self, lon: float, lat: float) -> None:
        self.lon = lon
        self.lat = lat


class Main:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    humidity: int

    def __init__(self, temp: float, feels_like: float, temp_min: float, temp_max: float, pressure: int, humidity: int) -> None:
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.humidity = humidity


class Sys:
    type: int
    id: int
    country: str
    sunrise: int
    sunset: int

    def __init__(self, type: int, id: int, country: str, sunrise: int, sunset: int) -> None:
        self.type = type
        self.id = id
        self.country = country
        self.sunrise = sunrise
        self.sunset = sunset


class Weather:
    id: int
    main: str
    description: str
    icon: str

    def __init__(self, id: int, main: str, description: str, icon: str) -> None:
        self.id = id
        self.main = main
        self.description = description
        self.icon = icon


class Wind:
    speed: float
    deg: int

    def __init__(self, speed: float, deg: int) -> None:
        self.speed = speed
        self.deg = deg


class WeatherInfo:
    coord: Coord
    weather: List[Weather]
    base: str
    main: Main
    visibility: int
    wind: Wind
    clouds: Clouds
    dt: int
    sys: Sys
    timezone: int
    id: int
    name: str
    cod: int

    def __init__(self, coord: Coord, weather: List[Weather], base: str, main: Main, visibility: int, wind: Wind, clouds: Clouds, dt: int, sys: Sys, timezone: int, id: int, name: str, cod: int) -> None:
        self.coord = coord
        self.weather = weather
        self.base = base
        self.main = main
        self.visibility = visibility
        self.wind = wind
        self.clouds = clouds
        self.dt = dt
        self.sys = sys
        self.timezone = timezone
        self.id = id
        self.name = name
        self.cod = cod
