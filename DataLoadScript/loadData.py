import csv
import json
import requests
import pandas as pd
import random


from firebase_admin import credentials, firestore, initialize_app

cred = credentials.Certificate('./firebase-private.json')
default_app = initialize_app(cred)
db = firestore.client()
itemService = db.collection('items')


# Specify the path to your CSV file
csv_file = '/Users/sarthakrawat/PythonProjects/hackathon/gpt-jam-backend/DataLoadScript/FoodNames.csv'



index = 0

df = pd.read_csv(csv_file)

id = 1

for index, row in df.iterrows():
    # Read the values from the DataFrame row
    food_item = row['FoodItem']
    food_category = row['FoodCategory']
    image_url = row['Image']

    # Create a dictionary for the JSON object
    json_obj = {
        "itemId": "itm"+str(id).zfill(6),
        "name": food_item,
        "description": food_item + " - " + food_category,
        "tags": [food_item.lower(),food_category.lower()],
        "rating": random.randint(3, 5),
        "price": random.randint(3, 8)+0.99,
        "image": image_url
    }
    item_id = json_obj["itemId"]
    # json_string = json.dumps(json_obj)
    itemService.document(item_id).set(json_obj)
    id += 1