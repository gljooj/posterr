from marshmallow import Schema, fields, validate


class Post(Schema):
    date = fields.DateTime()
    owner_username = fields.Str()
    text = fields.Str(validate=validate.Length(max=777))
    type = fields.Str()
    username = fields.Str()
