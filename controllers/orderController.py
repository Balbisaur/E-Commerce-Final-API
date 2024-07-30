from flask import request, jsonify
from marshmallow import ValidationError
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from utils.util import user_token_required

def save():
    try:
        order_data = order_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400
    
    new_order = orderService.save(order_data)
    return order_schema.jsonify(new_order), 201

def find_all():
    all_orders = orderService.find_all()
    return orders_schema.jsonify(all_orders), 200

def find_by_id(order_id):
    order = orderService.find_by_id(order_id)
    if order:
        return order_schema.jsonify(order), 200
    else:
        return jsonify({'message': 'Order not found'}), 404

@user_token_required
def find_by_customer_id(customer_id, token_id):
    if customer_id == token_id:
        orders = orderService.find_by_customer_id(customer_id)
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({"message": "You can't view other people's orders"}), 403

def find_by_customer_email():
    try:
        email = request.json['email']
    except KeyError:
        return jsonify({'message': 'Email is required'}), 400

    orders = orderService.find_by_customer_email(email)
    if orders:
        return orders_schema.jsonify(orders), 200
    else:
        return jsonify({'message': 'No orders found for this email'}), 404
