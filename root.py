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
from mp4boxes import *


class Root:
    """
    the root box of a mp4 file
    """

    def __init__(self, offset=0):
        self.offset = offset

        self.moov = None
        self.ftyp = None
        self.mdat = None
        self.free = None
        self.skip = None
        self.udat = None

    def decode(self, filename):
        if filename is None:
            print "file is None"
            return

        filesize = os.path.getsize(filename)

        with open(filename, 'rb') as mp4_file:
            file_strm = FileStream(mp4_file)
            while filesize > 0:
                tmp_box = Box()
                file_strm = tmp_box.peek(file_strm)
                if tmp_box.type == FourCCMp4Moov:
                    self.moov = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                    file_strm = self.moov.decode(file_strm)
                    self.offset += self.moov.Size()
                elif tmp_box.type == FourCCMp4Ftyp:
                    self.ftyp = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                    file_strm = self.ftyp.decode(file_strm)
                    self.offset += self.ftyp.Size()
                elif tmp_box.type == FourCCMp4Mdat:
                    self.mdat = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                    file_strm = self.mdat.decode(file_strm)
                    self.offset += self.mdat.Size()
                elif tmp_box.type == FourCCMp4Udat:
                    self.udat = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                    file_strm = self.udat.decode(file_strm)
                    self.offset += self.udat.Size()
                elif tmp_box.type == FourCCMp4Free:
                    self.free = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                    file_strm = self.free.decode(file_strm)
                    self.offset += self.free.Size()
                elif tmp_box.type == FourCCMp4Skip:
                    self.skip = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                    file_strm = self.skip.decode(file_strm)
                    self.offset += self.skip.Size()
                else:
                    file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
                    self.offset += tmp_box.Size()
                filesize -= tmp_box.Size()

            return file_strm

    def __str__(self):
        logstr = "moov = %s, ftyp = %s, mdat = %s, free = %s, " \
                 "skip = %s, udat = %s" % \
                 (self.moov, self.ftyp, self.mdat, self.free,
                  self.skip, self.udat)
        return logstr
