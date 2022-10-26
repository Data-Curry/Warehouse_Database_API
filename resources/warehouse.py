# import uuid
# from flask import request
from flask.views import MethodView
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError, IntegrityError

from db import db
from models import WarehouseModel
from schemas import WarehouseSchema

blp = Blueprint("warehouses", __name__, description="Operations on warehouses")


@blp.route("/warehouse/<string:warehouse_id>")
class Warehouse(MethodView):
    @blp.response(200, WarehouseSchema)
    def get(self, warehouse_id):              # Get a warehouse
        warehouse = WarehouseModel.get_or_404(warehouse_id)
        return warehouse

    def delete(self, warehouse_id):           # Delete a warehouse
        warehouse = WarehouseModel.query.get_or_404(warehouse_id)
        raise NotImplementedError("Deleting a warehouse is not implemented.")


@blp.route("/warehouse")
class WarehouseList(MethodView):
    @blp.response(200, WarehouseSchema(many=True))
    def get(self):                                          # Get all warehouses
        return warehouses.values()

    @blp.arguments(WarehouseSchema)
    @blp.response(200, WarehouseSchema)
    def post(self, warehouse_data):                         # Create a warehouse
        warehouse = WarehouseModel(**warehouse_data)

        try:
            db.session.add(warehouse)
            db.session.commit()
        except IntegrityError:
            abort(
                400,
                message="A warehouse with that name already exists."
            )
        except SQLAlchemyError:
            abort(500, message="An error occurred while inserting the item.")

        return warehouse







































