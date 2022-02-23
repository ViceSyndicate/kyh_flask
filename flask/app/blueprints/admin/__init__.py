import datetime
import uuid
from flask import Blueprint, redirect, url_for

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
    name = request.form['name']
    password = request.form['password']
    #TODO double check that passwords match & other safety checks.
    check_password = request.form['check-password']
    access_level = request.form['access-level']

    id = str(uuid.uuid4())

    current_time = datetime.datetime.now()
    created_time = current_time.strftime("%y-%m-%d %H:%M:%S")

    #id, password, user_created, username

    new_tag = {
        'id': id,
        'password': password,
        'created': created_time,
        'username': name,
        'access': access_level
    }
    dynamodb_access.add_tag(new_tag)
    return redirect(url_for('bp_admin.users'))
