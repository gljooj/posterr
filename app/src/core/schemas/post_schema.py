import json

from marshmallow import Schema, fields, ValidationError, validates_schema

from src.controller import ProfileValidate


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
            user_original_post = json.dumps({"username": data['original_post']['username']})

            ProfileValidate(user=user_original_post).validate_user()

            if data['original_post']['type'] == data['type']:
                msg = "When quote-posts just can be to [post, repost]" \
                    if data['type'] == 'quote-post' else "When repost just can be to [post, quote-post]"
                raise ValidationError(
                    f"You Cannot {data['type']} a {data['type']}"
                    f" Choose one of {msg}"
                )

            if data['original_post']['type'] in ['repost', 'quote-post']:
                if 'original_post' in data['original_post']:
                    user_original_original_post = json.dumps(
                        {"username": data['original_post']['original_post']['username']}
                    )

                    ProfileValidate(user=user_original_original_post).validate_user()
                    try:
                        PostSchema().load(data['original_post']['original_post'])
                    except ValidationError as err:
                        raise Exception({"original_post_validation": err.messages})

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

        if data['type'] == 'post' and 'original_post' in data:
            raise ValidationError(
                "Posts must be new"
            )

        if data['type'] == 'repost' and 'text' in data:
            if data['text'] not in ['', None]:
                raise ValidationError(
                    "When repost you can not text"
                )
            raise ValidationError(
                "When repost you can not text"
            )
