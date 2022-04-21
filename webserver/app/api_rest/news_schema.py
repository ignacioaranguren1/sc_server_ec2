from marshmallow import Schema, fields


class NewsSchema(Schema):
    """
        Schema for an incoming news
    """
    id = fields.Int(required=True)
    sentiment = fields.Str(required=True)
