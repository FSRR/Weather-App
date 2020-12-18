from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
from entity import *
from model import *
from controller import *
import requests as req
import json

app = Flask(__name__)

@app.route('/')
@app.route('/place/<woeid>')
def index(woeid = 44418):
    url = f'https://www.metaweather.com/api/location/{woeid}/'
    response = req.get(url)

    if response.status_code == 200:
        responseJson = response.json()

        lugar = DayController()

        today = lugar.today(responseJson)

        data = lugar.days(responseJson)

        return render_template('index.html', today = today, anothersDays = data)


@app.route('/location/<loc>', methods = ['GET'])
def location(loc):
    if request.method == 'GET':
        url = f'https://www.metaweather.com/api/location/search/?lattlong={loc}'
        response = req.get(url)

        if response.status_code == 200:
            responseJson = response.json()
            location = responseJson[0]

    return redirect(f"/place/{location['woeid']}")

if __name__ == '__main__':
    app.run(debug=True)
