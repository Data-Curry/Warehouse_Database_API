from db import db


class WarehouseModel(db.Model):
    __tablename__ = "warehouses"

    warehouse_id = db.Column(db.Integer, primary_key=True)
    warehouse_name = db.Column(db.String(80), unique=True, nullable=False)
    items = db.relationship("ItemModel", back_populates="warehouse", lazy="dynamic")

