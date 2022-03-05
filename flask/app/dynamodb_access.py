import os
import boto3
from boto3.dynamodb.conditions import Attr
import json

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


#TODO Get 20 most recent logs.
def get_recent_rfid_logs():
    client = get_resources()
    table = client.table('entry_logs')


def get_all_users():
    client = get_resources()
    table = client.Table('users')
    response = table.scan(
        AttributesToGet=['id', 'access', 'created', 'username']
    )
    return response['Items']


def add_tag(new_tag):
    client = get_resources()
    table = client.Table('users')
    table.put_item(Item=new_tag)
    return


def get_users(search_string):
    client = get_resources()
    table = client.Table('users')
    response = table.scan(
        FilterExpression=Attr('username').contains(search_string)
    )
    for item in response['Items']:
        item.pop("password")
    return response['Items']


def get_user(id):
    client = get_resources()
    table = client.Table('users')
    response = table.get_item(Key={'id': id})
    return response['Item']


def update_user(user):
    client = get_resources()
    table = client.Table('users')
    key = {
        'id': {'S': user['id']}
    }
    response = table.get_item(key)
    return


def delete_tag(tag_id):
    client = get_resources()
    table = client.Table('users')
    key = {
        'id': tag_id
    }
    response = table.delete_item(Key=key)
    print(response)
    return
