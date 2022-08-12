#!/usr/bin/python3
'''Define base class.'''
import json


class Base:
    '''private class attribute: _nb_objects.
    class constructor attribute.
    '''
    __nb_objects = 0

    def __init__(self, id=None):
        '''assign the public instance attribute id with argument value.
        Args:
            id (int): id attribute.
        '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    def to_json_string(list_dictionaries):
        '''returns the JSON string representation of dictionaries.
        Args:
            list_dictionaries (dict): a list of dictionaries.
        '''
        if list_dictionaries is None:
            return '[]'
        return json.dumps(list_dictionaries)
