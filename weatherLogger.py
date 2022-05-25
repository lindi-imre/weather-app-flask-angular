class WeatherLogger:
    def writeDataToFile(self, weatherInfo):
        print("ticked")
        logfile = open("weatherLog.csv", "a")
        record = weatherInfo.name + "," + str(weatherInfo.main.temp) + "," + str(weatherInfo.main.humidity) + "\n"
        logfile.write(record)
        logfile.close()

    def writeForecastDataToFile(self, weatherInfo):
        logfile = open("weatherForecast.json", "w")
        logfile.write(weatherInfo)
        logfile.close()
