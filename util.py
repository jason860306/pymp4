#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '4/26/0026 16:54:04'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from datetime import *


class Util:
    """

    """

    @staticmethod
    def time_format(utc_time=None):
        return datetime.fromtimestamp(utc_time).strftime(
            "UTC %Y-%m-%d %H:%M:%S")
