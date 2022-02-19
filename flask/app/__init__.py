from flask import Flask, render_template
from app import dynamodb_access

app = Flask(__name__)


@app.get('/')
def index():
    all_readings = dynamodb_access.get_all_readings()
    print(all_readings)
    return render_template('index.html', all_readings=all_readings)

@app.get('/all_logs')
def logs():
    all_logs = dynamodb_access.get_all_rfid_logs()
    return render_template('all_logs.html', all_logs=all_logs)

@app.get('all_users')
def users():
    all_users = dynamodb_access.get_all_users
    return render_template('all_users.html', all_users)