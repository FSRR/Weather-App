from flask import Flask
from flask import render_template
import requests
import json
from entity import *
from model import *
from controller import *

# app = Flask(__name__)

# @app.route('/')
# def index():
#     url = 'https://www.metaweather.com/api/location/418440/'
#     response = requests.get(url)

#     if response.status_code == 200:
#         responseJson = response.json()['consolidated_weather']
#         miraflores = DayController()
#         days = miraflores.days(responseJson)


#     return render_template('index.html')


# if __name__ == '__main__':
#     app.run(debug=True)

if __name__ == '__main__':
    url = 'https://www.metaweather.com/api/location/418440/'
    response = requests.get(url)

    if response.status_code == 200:
        responseJson = response.json()['consolidated_weather']
        miraflores = DayController()
        today = miraflores.today(responseJson)
        days = miraflores.days(responseJson)
        print(today)
        print(days)