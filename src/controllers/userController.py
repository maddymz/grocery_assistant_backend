from flask import Blueprint,request, jsonify
import os
from src.service.firebaseService import userService

user_routes = Blueprint('user_routes',__name__, url_prefix='/user')


@user_routes.route('/add', methods=['POST'])
def create_order():
    try:
        id = request.json['userId']
        userService.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
@user_routes.route('/list', methods=['GET'])
def read_order():
    try:
        # Check if ID was passed to URL query
        userId = request.args.get('id')    
        if userId:
            user = userService.document(userId).get()
            return jsonify(user.to_dict()), 200
        else:
            all_user = [doc.to_dict() for doc in userService.stream(limit=10)]
            return jsonify(all_user), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
@user_routes.route('/update', methods=['POST', 'PUT'])
def update_order():
    try:
        id = request.json['id']
        userService.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
@user_routes.route('/delete', methods=['GET', 'DELETE'])
def delete_order():
    try:
        # Check for ID in URL query
        id = request.args.get('id')
        userService.document(id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"