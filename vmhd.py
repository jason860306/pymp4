#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # user
__date__ = '2016/3/4 22:39'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *


class Vmhd(Box):
    """
    aligned(8) class VideoMediaHeaderBox extends FullBox(‘vmhd’, version = 0, 1) {
        template unsigned int(16) graphicsmode = 0; // copy, see below
        template unsigned int(16)[3] opcolor = {0, 0, 0};
    }
    """

    def __init__(self):
        Box.__init__(self)

        self.graphocsmode = 0
        self.opcolor = [0 for i in range(3)]

    def decode(self, file=None):
        Box.decode(self, file)

        file_strm = Util(file)

        self.graphocsmode = file_strm.read_uint16_lit()
        for i in range(len(self.opcolor)):
            self.opcolor[i] = file_strm.read_uint16_lit()

    def __str__(self):
        logstr = "%s, graphicsmode = %d, opcolor = [" % \
                 (Box.__str__(self), self.graphocsmode)
        for opcolor_ in self.opcolor:
            logstr += "%s, " % opcolor_
        logstr += "]"
        return logstr
