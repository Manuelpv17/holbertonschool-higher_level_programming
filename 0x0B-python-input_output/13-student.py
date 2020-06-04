#!/usr/bin/python3
""" Student to JSON
    """


class Student:
    """class Student that defines a student
        """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        new_dict = {}
        if type(attrs) is not list:
            return self.__dict__
        for key, val in self.__dict__.items():
            if key in attrs:
                new_dict[key] = val
        return new_dict

    def reload_from_json(self, json):
        for key, val in json.items():
            self.__dict__[key] = val
