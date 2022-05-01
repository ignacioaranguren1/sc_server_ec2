from marshmallow import Schema, fields, validate


class NewsSchema(Schema):
    """
        Schema for an incoming news
    """
    id = fields.Int(required=True)
    sentiment = fields.Int(required=True, validate=validate.Range(min=0, max=1))
