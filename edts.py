#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 15:56'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class Edts(Box):
    """
    aligned(8) class EditBox extends Box(‘edts’) {
    }
    """

    def __init__(self):
        Box.__init__(self)

    def decode(self, file=None):
        Box.decode(self, file)

    def __str__(self):
        logstr = "%s" % Box.__str__(self)
        return logstr
