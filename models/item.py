from db import db


class ItemModel(db.Model):
    __tablename__ = "items"

    item_id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(80), unique=True, nullable=False)
    price = db.Column(db.Float(precision=2), unique=False, nullable=False)
    warehouse_id = db.Column(db.Integer, db.ForeignKey("warehouses.warehouse_id"), unique=False, nullable=False)
    warehouse = db.relationship("WarehouseModel", back_populates="items")






















