from model import *

class DayController:
    def __init__(self):
        self.obj = DayDao()

    def today(self, data):
        return self.obj.dayOne(data[0])

    def days(self, data, i):
        return self.obj.anotherDays(data[i])
