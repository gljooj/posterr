from datetime import datetime
from src.controller.post_controller import PostController
from src.core.infra.database.database_config import DataBaseConfig


class TestPostController:
    __db = DataBaseConfig().db
    controller = PostController()
    user = '{"username": "usertestpost"}'

    """The Rules is in the test_post_schema has here"""

    def setup(self):
        self.__db.post.delete_many({"username": "usertestpost"})
        self.__db.user.delete_many({"username": "usertestpost"})

        self.__db.user.insert_one({"username": "usertestpost",
                                   "joined_at": datetime(2022, 7, 17, 4, 55, 5)})

    def test_new_post_success(self):
        post = self.controller.new_post(post={"type": "post", "text": "test_success"}, user=self.user)
        assert post['body']['message']

    def test_repost_new_post_test_ok(self):
        post = self.controller.new_post(post={"type": "repost",
                                              "original_post": {"username": "usertest1", "type": "post",
                                                                "text": "test_repost_new_post_test_ok"}},
                                        user=self.user)

        assert post['body']['message']

    def test_quote_post_test_ok(self):
        post = self.controller.new_post(post={"type": "quote-post", "text": "test_quote_post_test_ok",
                                              "original_post": {"username": "usertest1", "type": "post",
                                                                "text": "first"}
                                              }, user=self.user)
        assert post['body']['message']

    def test_repost_quote_post_test_ok(self):
        post = self.controller.new_post(post={"type": "repost",
                                              "original_post": {"type": "quote-post",
                                                                "text": "test_repost_quote_post_test_ok",
                                                                "username": "usertest1",
                                                                "original_post": {"username": "usertest1",
                                                                                  "type": "post",
                                                                                  "text": "first"}
                                                                }
                                              }, user=self.user)
        assert post['body']['message']

    def test_quote_post_to_repost_test_ok(self):
        post = self.controller.new_post(
            {"type": "quote-post", "text": "test_quote_post_to_repost_test_ok",
             "original_post": {"username": "usertest1", "type": "repost",
                               "original_post": {"username": "usertest1", "type": "post", "text": "first"}
                               }
             }, user=self.user)
        assert post['body']['message']

    def test_post_test_big_string_nok(self):
        post = self.controller.new_post(post={"type": "post", "text": 'a' * 778}, user=self.user)
        assert post[0]['body']['error']
        assert post[1] == 400

    def test_repost_repost_nok(self):
        post = self.controller.new_post(post={"type": "repost",
                                              "original_post": {"username": "usertest1", "type": "repost",
                                                                "text": "first"}
                                              }, user=self.user)
        assert post[0]['body']['error']
        assert post[1] == 400

    def test_quote_post_quote_post_nok(self):
        post = self.controller.new_post({"type": "quote-post", "text": "testing text",
                                         "original_post": {"username": "usertest1", "type": "quote-post",
                                                           "text": "first"}
                                         }, user=self.user)
        assert post[0]['body']['error']
        assert post[1] == 400

    def test_repost_with_text(self):
        post = self.controller.new_post(post={"type": "repost", "text": "first"}, user=self.user)
        assert post[0]['body']['error']
        assert post[1] == 400

    def test_not_field_exist(self):
        post = self.controller.new_post(post={"post_none": "not_field_exist"}, user=self.user)
        assert post[0]['body']['error']
        assert post[1] == 400

    def finished(self):
        self.__db.user.delete_many({"username": "usertestpost"})
        self.__db.post.delete_many({"username": "usertestpost"})
