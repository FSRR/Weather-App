from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask import request
# from entity import *
# from model import *
# from controller import *
from request import *

app = Flask(__name__)

@app.route('/')
@app.route('/place/<woeid>')
def index(woeid = 44418):
    # lugar = DayController(woeid)

    # today = lugar.today()
    
    # data = lugar.days()

    today = ['Rain',15,23,56,33,22, 11]
    data = [(12,33,43), (10,33,43), (12,53,83), (21,33,42)]

    return render_template('index.html', today = today, anothersDays = data)


# @app.route('/location/<loc>', methods = ['GET'])
# def location(loc):
#     if request.method == 'GET':
#         location = ApiRequest()
#         woeid = location.myLocation(loc)

#     return redirect(f"/place/{woeid}")


if __name__ == '__main__':
    app.run(debug=True)
