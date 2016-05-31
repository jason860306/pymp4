#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '6/12/0012 16:05:15'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from pymp4def import *


class Track:
    """
    a video or audio sequence
    """

    def __init__(self, type=VideTrackType):
        self.type = type
        self.samples = []

    def get_samples(self):
        return self.samples

    def append_sample(self, sample):
        self.samples.append(sample)

    def __str__(self):
        logstr = "type = %s, samples = [" % (self.type)
        for sample in self.samples:
            logstr += "%d. %s" % (sample.index, sample)
        logstr += "]"
        return logstr
