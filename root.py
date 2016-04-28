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

    def __init__(self, file_strm, file_size, offset=0):
        self.box_offset = offset
        self.offset = offset

        self.moov = None
        self.ftyp = None
        self.mdat = None
        self.free = None
        self.skip = None
        self.udat = None

        if file_strm == None or 0 == file_size:
            pass  # raise
        self.file_strm = file_strm
        self.file_size = file_size

    def decode(self):
        fsize = self.file_size
        file_strm_ = self.file_strm
        while fsize > 0:
            tmp_box = Box()
            file_strm_ = tmp_box.peek(file_strm_)
            if tmp_box.type == FourCCMp4Moov:
                self.moov = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm_ = self.moov.decode(file_strm_)
                self.offset += self.moov.Size()
            elif tmp_box.type == FourCCMp4Ftyp:
                self.ftyp = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm_ = self.ftyp.decode(file_strm_)
                self.offset += self.ftyp.Size()
            elif tmp_box.type == FourCCMp4Mdat:
                self.mdat = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm_ = self.mdat.decode(file_strm_)
                self.offset += self.mdat.Size()
            elif tmp_box.type == FourCCMp4Udta:
                self.udat = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm_ = self.udat.decode(file_strm_)
                self.offset += self.udat.Size()
            elif tmp_box.type == FourCCMp4Free:
                self.free = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm_ = self.free.decode(file_strm_)
                self.offset += self.free.Size()
            elif tmp_box.type == FourCCMp4Skip:
                self.skip = MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm_ = self.skip.decode(file_strm_)
                self.offset += self.skip.Size()
            else:
                file_strm_.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            fsize -= tmp_box.Size()
        return file_strm_

    def get_sample_data(self, utc_timestamp, track_type=VideTrackType):
        if None == self.moov:
            pass  # raise
        return self.moov.get_sample_data(self.file_strm, utc_timestamp, track_type)

    def get_meta_data(self):
        if None == self.moov or None == self.ftyp:
            pass  # raise
        meta_data = {}

        general = {}
        general['major_brand'] = '' if (self.ftyp == None) else self.ftyp.major_brand
        general['minor_brand'] = '' if (self.ftyp == None) else self.ftyp.minor_brand
        general['compatible_brands'] = '' if (self.ftyp == None) else self.ftyp.compatible_brands
        general.update(self.moov.get_general_meta_data())
        video_meta_data = self.moov.get_vide_meta_data()
        sound_meta_data = self.moov.get_soun_meta_data()

        meta_data['general'] = general
        meta_data['video'] = video_meta_data
        meta_data['audio'] = sound_meta_data

        return meta_data

    def dump(self):
        dump_info = {}
        if None != self.moov:
            dump_info['moov'] = self.moov.dump()
        if None != self.ftyp:
            dump_info['ftyp'] = self.ftyp.dump()
        if None != self.mdat:
            dump_info['mdat'] = self.mdat.dump()
        if None != self.free:
            dump_info['free'] = self.free.dump()
        if None != self.skip:
            dump_info['skip'] = self.skip.dump()
        if None != self.udat:
            dump_info['udat'] = self.udat.dump()
        return dump_info

    def __str__(self):
        logstr = "%s\n%s\n%s\n%s\n%s\n%s" % \
                 (self.moov, self.ftyp, self.mdat, self.free,
                  self.skip, self.udat)
        return logstr
