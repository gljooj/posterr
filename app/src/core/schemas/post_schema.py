from marshmallow import Schema, fields, ValidationError, validates_schema


class PostSchema(Schema):
    username = fields.Str(required=True)
    type = fields.Str(required=True)
    text = fields.String()
    original_post = fields.Dict()

    @validates_schema
    def validate(self, data, **kwargs):
        self.validate_types(data)
        if 'text' in data:
            if len(data['text']) > 777:
                raise ValidationError(
                    "Text Lengh must be smaller than 777 characters"
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

    def validate_types(self, data):
        if data['type'] not in ["post", "repost", "quote-post"]:
            raise ValidationError(
                "Type must be in [post, repost, quote-post]"
            )
        if data['type'] in ['repost', 'quote-post'] and 'original_post' not in data:
            raise ValidationError(
                "When [repost, quote-post] inform original_post"
            )

        if data['type'] == 'quote-post' and data['original_post']['type'] == 'quote-post':
            raise ValidationError(
                "When quote-posts just can be to [post, repost]"
            )

        if data['type'] == 'repost' and 'text' in data:
            if data not in ['', None]:
                raise ValidationError(
                    "When repost you can not text"
                )
            raise ValidationError(
                "When repost you can not text"
            )
