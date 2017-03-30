import pymongo

from pymongo import MongoClient
from bottle import route, run, template

# Bottle
# @route('/hello/<name>')
# def index(name):
#     return template('<b>Hello {{name}}</b>!', name=name)
#
# run(host='localhost', port=8080)

# PyMongo
# connect to database
connection = MongoClient('localhost', 27017)
db = connection['people']

# handle to names collection
names = db.names

item = names.find_one()

print item['name']
