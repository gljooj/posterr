from datetime import datetime


class PostObject:
    def __init__(self, post: dict, user: dict):
        self.post = post
        self.user = user


class UserObject:
    def __init__(self, username: str, joined_at: datetime):
        self.username = username
        self.joined_at = joined_at
