from flask import Flask
import json

app = Flask(__name__)



@app.route("/")
def hello():
    person = {
        'name': 'Jhon',
        'age': 25,
        'city': 'Osaka'
    }
    nama = json.dumps(person)
    return nama