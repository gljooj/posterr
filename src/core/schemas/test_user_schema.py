from marshmallow import ValidationError

from src.core.schemas.user_schema import UserSchema


def validate_schema(post):
    try:
        UserSchema().load(post)
        return True
    except ValidationError:
        return False


def test_order_load_data():
    test_data = [{"username": "new"},
                 {"username": "opa09"},
                 {"username": "newwwwwwwwwwwww"},
                 {"username": "opa 09"}]

    # assert expected, on the examples in array each username has the name of test,
    # and the assert_expected is the expected
    assert_expected = {"new": True,
                       "opa09": True,
                       "newwwwwwwwwwwww": False,
                       "opa 09": False
                       }

    for post in test_data:
        assert assert_expected[post.get('username')] == validate_schema(post)
