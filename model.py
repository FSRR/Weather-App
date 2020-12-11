from entity import *

class DayDao:
    def __init__(self):
        pass

    def dayOne(self, data):
        today = Day()
        today.temperature = data['the_temp']
        today.weather = data['weather_state_name']
        today.date = data['applicable_date']
        today.windStatus = data['wind_speed']
        today.humidity = data['humidity']
        today.visibility = data['visibility']
        today.airPressure = data['air_pressure']
        information = (today.temperature, today.weather, today.date, today.windStatus, today.humidity, today.visibility, today.airPressure)
        return information

    def dayTwo(self, data):
        tomorrow = Day()
        tomorrow.temperature = data['the_temp']
        tomorrow.weather = data['weather_state_name']
        tomorrow.date = data['applicable_date']
        information = (tomorrow.temperature, tomorrow.weather, tomorrow.date)
        return information

    def dayThree(self, data):
        three = Day()
        three.temperature = data['the_temp']
        three.weather = data['weather_state_name']
        three.date = data['applicable_date']
        information = (three.temperature, three.weather, three.date)
        return information

    def dayFour(self, data):
        four = Day()
        four.temperature = data['the_temp']
        four.weather = data['weather_state_name']
        four.date = data['applicable_date']
        information = (four.temperature, four.weather, four.date)
        return information

    def dayFive(self, data):
        five = Day()
        five.temperature = data['the_temp']
        five.weather = data['weather_state_name']
        five.date = data['applicable_date']
        information = (five.temperature, five.weather, five.date)
        return information

    def daySix(self, data):
        six = Day()
        six.temperature = data['the_temp']
        six.weather = data['weather_state_name']
        six.date = data['applicable_date']
        information = (six.temperature, six.weather, six.date)
        return information