from model import *

class DayController:
    def __init__(self):
        self.obj = DayDao()

    def today(self, data):
        return self.obj.dayOne(data[0])

    # def secondDay(self, data):
    #     return self.obj.dayTwo(data[1])

    # def thirdDay(self, data):
    #     return self.obj.dayThree(data[2])

    # def fourthDay(self, data):
    #     return self.obj.dayFour(data[3])

    # def fifthDay(self, data):
    #     return self.obj.dayFive(data[4])

    # def sixthDay(self, data):
    #     return self.obj.daySix(data[5])

    def days(self, data):
        information = []
        # self.obj.dayTwo(data[1])
        # self.obj.dayThree(data[2])
        # self.obj.dayFour(data[3])
        # self.obj.dayFive(data[4])
        # self.obj.daySix(data[5])

        return information
