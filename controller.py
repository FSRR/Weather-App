from model import *

class DayController:
    def __init__(self):
        self.obj = DayDao()

    def today(self, data):
        return self.obj.dayOne(data)

    def days(self, data, i):
        return self.obj.anotherDays(data['consolidated_weather'][i])
