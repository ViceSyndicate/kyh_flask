from flask import Blueprint

bp_admin = Blueprint('bp_admin', __name__)

from flask import Flask, render_template, request
from app import dynamodb_access


@bp_admin.get('/')
def index():
    all_readings = dynamodb_access.get_all_readings()
    print(all_readings)
    return render_template('index.html', all_readings=all_readings)


@bp_admin.get('/all_logs')
def logs():
    all_logs = dynamodb_access.get_all_rfid_logs()
    return render_template('all_logs.html', all_logs=all_logs)


@bp_admin.get('/all_users')
def users():
    all_users = dynamodb_access.get_all_users()
    return render_template('all_users.html', all_users=all_users)


@bp_admin.get('/create_user')
def create_user():
    return render_template('create_user.html')


@bp_admin.post('/create_user')
def post_created_user():
    all_users = dynamodb_access.get_all_users
    return render_template('all_users.html', all_users=all_users)
    #data = request.form['name']
    #data = request.form['password']
    #data = request.form['check-password']
    #data = request.form['access-level']
    #all_users = dynamodb_access.get_all_users
    #return render_template('all_users.html', all_users=all_users)