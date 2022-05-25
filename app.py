from collections import namedtuple
from functools import wraps
from apscheduler.schedulers.background import BackgroundScheduler

import jwt
import json
import requests
from flask import Flask, jsonify, request
from datetime import timedelta, datetime
from flask_cors import CORS

import weatherLogger

app = Flask(__name__)
app.config['SECRET_KEY'] = 'VERYSECRETKEY'
CORS(app)


def weatherDecoder(weatherDict):
    return namedtuple('X', weatherDict.keys())(*weatherDict.values())


def getWeatherDataFromApi():
    response = requests.get("https://api.openweathermap.org/data/2.5/weather?q=Kecskemet,hu&APPID=ac230c93f3172f79b1a1fc48bf5da4c6")
    weather = json.loads(json.dumps(response.json()), object_hook=weatherDecoder)
    return weather

def getWeatherForecastDataFromApi():
    response = requests.get("https://api.openweathermap.org/data/2.5/forecast?lat=46.895092&lon=19.687977&appid=ac230c93f3172f79b1a1fc48bf5da4c6")
    return response.json()


def token_required(func):
    # decorator factory which invoks update_wrapper() method and passes decorated function as an argument
    @wraps(func)
    def decorated(*args, **kwargs):
        token = request.headers.get('token')
        if not token:
            return jsonify({'Alert!': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            print(data)
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
        except:
           return jsonify({'Message': 'Invalid token'}), 403
        return func(*args, **kwargs)
    return decorated

@app.route('/')
@token_required
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/loginjwt', methods=['POST'])
def loginJwt():
    content = request.json
    if(content["username"] == "testuser" and content["password"] == "123456"):
        token = jwt.encode({
                'user': content["username"],
                'expiration': str(datetime.utcnow() + timedelta(seconds=600))
            }, app.config['SECRET_KEY'])
        return jsonify({"token": token.encode().decode("UTF-8")})

    return jsonify({"message" : "invalid login credentials"})

def logWeatherInfo():
    logger = weatherLogger.WeatherLogger()
    logger.writeDataToFile(getWeatherDataFromApi())
    logger.writeForecastDataToFile(str(getWeatherForecastDataFromApi()))

scheduler = BackgroundScheduler()
scheduler.add_job(func=logWeatherInfo, trigger="interval", seconds=30)
scheduler.start()

if __name__ == '__main__':
    app.run()
