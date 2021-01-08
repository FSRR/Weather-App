from datetime import datetime
from entity import *
from request import *

class DayDao:
    def __init__(self, woeid):
        self.__request = ApiRequest().myRequest(woeid)

    def dayOne(self):
        try:
            with open('requests/place.json', 'r') as f:
                data = json.load(f)
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
                print(information)
                return information
        except:
            print('No se puedo realizar la solicitud')

    def anotherDays(self):
        try:
            with open('requests/place.json', 'r') as f:
                data = json.load(f)['consolidated_weather']
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
        except:
            print('No se puedo realizar la solicitud')


prueba = DayDao(44418).dayOne()