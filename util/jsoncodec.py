#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '4/27/2016 10:28:48'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import json


class JsonEnc(json.JSONEncoder, object):
    """
    encode data to json via json.JSONEncoder
    """

    def default(self, obj):
        # convert object to a dict
        dict = {}
        dict['__class__'] = obj.__class__.__name__
        dict['__module__'] = obj.__module__
        dict.update(obj.__dict__)
        return dict


class JsonDec(json.JSONDecoder, object):
    """
    decode data from json via json.JSONDecoder
    """

    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict2obj)

    def dict2obj(self, dict):
        # convert dict to object
        if '__class__' in dict:
            class_name = dict.pop('__class__')
            module_name = dict.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            args = dict((key.encode('ascii'), value) for
                        key, value in dict.items())  # get args
            inst = class_(**args)  # create new instance
        else:
            inst = dict
        return inst
