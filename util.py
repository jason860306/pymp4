#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '4/26/2016 16:54:04'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import time
from datetime import *


class Util:
    """

    """

    @staticmethod
    def datetime_format(utc_time=None):
        return datetime.fromtimestamp(utc_time).strftime(
            "UTC %Y-%m-%d %H:%M:%S")

    @staticmethod
    def time_format(seconds=None):
        return time.strftime("%H:%M:%S", time.gmtime(seconds))

    __tab_num = 1
    __dict_len = 0

    @staticmethod
    def dump_dict(d=None):
        dump_str = ""
        if None == d:
            return dump_str
        idx = 0
        for k, v in d.items():
            if isinstance(v, dict):
                Util.__dict_len = len(v)  # 子字典的长度
                Util.__tab_num += 1
                dump_str += "\t%s:\n%s" % (k, Util.dump_dict(v))
            else:
                dump_str += "\t" * Util.__tab_num + "{0} = {1}\n".format(k, v)
                idx += 1
                if idx == Util.__dict_len:
                    Util.__tab_num -= 1  # 子字典遍历完要将tab数据减1
        return dump_str
