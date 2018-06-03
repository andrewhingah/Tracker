import datetime

from marshmallow import Schema, fields, post_load

user_requests = [

    {'user1':['car', 'engine replacement']},
    {'user2':['iphone7', 'black screen']},
    {'user3':['house112', 'painting']},
    {'user4':['windows 10 laptops', 'windows updates and virus protection']}
    
]

class UserRequest(object):
    def __init__(self, description, fault, created_at):
        self.description = description
        self.fault = fault
        self.created_at = datetime.datetime.now()

    def __repr__(self):
        return '<UserRequest(name={self.description!r})>'.format(self=self)

class UserRequestSchema(Schema):
    description = fields.Str()
    fault = fields.Str()
    created_at = fields.Date()

    @post_load
    def make_maintenance(self, data):
        return UserRequest(**data)