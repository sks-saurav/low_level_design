"""
Requirement:
[x] User add information to profile
[x] User can search and view pages gropus and other users
[x] send and cancel connection req
[x] follow other without adding them to connection
[x] view # of conn, pofile view, post impression, search apperience
[] request and give recommendation to user
[] write new post
[x] react and comment on post
[x] react and comment on existing comment
[x] send receive message from other user
[] notification to user to inform them about messages, connection req or comment on post
[x] follow company pages
[x] create and join group
"""
from enum import Enum
from typing import Dict, List, Optional


class JobStatus(Enum):
    OPENTOWORK = 0
    HIRING = 1


class RequestStatus(Enum):
    ACCEPTED = 1
    PENDING = 2
    DECLINED = 3


class User:
    def __init__(self, id: str, name: str):
        self.__id = id
        self.name = name
        self.description = None
        self.experience = []
        self.education = []
        self.post = []
        self.status = None
        self.connection = []
        self.following = []
        self.sent_requests = []
        self.received_reuqest = []
        self.search_apperance = 0
        self.profile_view = 0
        self.groups = []


class Request:
    def __init__(self):
        self.name = None
        self.status = None
        self.date = None


class Institution:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__start_date = None
        self.__end_date = None
        self.description = None


class Pages:
    def __init__(self):
        self.__id = id
        self.__user = None
        self.__content = None
        self.__followers = []


class Reaction(Enum):
    LIKE = 0
    CELEBRATE = 1
    LOVE = 2
    HAHA = 3
    SAD = 4


class Comments:
    def __init__(self, id, user, content):
        self.__id = id
        self.__user = user
        self.__content = content
        self.reactions: Dict[Reaction] = {}
        self.comment: List[Comments] = None


class Post:
    def __init__(self, id):
        self.__id = id
        self.content = None
        self.comments: Optional[List[Comments]] = None
        self.reactions = {}


class Group:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name
        self.__member: Optional[List[User]] = None
        self.__posts: List[Post] = []

    def join_group(self, user):
        self.__member.append(user)


class Message:
    def __init__(self):
        self.__id = id
        self.__from = None
        self.__to = None
        self.__content = None



