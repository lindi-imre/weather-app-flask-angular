from enum import Enum
from typing import List, Optional
from datetime import datetime


class Coord:
    lat: float
    lon: float

    def __init__(self, lat: float, lon: float) -> None:
        self.lat = lat
        self.lon = lon


class City:
    id: int
    name: str
    coord: Coord
    country: str
    population: int
    timezone: int
    sunrise: int
    sunset: int

    def __init__(self, id: int, name: str, coord: Coord, country: str, population: int, timezone: int, sunrise: int, sunset: int) -> None:
        self.id = id
        self.name = name
        self.coord = coord
        self.country = country
        self.population = population
        self.timezone = timezone
        self.sunrise = sunrise
        self.sunset = sunset


class Clouds:
    all: int

    def __init__(self, all: int) -> None:
        self.all = all


class MainClass:
    temp: float
    feels_like: float
    temp_min: float
    temp_max: float
    pressure: int
    sea_level: int
    grnd_level: int
    humidity: int
    temp_kf: float

    def __init__(self, temp: float, feels_like: float, temp_min: float, temp_max: float, pressure: int, sea_level: int, grnd_level: int, humidity: int, temp_kf: float) -> None:
        self.temp = temp
        self.feels_like = feels_like
        self.temp_min = temp_min
        self.temp_max = temp_max
        self.pressure = pressure
        self.sea_level = sea_level
        self.grnd_level = grnd_level
        self.humidity = humidity
        self.temp_kf = temp_kf


class Rain:
    the_3_h: float

    def __init__(self, the_3_h: float) -> None:
        self.the_3_h = the_3_h


class Pod(Enum):
    D = "d"
    N = "n"


class Sys:
    pod: Pod

    def __init__(self, pod: Pod) -> None:
        self.pod = pod


class Description(Enum):
    BROKEN_CLOUDS = "broken clouds"
    CLEAR_SKY = "clear sky"
    FEW_CLOUDS = "few clouds"
    LIGHT_RAIN = "light rain"
    OVERCAST_CLOUDS = "overcast clouds"
    SCATTERED_CLOUDS = "scattered clouds"


class MainEnum(Enum):
    CLEAR = "Clear"
    CLOUDS = "Clouds"
    RAIN = "Rain"


class Weather:
    id: int
    main: MainEnum
    description: Description
    icon: str

    def __init__(self, id: int, main: MainEnum, description: Description, icon: str) -> None:
        self.id = id
        self.main = main
        self.description = description
        self.icon = icon


class Wind:
    speed: float
    deg: int
    gust: float

    def __init__(self, speed: float, deg: int, gust: float) -> None:
        self.speed = speed
        self.deg = deg
        self.gust = gust


class ListElement:
    dt: int
    main: MainClass
    weather: List[Weather]
    clouds: Clouds
    wind: Wind
    visibility: int
    pop: float
    sys: Sys
    dt_txt: datetime
    rain: Optional[Rain]

    def __init__(self, dt: int, main: MainClass, weather: List[Weather], clouds: Clouds, wind: Wind, visibility: int, pop: float, sys: Sys, dt_txt: datetime, rain: Optional[Rain]) -> None:
        self.dt = dt
        self.main = main
        self.weather = weather
        self.clouds = clouds
        self.wind = wind
        self.visibility = visibility
        self.pop = pop
        self.sys = sys
        self.dt_txt = dt_txt
        self.rain = rain


class Welcome8:
    cod: int
    message: int
    cnt: int
    list: List[ListElement]
    city: City

    def __init__(self, cod: int, message: int, cnt: int, list: List[ListElement], city: City) -> None:
        self.cod = cod
        self.message = message
        self.cnt = cnt
        self.list = list
        self.city = city
