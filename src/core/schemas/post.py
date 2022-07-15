from marshmallow import Schema, fields, validate, ValidationError, validates_schema


class PostSchema(Schema):
    username = fields.Str(required=True)
    # Criar regra para repost
    text = fields.Str(validate=validate.Length(max=777))
    type = fields.Str(required=True)
    original_post = fields.Dict()

    @validates_schema
    def validate_type(self, data,  **kwargs):
        if data['type'] not in ["post", "repost", "quote-post"]:
            raise ValidationError(
                'type must be in ["post", "repost", "quote-post"]'
            )
        if data['type'] in ['repost', 'quote-post'] and 'original_post' not in data:
            raise ValidationError(
                "When [repost, quote-post] inform original_post"
            )
        if data['type'] == 'repost' and 'text' in data:
            if data not in ['', None]:
                raise ValidationError(
                    "When repost you can not text"
                )
            raise ValidationError(
                "When repost you can not text"
            )

        if 'original_post' in data:
            if data['original_post']['type'] == "repost":
                raise ValidationError(
                    "You Cannot repost a repost"
                )
            try:
                PostSchema().load(data['original_post'])
            except ValidationError as err:
                raise Exception({"original_post_validation": err.messages})
