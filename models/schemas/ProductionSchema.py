from marshmallow import fields
from schema import ma

class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False) #id is autogenerated
    product_id = fields.Integer(required=True)
    quantity_produced = fields.Integer(required=True)
    date_produced = fields.Date(required=True)

    class Meta:
        fields = ("id", "product_id", "quantity_produced", "date_produced")

#Create instances of the schemas
production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)