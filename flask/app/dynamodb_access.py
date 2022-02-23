import os
import boto3


def get_resources():
    return boto3.resource('dynamodb',
                          aws_access_key_id=os.environ['AWS_KEY'],
                          aws_secret_access_key=os.environ['AWS_SECRET_KEY'],
                          region_name='eu-north-1')


def get_all_readings():
    client = get_resources()
    table = client.Table('temp_readings')
    response = table.scan()
    return response['Items']


def get_all_rfid_logs():
    client = get_resources()
    table = client.Table('entry_logs')
    response = table.scan()
    return response['Items']


def get_recent_rfid_logs():
    client = get_resources()
    table = client.table('entry_logs')
    # TODO Get 20 most recent logs.


def get_all_users():
    client = get_resources()
    table = client.Table('users')
    # TODO Filter out password & sensitive data.
    response = table.scan()
    return response['Items']


def add_tag(new_tag):
    client = get_resources()
    table = client.Table('users')
    table.put_item(Item=new_tag)
    return
