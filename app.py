from flask import Flask
from flask import render_template
import requests
import json
from entity import *
from model import *
from controller import *

app = Flask(__name__)

@app.route('/')
def index():
    url = 'https://www.metaweather.com/api/location/418440/'
    # url = 'https://www.metaweather.com/api/location/44418/'
    response = requests.get(url)

    if response.status_code == 200:
        responseJson = response.json()

        lugar = DayController()

        today = lugar.today(responseJson)

        data = lugar.days(responseJson)


    return render_template('index.html', today = today, anothersDays = data)


if __name__ == '__main__':
    app.run(debug=True)
