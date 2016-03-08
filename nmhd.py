#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/2 18:17'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *


class Nmhd(FullBox):
    """
    aligned(8) class NullMediaHeaderBox
        extends FullBox(’nmhd’, version = 0, flags) {
    }
    """

    def __init__(self):
        FullBox.__init__(self)

    def decode(self, file=None):
        FullBox.decode(self, file)

    def __str__(self):
        logstr = "%s" % FullBox.__str__(self)
        return logstr
