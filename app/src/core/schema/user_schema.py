from marshmallow import Schema, fields, validates_schema, ValidationError


class UserSchema(Schema):
    username = fields.Str(required=True)

    @validates_schema
    def validate_type(self, data, **kwargs):
        if len(data['username']) > 14:
            raise ValidationError(
                "Username Lenght must be smaller than 14 characters"
            )
        if not data['username'].isalnum():
            raise ValidationError(
                "Text must be alphanumeric"
            )
