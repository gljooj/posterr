from datetime import datetime

from src.controller.home_controller import HomeController


class TestHomeController:
    controller_success = HomeController(user="{'username': 'test'}", page=1,
                                        post_from='only-mine', start_at=None, end_at=None)

    def test_define_query_success(self):
        assert self.controller_success.define_query() == "{'username': 'test'}"

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

