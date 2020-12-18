from datetime import datetime
from entity import *

class DayDao:
    def __init__(self):
        pass

    def dayOne(self, data):
        today = Day()
        today.temperature = round(data['consolidated_weather'][0]['the_temp'], 1)
        today.weather = data['consolidated_weather'][0]['weather_state_name']

        date = data['consolidated_weather'][0]['applicable_date']
        today.date = datetime.strptime(date, '%Y-%m-%d').strftime('%a %d %b')

        today.windStatus = round(data['consolidated_weather'][0]['wind_speed'], 1)
        today.humidity = round(data['consolidated_weather'][0]['humidity'], 1)
        today.visibility = round(data['consolidated_weather'][0]['visibility'], 1)
        today.airPressure = round(data['consolidated_weather'][0]['air_pressure'])
        today.place = data['title']

        information = (today.temperature, today.weather, today.date, today.windStatus, today.humidity, today.visibility, today.airPressure, today.place)
        return information

    def anotherDays(self, data):
        dt = []
        for i in range(5):
            tomorrow = Day()
            tomorrow.maxTemp = round(data[i+1]['max_temp'], 1)
            tomorrow.minTemp = round(data[i+1]['min_temp'], 1)
            tomorrow.weather = data[i+1]['weather_state_name']

            date = data[i+1]['applicable_date']
            tomorrow.date = datetime.strptime(date, '%Y-%m-%d').strftime('%a, %d %b')
            
            information = (tomorrow.maxTemp, tomorrow.minTemp, tomorrow.weather, tomorrow.date)
            dt.append(information)

        return dt
