from flask import Blueprint, request, jsonify
import os
from src.service.firebaseService import itemService

item_routes = Blueprint('item_routes', __name__, url_prefix='/item')


empty_item = dict({
    "description": "Product Not Avaialble",
    "image": "",
    "itemId": "NA",
    "name": "Product Not Avaialble",
    "price": 0.0,
    "rating": 5,
    "tags": [
            ""
    ]
})


@item_routes.route('/add', methods=['POST'])
def create_item():
    try:
        id = request.json['itemId']
        itemService.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@item_routes.route('/list', methods=['GET'])
def read_item():
    try:
        # Check if ID was passed to URL query
        itemId = request.args.get('id')
        if itemId:
            item = itemService.document(itemId).get()
            return jsonify(item.to_dict()), 200
        else:
            all_items = [doc.to_dict() for doc in itemService.stream(limit=10)]
            return jsonify(all_items), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@item_routes.route('/list', methods=['POST'])
def read_item_list():
    try:
        itemIds = request.json['itemIds']
        result = []
        for itemId in itemIds:
            if itemId.startswith("NA"):
                words = itemId.split("-")
                itemName = words[1]
                empty_item["name"] = "NOT AVAILABLE - "+itemName.upper()
                result.append(empty_item)
                continue
            item = itemService.document(itemId).get()
            result.append(item.to_dict())
        return jsonify(result), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@item_routes.route('/update', methods=['POST', 'PUT'])
def update_item():
    try:
        id = request.json['id']
        itemService.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@item_routes.route('/delete', methods=['GET', 'DELETE'])
def delete_item():
    try:
        # Check for ID in URL query
        id = request.args.get('id')
        itemService.document(id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"


@item_routes.route('/listTop', methods=['GET'])
def read_top_item():
    try:
        all_items = [doc.to_dict() for doc in itemService.limit(50).get()]
        return jsonify(all_items), 200
    except Exception as e:
        return f"An Error Occured: {e}"
