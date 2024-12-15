import os.path
from tinydb import TinyDB

data = [
    {'name': 'Order FormEmailDate', 'order_email': 'email', 'order_date': 'date'},
    {'name': 'FormEmailDate', 'user_email': 'email', 'user_date': 'date'},
    {'name': 'Order FormEmailPhone', 'order_email': 'email', 'order_phone': 'phone'},
    {'name': 'FormEmailPhone', 'user_email': 'email', 'user_phone': 'phone'},
    {'name': 'Order FormEmailPhoneDate', 'order_email': 'email', 'order_phone': 'phone', 'order_date': 'date'},
    {'name': 'FormEmailPhoneDate', 'user_email': 'email', 'user_phone': 'phone', 'user_date': 'date'},
    {'name': 'Order FormEmail', 'order_email': 'email'},
    {'name': 'FormEmail', 'user_email': 'email'},
    {'name': 'Order FormText', 'order_text': 'text'},
    {'name': 'FormText', 'user_text': 'text'}
]

if not os.path.isfile('db.json'):
    db = TinyDB('db.json')
    for entry in data:
        db.insert(entry)
