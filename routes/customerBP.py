from flask import Blueprint
from controllers.customerController import find_all_paginate, login, save, find_all

# Create a Blueprint for customer-related routes
customer_blueprint = Blueprint('customer_bp', __name__)

# Define routes and their corresponding view functions
customer_blueprint.add_url_rule('/', methods=['POST'], view_func=save)
customer_blueprint.add_url_rule('/', methods=['GET'], view_func=find_all)
customer_blueprint.add_url_rule('/paginate', methods=['GET'], view_func=find_all_paginate)
customer_blueprint.add_url_rule('/login', methods=['POST'], view_func=login)
