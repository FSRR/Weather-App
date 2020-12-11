class Day:
    def __init__(self):
        self.__temperature = None
        self.__weather = None
        self.__date = None
        self.__windStatus = None
        self.__humidity = None
        self.__visibility = None
        self.__airPressure = None
        self.__place = None

    @property
    def temperature(self):
        return self.__temperature

    @property
    def weather(self):
        return self.__weather

    @property
    def date(self):
        return self.__date

    @property
    def windStatus(self):
        return self.__windStatus

    @property
    def humidity(self):
        return self.__humidity

    @property
    def visibility(self):
        return self.__visibility

    @property
    def airPressure(self):
        return self.__airPressure

    @property
    def place(self):
        return self.__place

    @temperature.setter
    def temperature(self, temperature):
        self.__temperature = temperature

    @weather.setter
    def weather(self, weather):
        self.__weather = weather

    @date.setter
    def date(self, date):
        self.__date = date

    @windStatus.setter
    def windStatus(self, windStatus):
        self.__windStatus = windStatus

    @humidity.setter
    def humidity(self, humidity):
        self.__humidity = humidity

    @visibility.setter
    def visibility(self, visibility):
        self.__visibility = visibility

    @airPressure.setter
    def airPressure(self, airPressure):
        self.__airPressure = airPressure

    @place.setter
    def place(self, place):
        self.__place = place
