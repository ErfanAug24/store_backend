from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.Str(required=True)
    password = fields.Str(required=True)


class UserRegistrationSchema(UserSchema):
    email = fields.Str(required=True)


class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    price = fields.Str(required=True)
    description = fields.Str(required=True)


class RegisterProductSchema(ProductSchema):
    name = fields.Str(required=True)
    price = fields.Str(required=True)
    description = fields.Str(required=True)


user_schema = UserSchema()
user_schemas = UserSchema(many=True)

user_register_schema = UserRegistrationSchema()
user_register_schemas = UserRegistrationSchema(many=True)


product_schema = ProductSchema()
products_schema = ProductSchema(many=True)


product_registration_schema = RegisterProductSchema()
product_registration_schemas = RegisterProductSchema(many=True)
