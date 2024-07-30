from marshmallow import fields
from . import ma

class OrderSchema(ma.Schema):
    id = fields.Integer(dump_only=True)  # Primary key
    date = fields.Date(required=True)     # Date of the order
    customer_id = fields.Integer(required=True)  # Reference to the customer
    products = fields.Nested("ProductSchema", many=True)  # List of products in the order
    customer = fields.Nested("CustomerOrderSchema")  # Detailed customer information
    
    class Meta:
        fields = ('id', 'date', 'customer_id', 'products', 'customer')

# Create instances of the OrderSchema
order_schema = OrderSchema()
orders_schema = OrderSchema(many=True)  # For handling multiple orders
