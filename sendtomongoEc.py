import pymongo
import csv
import json
from pymongo import MongoClient 

import pandas as pd
with open('Ecuador.json') as f:
    file_data = json.load(f)
client = MongoClient('mongodb://admin:new_password_here@52.53.164.143:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass%20Community&ssl=false')
db = client['INTL_db']
db["audits"].insert_one(file_data)