from src.controller.profile_controller import ProfileController
from src.core.infra.database.database_config import DataBaseConfig


class TestProfileController:
    def test_new_user(self):
        profile_controller = ProfileController(user=None)
        new_user = profile_controller.new_user({"username": "test"})
        assert new_user['body']['message']

    def test_new_user_error(self):
        profile_controller = ProfileController(user=None)
        new_user = profile_controller.new_user({"a": "test"})
        print(new_user)
        assert new_user[0]['body']['error']
        assert new_user[1] == 400

    def test_profile_page_success(self):
        profile_controller = ProfileController(user='{"username": "usertest1"}')
        profile_page = profile_controller.profile_page()
        assert profile_page['body']['profile']['username'] == profile_controller.user['username']
        assert profile_page['body']['posts']
        assert profile_page['body']['total_posts']

    def test_profile_page_failed(self):
        profile_controller = ProfileController(user='{"uasername": "usertest1"}')
        profile_page = profile_controller.profile_page()
        assert profile_page[0]['body']['error']
        assert profile_page[1] == 500


__db = DataBaseConfig()
__db.db.user.delete_one({"username": "test"})
