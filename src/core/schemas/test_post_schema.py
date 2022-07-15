from marshmallow import ValidationError

from src.core.schemas.post_schema import PostSchema


def validate_schema(post):
    try:
        PostSchema().load(post)
        return True
    except ValidationError:
        return False


def test_order_load_data():
    test_data = [{"username": "post_test_ok", "type": "post", "text": "first"},

                 {"username": "repost_test_ok", "type": "repost",
                  "original_post": {"username": "post_test_ok", "type": "post", "text": "first"}
                  },

                 {"username": "repost_quote_post_test_ok", "type": "repost",
                  "original_post": {"username": "post_test_ok", "type": "post", "text": "first"}
                  },

                 {"username": "quote_post_test_ok", "type": "quote-post", "text": "testing text",
                  "original_post": {"username": "post_test_ok", "type": "post", "text": "first"}
                  },

                 {"username": "quote_post_to_repost_test_ok", "type": "quote-post", "text": "testing text",
                  "original_post": {"username": "post_test_ok", "type": "post", "text": "first"}
                  },

                 {"username": "post_test_big_string", "type": "post", "text": 'a' * 778},

                 {"username": "repost_repost", "type": "repost",
                  "original_post": {"username": "post_test_ok", "type": "repost", "text": "first"}
                  },

                 {"username": "quote-post_quote-post", "type": "quote-post", "text": "testing text",
                  "original_post": {"username": "post_test_ok", "type": "quote-post", "text": "first"}
                  },

                 {"username": "repost_with_text", "type": "repost", "text": "first"},

                 {"username": "not_field_exist", "post_none": "not_field_exist"}
                 ]

    # assert expected, on the examples in array each username has the name of test,
    # and the assert_expected is the expected
    assert_expected = {"post_test_ok": True,
                       "repost_test_ok": True,
                       "repost_quote_post_test_ok": True,
                       "quote_post_test_ok": True,
                       "quote_post_to_repost_test_ok": True,

                       "post_test_big_string": False,
                       "repost_repost": False,
                       "quote-post_quote-post": False,
                       "repost_with_text": False,
                       "not_field_exist": False,
                       }

    for post in test_data:
        assert assert_expected[post.get('username')] == validate_schema(post)
