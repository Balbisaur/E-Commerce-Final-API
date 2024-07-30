from flask import Blueprint
from controllers.orderController import find_by_customer_email, find_by_customer_id, find_by_id, save, find_all

# Create a Blueprint for order-related routes
order_blueprint = Blueprint('order_bp', __name__)

# Define routes and their corresponding view functions
order_blueprint.add_url_rule('/', methods=['POST'], view_func=save)
order_blueprint.add_url_rule('/', methods=['GET'], view_func=find_all)
order_blueprint.add_url_rule('/<int:id>', methods=['GET'], view_func=find_by_id)
order_blueprint.add_url_rule('/customer/<int:id>', methods=['GET'], view_func=find_by_customer_id)
order_blueprint.add_url_rule('/customer/email', methods=['POST'], view_func=find_by_customer_email)
