import pymongo

conn = 'mongodb://52.53.164.143:27017/'
client = pymongo.MongoClient(conn)
import csv
import json
from pymongo import MongoClient
import pandas as pd

BeerMarketDf = pd.read_json('USBeerMarket.json')


db = client.INTL_db
audits = db.audits.find()
for row in BeerMarketDf:
    db.audits.insert_one({'ID': row})
