import pymongo
import csv
import json
from pymongo import MongoClient
from csv import DictReader

import pandas as pd

df = pd.read_csv (r'Ecuador.csv', delimiter = ",", index_col=0)
df.to_json (r'Ecuador.json', orient = 'index')
print(df)