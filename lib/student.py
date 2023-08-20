#!/usr/bin/env python

from user import User

class Student(User):

    knowledge = []

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        pass
    
    def learn(self, info):
        self.knowledge.append(info)
        pass