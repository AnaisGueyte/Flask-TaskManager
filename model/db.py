from mongoengine import *
from flask_login import UserMixin


connect('todolist', host='localhost', port=27017)

class Task(Document):
    name = StringField(required=True)
    user = ReferenceField('User')
    assignee = ReferenceField('User')
    date = DateTimeField(required=True)

    # def validate(self, clean=True):
    # super(Task, self).validate(clean=clean)



class User(Document, UserMixin):
    pseudo = StringField(required=True, unique=True)
    password = StringField(required=True)

    def validate(self, clean=True):
        super(User, self).validate(clean=clean)

