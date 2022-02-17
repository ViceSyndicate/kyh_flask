from flask import Flask, render_template
from app import dynamodb_access

app = Flask(__name__)


@app.get('/')
def index():
    all_readings = dynamodb_access.get_all_readings()
    print(all_readings)
    return render_template('index.html', all_readings=all_readings)