from entity import *

class DayDao:
    def __init__(self):
        pass

    def dayOne(self, data):
        today = Day()
        today.temperature = round(data['consolidated_weather']['the_temp'], 1)
        today.weather = data['consolidated_weather']['weather_state_name']
        today.date = data['consolidated_weather']['applicable_date']
        today.windStatus = round(data['consolidated_weather']['wind_speed'], 1)
        today.humidity = round(data['consolidated_weather']['humidity'], 1)
        today.visibility = round(data['consolidated_weather']['visibility'], 1)
        today.airPressure = round(data['consolidated_weather']['air_pressure'])
        today.place = data.title
        information = (today.temperature, today.weather, today.date, today.windStatus, today.humidity, today.visibility, today.airPressure)
        return information

    def anotherDays(self, data):
        tomorrow = Day()
        tomorrow.temperature = data['the_temp']
        tomorrow.weather = data['weather_state_name']
        tomorrow.date = data['applicable_date']
        information = (tomorrow.temperature, tomorrow.weather, tomorrow.date)
        return information
