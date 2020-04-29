import pymongo
import csv
import json
from pymongo import MongoClient
from csv import DictReader

import pandas as pd

df = pd.read_csv (r'USBeerMarket.csv', delimiter = ",", index_col=0)
df.to_json (r'USBeerMarket.json', orient = 'index')
print(df)