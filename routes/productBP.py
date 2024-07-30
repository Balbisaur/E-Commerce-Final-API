from flask import Blueprint
from controllers.productController import find_all, save, search_product

# Create a Blueprint for product-related routes
product_blueprint = Blueprint('product_bp', __name__)

# Define routes and their corresponding view functions
product_blueprint.add_url_rule('/', methods=['POST'], view_func=save)
product_blueprint.add_url_rule('/', methods=['GET'], view_func=find_all)
product_blueprint.add_url_rule('/search', methods=['GET'], view_func=search_product)
