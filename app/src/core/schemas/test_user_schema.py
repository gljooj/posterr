from marshmallow import ValidationError

from app.src.core.schemas.user_schema import UserSchema


def validate_schema(post):
    try:
        UserSchema().load(post)
        return True
    except ValidationError:
        return False


def test_order_load_data():
    test_data = [{"username": "isalpha"},
                 {"username": "opa0isaplha099"},
                 {"username": "havemorethanfourtenstring"},
                 {"username": "is_not_alpha_numeric"}]

    # assert expected, on the examples in array each username has the name of test,
    # and the assert_expected is the expected
    assert_expected = {"isalpha": True,
                       "opa0isaplha099": True,
                       "havemorethanfourtenstring": False,
                       "is_not_alpha_numeric": False
                       }

    for post in test_data:
        assert assert_expected[post.get('username')] == validate_schema(post)
