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
urls = [
    "https://i.pinimg.com/originals/09/62/14/096214a506862dfeb83db3ae8936f315.png",
    "https://i.pinimg.com/474x/26/96/5f/26965f8b07068aefc05f01b969dd7bec.jpg",
    "https://i.pinimg.com/736x/6e/d2/ed/6ed2ed5a850b7b2ea9f193c0de16677f.jpg",
    "https://i.pinimg.com/736x/82/52/64/8252646faf5908f9644ef57ee79da489--pop-corn-prisma.jpg",
    "https://i.pinimg.com/originals/1a/c3/cf/1ac3cfec371cb38fa5dbadd536abbc0a.jpg",
    "https://i.pinimg.com/736x/8e/2e/64/8e2e64c2d2f68a534ffacd0207c1a7cc.jpg",
    "https://i.pinimg.com/736x/cc/ef/bd/ccefbd80fed09dd07825b7206e88c265.jpg",
    "https://i.pinimg.com/564x/a7/8c/2d/a78c2d004931a70fd2e7f6318a9d41b0.jpg",
    "https://i.pinimg.com/736x/b2/78/56/b278565d5c5acb18bf87d67df51b228a.jpg",
    "https://i.pinimg.com/736x/f6/e6/a9/f6e6a9901d35fa645d39d9973d02097b.jpg",
    "https://i.pinimg.com/280x280_RS/c0/46/d0/c046d0dfa2e9830992151920364399ab.jpg",
    "https://i.pinimg.com/736x/23/f1/3c/23f13cea8cede854514cee31a89a63e6--classic-white-the-loaf.jpg",
    "https://i.pinimg.com/originals/91/b9/bb/91b9bb25eeb795a8b6c1ad9ca0f01c0d.jpg"
]

image_dict = {index + 1: url for index, url in enumerate(urls)}

df = pd.read_csv(csv_file)

id = 1

for index, row in df.iterrows():
    # Read the values from the DataFrame row
    food_item = row['FoodItem']
    food_category = row['FoodCategory']

    # Create a dictionary for the JSON object
    json_obj = {
        "itemId": "itm"+str(id).zfill(6),
        "name": food_item,
        "description": food_item + " - " + food_category,
        "tags": [food_item.lower(),food_category.lower()],
        "rating": random.randint(3, 5),
        "price": random.randint(3, 8)+0.99,
        "image": image_dict[random.randint(1, 12)]
    }
    item_id = json_obj["itemId"]
    # json_string = json.dumps(json_obj)
    itemService.document(item_id).set(json_obj)
    id += 1