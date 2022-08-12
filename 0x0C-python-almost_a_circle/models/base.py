#!/usr/bin/python3
'''Define base class.'''

import json
import io


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

    @staticmethod
    def to_json_string(list_dictionaries):
        '''returns the json string representation of dictionaries.
        Args:
            list_dictionaries : a list of dictionaries.
        Returs:
            json string representation
        '''
        if list_dictionaries is None:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''writes the json string representation of list_objs to a file'''
        new_l = []
        if list_objs is not None:
            for i in list_objs:
                new_l.append(cls.to_dictionary(i))
        filename = cls.__name__ + '.json'
        with open(filename, 'w') as f:
            f.write(cls.to_json_string(new_l))

    def from_json_string(json_string):
        '''returns the list of the json string representation json_string'''
        if json_string is None:
            return '[]'
        else:
            return json.loads(json_string)
