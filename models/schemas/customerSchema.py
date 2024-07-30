from marshmallow import fields
from . import ma

class CustomerSchema(ma.Schema):
    id = fields.Integer(required=False)  
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)  
    role_id = fields.Integer(required=True)  

    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password", "role_id")


class CustomerOrderSchema(ma.Schema):
    id = fields.Integer(required=False)  
    name = fields.String(required=True)
    email = fields.Email(required=True)
    phone = fields.String(required=True)
    username = fields.String(required=True)
    password = fields.String(required=True)  
    orders = fields.Nested("OrderSchema", many=True)  

    class Meta:
        fields = ("id", "name", "email", "phone", "username", "password", "orders")


class CustomerCart(ma.Schema):
    name = fields.String(required=True)
    cart = fields.Nested("ProductSchema", many=True)  

    class Meta:
        fields = ("name", "cart")


# Instantiate schemas
customer_schema = CustomerSchema()
customers_schema = CustomerSchema(many=True, exclude=("password",))  
customer_order_schema = CustomerOrderSchema()
customer_cart_schema = CustomerCart()
