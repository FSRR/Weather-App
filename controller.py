from model import *

class DayController:
    def __init__(self, woeid):
        self.obj = DayDao(woeid)

    def today(self):
        return self.obj.dayOne()

    def days(self):
        return self.obj.anotherDays()
