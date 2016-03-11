#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/11/16 5:09 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from box import *
from filestream import *


class Root():
    """
    the root box of a mp4 file
    """

    def __init__(self):
        self.moov = None
        self.ftyp = None
        self.mdat = None
        self.free = None
        self.skip = None
        self.udat = None

    def decode(self, file=None):
        file_strm = None
        if file:
            file_strm = FileStream(file)

        tmp_box = Box()
        file_strm = tmp_box.decode(file)

        if tmp_box.type == FourCCMp4Moov:
            self.moov = MP4Boxes[tmp_box.type](tmp_box)
            file_strm = self.moov.decode(file)
        elif tmp_box.type == FourCCMp4Ftyp:
            self.ftyp = MP4Boxes[tmp_box.type](tmp_box)
            file_strm = self.ftyp.decode(file)
        elif tmp_box.type == FourCCMp4Mdat:
            self.mdat = MP4Boxes[tmp_box.type](tmp_box)
            file_strm = self.mdat.decode(file)
        elif tmp_box.type == FourCCMp4Udat:
            self.udat = MP4Boxes[tmp_box.type](tmp_box)
            file_strm = self.udat.decode(file)
        elif tmp_box.type == FourCCMp4Free:
            self.free = MP4Boxes[tmp_box.type](tmp_box)
            file_strm = self.free.decode(file)
        elif tmp_box.type == FourCCMp4Skip:
            self.skip = MP4Boxes[tmp_box.type](tmp_box)
            file_strm = self.skip.decode(file)

        return file_strm

    def __str__(self):
        logstr = "moov = %s, ftyp = %s, mdat = %s, free = %s, " \
                 "skip = %s, udat = %s" % \
                 (self.moov, self.ftyp, self.mdat, self.free,
                  self.skip, self.udat)
        return logstr
