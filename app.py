from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
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


@app.route('/hola')
def place(woeid):
    url = f'https://www.metaweather.com/api/location/{woeid}/'
    response = requests.get(url)

    if response.status_code == 200:
        responseJson = response.json()
        print(responseJson)

    return redirect(url_for('index'))


@app.route('/<loc>')
def location(loc):
    url = f'https://www.metaweather.com/api/location/search/?lattlong={loc}'
    response = requests.get(url)

    if response.status_code == 200:
        responseJson = response.json()
        woeid = responseJson[0]['woeid']
        print(woeid)

    return redirect(url_for(f'place({woeid})'))


if __name__ == '__main__':
    app.run(debug=True)
