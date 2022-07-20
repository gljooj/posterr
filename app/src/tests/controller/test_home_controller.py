from datetime import datetime

from src.controller.home_controller import HomeController


class TestHomeController:
    controller_success = HomeController(user='{"username": "test_home"}', page=1,
                                        post_from='only-mine', start_at=None, end_at=None)

    def test_define_query_success(self):
        assert self.controller_success.define_query() == self.controller_success.user
        alternate_controller = self.controller_success
        alternate_controller.post_from = "all"
        assert alternate_controller.define_query() == {}

    def test_define_query_error(self):
        alternate_controller = self.controller_success
        alternate_controller.post_from = "not_exist"
        try:
            self.controller_success.define_query()
        except Exception as e:
            assert e.args[0] == 'Filter must be all or only-mine'

    def test_define_date_query_success(self):
        controller_date = self.controller_success
        controller_date.start_at = "2022-07-18 04:55:05"
        controller_date.end_at = "2022-07-18 05:55:05"
        assert controller_date.define_date_query() == {'created_date': {'$lt': datetime(2022, 7, 18, 5, 55, 5),
                                                                        '$gte': datetime(2022, 7, 18, 4, 55, 5)
                                                                        }
                                                       }
        """Just end at informed"""
        controller_date.start_at = None
        assert controller_date.define_date_query() == {'created_date': {'$lt': datetime(2022, 7, 18, 5, 55, 5)}}

        """Just start at informed"""
        controller_date.start_at = "2022-07-18 04:55:05"
        controller_date.end_at = None
        assert controller_date.define_date_query() == {'created_date': {'$gte': datetime(2022, 7, 18, 4, 55, 5)}}

    def test_define_date_query_none(self):
        controller_date = self.controller_success
        controller_date.start_at = None
        controller_date.end_at = None
        assert controller_date.define_date_query() is None

    def test_home_page_success(self):
        controller = HomeController(user='{"username": "usertest1"}', page=1,
                                    post_from='only-mine', start_at=None, end_at=None)
        home_page = controller.home_page()
        assert home_page['body']['profile']
        assert home_page['body']['posts']
        assert len(home_page['body']['posts']) == 10

    def test_home_page_failed(self):
        controller = HomeController(user='{"a": "usertest1"}', page=1,
                                    post_from='only-mine', start_at=None, end_at=None)
        home_page = controller.home_page()
        assert home_page[0]['body']['error']
        assert home_page[1] == 500
