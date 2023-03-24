# import flask module
from flask import Flask,render_template,request

from flask_sqlalchemy import SQLAlchemy

import requests

# Initialising name to flask app
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def home():
    if request.method == 'POST':
        city = request.form.get('city')
        url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=4d2005c8ad2f2835fb9e2eb9d2b0968d'
        ret = requests.get(url.format(city)).json()

        weather = {
            'city': city,
            'temperature': ret['main']['temp'],
            'description': ret['weather'][0]['description'],
            'icon': ret['weather'][0]['icon']
        }

    return render_template('design.html',weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
