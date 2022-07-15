from marshmallow import Schema, fields, validate


class PostSchema(Schema):
    username = fields.Str(required=True)
    # Criar regra para repost
    text = fields.Str(validate=validate.Length(max=777))
    type = fields.Str(required=True)
    original_post = fields.Dict()
