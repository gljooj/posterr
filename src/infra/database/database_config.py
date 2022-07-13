import pymongo


def setUp():
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    db = myclient['posterr']

    create_user(db['user'])
    post = create_post(db['post']) or None
    create_comment(db['comment'], post.inserted_id if post else None)


def create_user(user_collection):
    if user_collection.find_one({"username": "gabtest"}):
        return print("You have already created user")
    return user_collection.insert_one({"username": "gabtest", "joined_at": "2022-07-11 10:25:54"})


def create_post(post_collection):
    if post_collection.find_one({"type": "post",
                                 "username": "gabtest", "text": "first", "date": "2022-07-12 15:07:35"}):
        return print("You have already created first post")
    return post_collection.insert_one({"type": "post", "username": "gabtest", "text": "first",
                                       "date": "2022-07-12 15:07:35"})


def create_comment(comment_collection, post_id):
    if comment_collection.find_one({"post_id": post_id}):
        return print("You have already created comment")
    return comment_collection.insert_one({"post_id": post_id, "username": "gabtest",
                                          "joined_at": "2022-07-11 10:25:54"})

