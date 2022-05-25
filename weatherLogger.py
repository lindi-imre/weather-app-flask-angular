class WeatherLogger:
    def writeDataToFile(self, weatherInfo):
        logfile = open("logs/weatherLog.csv", "a")
        record = weatherInfo.name + "," + str(weatherInfo.main.temp) + "," + str(weatherInfo.main.humidity) + "\n"
        logfile.write(record)
        logfile.close()
        print("Actual weather info saved")

    def writeForecastDataToFile(self, weatherInfo):
        logfile = open("logs/weatherForecast.json", "w")
        logfile.write(weatherInfo)
        logfile.close()
        print("Forecast info saved")
