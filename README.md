# Posterr

Made with Flask, MongoDB and Docker. Dockerfile is also available to make docker image and docker containers.

# Project Description

## Overview

Social media application called Posterr. Posterr is very similar to Twitter, but it has far fewer features.

Posterr only has two pages, the homepage, and the user profile page, which are described below. Other data and actions are also detailed below. 

### Pages

**Homepage**

- The homepage, by default, will show a feed of posts (including reposts and quote posts), starting with the latest 10 posts. Older posts are loaded on-demand on chunks of 10 posts whenever the user scrolling reaches the bottom of the page.
- There is a toggle switch "All / Only mine" that allows you to switch between seeing all posts and just posts you wrote. For both views, all kinds of posts are expected on the feed (original posts, reposts, and quote posts).
- There is a date range filter option (start date and end date) that allows results filtering based on the posted date, both values are optional: e.g user may want to filter only posts after a certain date without defining a limit date.
- New posts can be written from this page.

**User profile page**

- Shows data about the user:
    - Username
    - Date joined Posterr, formatted as such: "March 25, 2021"
    - Count of number of posts the user has made (including reposts and quote posts)
- Shows a feed of the posts the user has made (including reposts and quote posts), starting with the latest 5 posts. Older posts are loaded on-demand when the user clicks on a button at the bottom of the page labeled "show more".
- New posts can be written from this page: for this assessment, when writing a post from the profile screen, the profile user should be set as the author of the new content.
### More Details

**Users**

- Only alphanumeric characters can be used for username
- Maximum 14 characters for username
- Usernames should be unique values

**Posts**

Posts are the equivalent of Twitter's tweets. They are text-only, user-generated content. Users can write original posts and interact with other users' posts by reposting or quote-posting. For this project, you should implement all three — original posts, reposts, and quote-posting

- A user is not allowed to post more than 5 posts in one day (including reposts and quote posts)
- Posts can have a maximum of 777 characters
- Users cannot update or delete their posts
- Reposting: Users can repost other users' posts (like Twitter Retweet), limited to original posts and quote posts (not reposts)
- Quote-post: Users can repost other user's posts and leave a comment along with it (like Twitter Quote Tweet) limited to original and reposts (not quote-posts)

# Build proccess
My name is Gabriel, So I'll explain how I thought to build this project:
```
       On the first step I was thinking something to have good Performance and be Scalable 
       and "What the data the project will need and how I will have the control ?"
    So, with these thinking I Decided to use a NoSql Database even the data talk each other, I think could be 
    a good Ideia because, if in a near future need implements something new will not be a problem to new changes 
    considering the quantity of users and posts.
    And thinking this, below is the DataBase Modeling
```
## Database Modeling
![Screenshot](posterr_database.jpg)

```
After create Database Modeling.
        Now it's time to decide the architecture. This is one of the hard choices to do, because this decision will
    reflect also the performance, understanding and scalability of the project. 
    Then to serve these requirements, I decided use concepts of Clean Architecture, as the project is not something with big rules and 
    implementations and fits the needs.
```


## Built using :
```sh
	Flask : Python Based mini-Webframework
	MongoDB : Database Server
	Pymongo : Database Connector ( For creating connectiong between MongoDB and Flask )
```

## Set up environment for using this repo (ubuntu, Mac, Win):
```
Install Python ( If you don't have already )
	$ sudo apt-get install python
Install MongoDB ( Make sure you install it properly )
	$ sudo apt install -y mongodb

Windows:
    Install Python 3.9 from https://www.python.org/downloads/

    Install MongoDB from https://docs.docker.com/desktop/install/windows-install/

    Install MongoDB from https://www.mongodb.com/docs/manual/tutorial/install-mongodb-on-windows/
    
    
In Windows use Git bash: https://git-scm.com/downloads
Install Dependencies of the application
    in root project:
    $ py -m pip install virtualenv
    $ py -m venv venv
    
    Active venv
    windows: source venv/Scripts/activate
    linux: source venv/bin/activate
    
    Then:
    $ pip install -r app/requirements.txt
```

## Run the application
```
On Linux/Mac (in windows if you follow the tutorial in mongo website, will start when turn on your computer):
Start MongoDB
	$ sudo service mongod start
Start Docker
    $ sudo service docker start    

Start Application:
    $ docker-compose build
    $ docker-compose up
    if you don't want to see the logs run ( docker-compose up -d)
Stop Application:
    $ CTRL + C or docker-compose down
```

## Run the Unnit tests

```
After Start Application:
    $ docker exec -it posterr_web pytest
```

## Makefile

```
If you prefere you can prepare environment and use project by make commands:
Commands
    $ make setup
    $ make build
    $ make up
    $ make down
```

## Collection Postman
```
The file Posterr.postman_collection.json is a postman collection
Import the file in your postman for real tests

Important: For all get requisitions we pass the user on header
Folder - Profile
            - Get Profile you can paginate(See the params)
            - Create Profile
            - Create Post From Profile
       - Home
            - Home (params to page)
            - Home Only-Mine(with params to only mine)(See the params)
            - Home with date_range [Dates must be Like '2022-07-17 00:00:00' or '2022-07-17'] (See the params)
            - Create Post From Home
       - Post
            - Create post
            - Create repost
            - Create quote-post
           
 
Dates must be Like '2022-07-17 00:00:00' or '2022-07-17'

If page not informed we pass the lastest 10

About the scrolling HomePage/Profile. I did thinking on in front-end requests, 
whenever the user reaches the bottom of page so it pass the param page.
```
