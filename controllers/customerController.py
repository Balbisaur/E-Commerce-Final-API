from flask import request, jsonify
from models.schemas.customerSchema import customer_schema, customers_schema, customer_cart_schema
from services import customerService
from marshmallow import ValidationError
from caching import cache
from utils.util import admin_required, token_required

def login():
    try:
        credentials = request.json
        token = customerService.login(credentials['username'], credentials['password'])
    except KeyError:
        return jsonify({'message': 'Invalid payload, expecting username and password'}), 401

    if token:
        return jsonify(token), 200
    else:
        return jsonify({'message': "Invalid username or password"}), 401

def save():
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as e:
        return jsonify(e.messages), 400

    customer_saved = customerService.save(customer_data)
    return customer_schema.jsonify(customer_saved), 201

@admin_required
# @cache.cached(timeout=60)
def find_all():
    all_customers = customerService.find_all()
    return customers_schema.jsonify(all_customers), 200

@admin_required
def find_all_paginate():
    try:
        page = int(request.args.get("page", 1))
        per_page = int(request.args.get("per_page", 10))
    except ValueError:
        return jsonify({'message': 'Invalid pagination parameters'}), 400

    customers = customerService.find_all_paginate(page, per_page)
    return customers_schema.jsonify(customers), 200

@token_required
def cart():
    try:
        user_id = request.args.get('user_id')
        if not user_id:
            return jsonify({'message': 'User ID is required'}), 400

        customer_cart = customerService.get_cart(user_id)
        return customer_cart_schema.jsonify(customer_cart), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 500
