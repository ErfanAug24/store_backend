from flask.views import MethodView
from flask_smorest import Blueprint, abort
from src.api.v1.models.product import ProductModel
from src.api.v1.schemas.schemas import ProductSchema, RegisterProductSchema
from datetime import datetime
from flask_jwt_extended import jwt_required

blp = Blueprint("ProductsApi", 'productsapi', description="Operations on stores")


@blp.route('/product/<string:product_id>')
class Product(MethodView):
    @jwt_required()
    @blp.response(200, ProductSchema)
    def get(self, product_id) -> "ProductModel":
        return ProductModel.find_by_id(product_id)

    @blp.response(201, ProductSchema)
    @blp.arguments(RegisterProductSchema)
    def Put(self, product_id, product_data):
        product = ProductModel.find_by_id(product_id)
        if product:
            product.name = product_data['name']
            product.created_at = datetime.utcnow
            product.price = product_data['price']
            product.description = product_data['description']
        else:
            product = ProductModel(product_data['name'],
                                   product_data['price'],
                                   product_data['description']
                                   )
        product.save()
        return product

    # it seems that it need admin premission to delete something on database.
    @jwt_required()
    def delete(self, product_id):
        product = ProductModel.find_by_id(product_id)
        product.delete()
        return {'message': 'the product had been deleted !'}


@blp.route('/product_list')
class ProductList(MethodView):
    @jwt_required()  # admin premission required
    @blp.response(200, ProductSchema(many=True))
    def get(self):
        return ProductModel.query.all()
