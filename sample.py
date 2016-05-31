#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '6/12/2016 15:38:26'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"


# '$Source$'


class Sample:
    """
    base class for video frame and audio sample.
    """

    def __init__(self):
        self.index = 0
        self.offset = 0
        self.size = 0
        self.duration = 0

    def __str__(self):
        logstr = "index = %d, offset = %d, size = %d, duration = %d" % \
                 (self.index, self.offset, self.size, self.duration)
        return logstr


class VideoSample(Sample):
    """
    a video frame
    """

    def __init__(self):
        Sample.__init__(self)

    def __str__(self):
        logstr = "%s" % (Sample.__str__(self))
        return logstr


class AudioSample(Sample):
    """
    a audio sample
    """

    def __init__(self):
        Sample.__init__(self)

    def __str__(self):
        logstr = "%s" % (Sample.__str__(self))
        return logstr
