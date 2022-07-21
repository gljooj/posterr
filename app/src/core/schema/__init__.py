from datetime import datetime


def iterable(cls):
    def iterfn(self):
        iters = dict((x, y) for x, y in cls.__dict__.items() if x[:2] != '__')
        iters.update(self.__dict__)

        for x, y in iters.items():
            yield x, y

    cls.__iter__ = iterfn
    return cls


@iterable
class PostObject:
    def __init__(self, post: dict, user: dict):
        self.post = post
        self.user = user


@iterable
class UserObject:
    def __init__(self, username: str, joined_at: datetime):
        self.username = username
        self.joined_at = joined_at
