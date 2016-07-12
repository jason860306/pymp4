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


from boxes.box import *
from mp4boxes import *
from sample import *
from track import *


class Root(object):
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

        if file_strm is None or 0 == file_size:
            pass  # raise
        self.file_strm = file_strm
        self.file_size = file_size

        self.tracks = []

    def get_major_brand(self):
        return "h264" if self.ftyp is None else self.ftyp.major_brand

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
                file_strm_.seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            fsize -= tmp_box.Size()
        return file_strm_

    def rebuild_sample_table(self):
        TrackType = [VideTrackType, SounTrackType, HintTrackType]
        for trk_type in TrackType:
            if self.moov.get_track(trk_type) is None:
                continue
            track = Track(trk_type)

            sample_idx = 0
            chunk_offset_lst = self.moov.get_chunk_offset_list()
            for i in range(len(chunk_offset_lst)):
                sample_per_chunk = self.moov.get_sample_per_chunk(i, trk_type)
                for j in range(sample_per_chunk):
                    sample = None
                    if trk_type == VideTrackType:
                        sample = VideoSample()
                    elif trk_type == SounTrackType:
                        sample = AudioSample()
                    if sample is None:
                        continue
                    sample.index = sample_idx
                    sample_idx += 1

                    sample.offset, sample.size = \
                        self.moov.get_sample(i, sample.index, trk_type)
                    sample.duration = \
                        self.moov.get_sample_duration(sample.index, trk_type)

                    track.append_sample(sample)

                    print sample
            self.tracks.append(track)

    def get_tracks(self):
        return self.tracks

    def write_es_header(self):
        sps = self.moov.get_sps(VideTrackType)
        pps = self.moov.get_pps(VideTrackType)
        spse = self.moov.get_spse(VideTrackType)

    def get_sample_data_by_time(self, utc_timestamp, track_type=VideTrackType):
        if self.moov is None:
            pass  # raise
        return self.moov.get_sample_data_by_time(self.file_strm, utc_timestamp, track_type)

    def get_sample_data(self, offset, size, file_strm, track_type=VideTrackType):
        if self.moov is None:
            pass  # raise
        return self.moov.get_sample_data(offset, size, self.file_strm, track_type)

    def write_es_tailer(self):
        return ''

    def get_meta_data(self):
        if self.moov is None or self.ftyp is None:
            pass  # raise
        meta_data = {}

        general = {}
        general['major_brand'] = '' if (self.ftyp is None) else self.ftyp.major_brand
        general['minor_brand'] = '' if (self.ftyp is None) else self.ftyp.minor_brand
        general['compatible_brands'] = '' if (self.ftyp is None) else self.ftyp.compatible_brands
        general.update(self.moov.get_general_meta_data())
        video_meta_data = self.moov.get_vide_meta_data()
        sound_meta_data = self.moov.get_soun_meta_data()

        meta_data['general'] = general
        meta_data['video'] = video_meta_data
        meta_data['audio'] = sound_meta_data

        return meta_data

    def get_sps(self, track_type=VideTrackType):
        return None if (self.moov is None) else self.moov.get_sps(track_type)

    def get_pps(self, track_type=VideTrackType):
        return None if (self.moov is None) else self.moov.get_pps(track_type)

    def get_spse(self, track_type=VideTrackType):
        return None if (self.moov is None) else self.moov.get_spse(track_type)

    def get_nal_len_size(self, track_type=VideTrackType):
        return 0 if self.moov is None else self.moov.get_nal_len_size(track_type)

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
