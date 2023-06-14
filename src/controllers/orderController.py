from flask import Blueprint,request, jsonify
import os
from src.service.firebaseService import orderService

order_routes = Blueprint('order_routes',__name__, url_prefix='/order')


@order_routes.route('/add', methods=['POST'])
def create_order():
    try:
        id = request.json['orderId']
        orderService.document(id).set(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
@order_routes.route('/list', methods=['GET'])
def read_order():
    try:
        # Check if ID was passed to URL query
        orderId = request.args.get('id')    
        if orderId:
            order = orderService.document(orderId).get()
            return jsonify(order.to_dict()), 200
        else:
            all_orders = [doc.to_dict() for doc in orderService.stream(limit=10)]
            return jsonify(all_orders), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
@order_routes.route('/update', methods=['POST', 'PUT'])
def update_order():
    try:
        id = request.json['id']
        orderService.document(id).update(request.json)
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"
    
@order_routes.route('/delete', methods=['GET', 'DELETE'])
def delete_order():
    try:
        # Check for ID in URL query
        id = request.args.get('id')
        orderService.document(id).delete()
        return jsonify({"success": True}), 200
    except Exception as e:
        return f"An Error Occured: {e}"