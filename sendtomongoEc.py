import pymongo
import csv
import json
from pymongo import MongoClient 

import pandas as pd
with open('Ecuador.json') as f:
    file_data = json.load(f)
client = MongoClient('mongodb://127.0.0.1:27017/?compressors=disabled&gssapiServiceName=mongodb')
db = client['INTL_db']
db["audits"].insert_one(file_data)