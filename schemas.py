from marshmallow import Schema, fields


class PlainItemSchema(Schema):
    item_id = fields.Int(dump_only=True)
    item_name = fields.Str(required=True)
    price = fields.Float(required=True)


class PlainWarehouseSchema(Schema):
    warehouse_id = fields.Int(dump_only=True)
    warehouse_name = fields.Str(required=True)


class ItemUpdateSchema(Schema):
    item_name = fields.Str()
    price = fields.Float()
    warehouse_id = fields.Int()


class ItemSchema(PlainItemSchema):
    warehouse_id = fields.Int(required=True)
    warehouse = fields.Nested(PlainWarehouseSchema(), dump_only=True)


class WarehouseSchema(PlainWarehouseSchema):
    items = fields.List(fields.Nested(PlainItemSchema()), dump_only=True)
