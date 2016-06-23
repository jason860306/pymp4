#!/usr/bin/python
# encoding: utf-8

"""

"""
from util.util import Util

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/1 17:22'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import mp4boxes
from box import *


class Moov(Box):
    """
    aligned(8) class MovieBox extends Box(‘moov’){
    }
    """

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)

        self.mvhd = None
        self.trak = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = self.Size() - self.GetLength()
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Mvhd:
                self.mvhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mvhd.decode(file_strm)
                self.offset += self.mvhd.Size()
            elif tmp_box.type == FourCCMp4Trak:
                trak_ = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = trak_.decode(file_strm)
                self.offset += trak_.Size()
                self.trak.append(trak_)
            elif tmp_box.type == FourCCMp4Mdia:
                self.mdia = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mdia.decode(file_strm)
                self.offset += self.mdia.Size()
            else:
                file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        return file_strm

    def duration(self):
        return self.mvhd.movie_duration()

    def track_bitsize(self, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return 0 if (trk is None) else trk.bitsize()

    def track_duration(self, track_type=VideTrackType):
        trk = self.get_track(track_type)
        if self.mvhd is None:
            return 0.0
        duration_ = trk.track_duration() / self.mvhd.timescale
        return duration_

    def track_bitrate(self, track_type=VideTrackType):
        track_bsize = self.track_bitsize(track_type)
        track_duration = self.track_duration(track_type)
        return 0.0 if (0 == track_duration) else (track_bsize / track_duration)

    def width(self):
        trk = self.get_track(VideTrackType)
        return trk.width()

    def height(self):
        trk = self.get_track(VideTrackType)
        return trk.height()

    def fps(self):
        duration_ = self.track_duration(VideTrackType)
        sample_count_ = self.get_track(VideTrackType).sample_count()
        return 0.0 if (duration_) == 0 else (1.0 * sample_count_ / duration_)

    def bitrate(self):
        bsize = 0
        duration_ = self.mvhd.movie_duration()
        for trk in self.trak:
            bsize += trk.bitsize()
        return 0.0 if (duration_ == 0) else (1.0 * bsize / duration_)

    def find_sample_index(self, utc_timestamp, track_type=VideTrackType):
        mp4_timestamp = self.utc2mp4_timestamp(utc_timestamp)
        trk = self.get_track(track_type)
        return trk.find_sample_index(mp4_timestamp)

    def get_sample_duration(self, sample_idx, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return trk.get_sample_duration(sample_idx)

    def get_sample_size(self, sample_index, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return trk.get_sample_size(sample_index)

    def find_chunk_index(self, sample_index, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return trk.find_chunk_index(sample_index)

    def chunk_last_sample_index(self, chunk_index, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return trk.chunk_last_sample_index(chunk_index)

    def chunk_offset(self, chunk_idx, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return trk.chunk_offset(chunk_idx)

    def get_chunk_offset_list(self, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return trk.get_chunk_offset_list()

    def get_sample_per_chunk(self, chunk_idx, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return trk.get_sample_per_chunk(chunk_idx)

    def get_sps(self, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return None if (trk is None) else trk.get_sps()

    def get_pps(self, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return None if (trk is None) else trk.get_pps()

    def get_spse(self, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return None if (trk is None) else trk.get_spse()

    def get_nal_len_size(self, track_type=VideTrackType):
        trk = self.get_track(track_type)
        return 0 if trk is None else trk.get_nal_len_size()

    # def get_sample(self, sample_index, track_type=VideTrackType):
    #     trk = self.get_track(track_type)
    #     chunk_idx = trk.find_chunk_index(sample_index)
    #     if len(chunk_idx) < 0:
    #         pass  # raise
    #     chunk_idx = chunk_idx.keys[0]
    #     samples_idx = chunk_idx.values[0]
    #     data_offset = chunk_offset = trk.chunk_offset(chunk_idx)
    #     for i in range(len(samples_idx) - 1):
    #         sample_size = trk.get_sample_size(samples_idx[i])
    #         data_offset += sample_size
    #     data_size = trk.get_sample_size(samples_idx[-1])
    #     return data_offset, data_size

    def get_sample(self, chunk_idx, sample_idx, track_type=VideTrackType):
        trk = self.get_track(track_type)
        chunk_offset_lst = self.get_chunk_offset_list(track_type)
        if chunk_idx >= len(chunk_offset_lst):
            pass  # raise
        chunk_offset = chunk_offset_lst[chunk_idx]
        sample_offset = chunk_offset
        for idx in trk.chunk_sample_index_diff(chunk_idx, sample_idx):
            sample_offset += trk.get_sample_size(idx)
        sample_size = trk.get_sample_size(sample_idx)
        return sample_offset, sample_size

    def get_sample_data_by_time(self, file_strm, utc_timestamp, track_type=VideTrackType):
        mp4_timestamp = self.utc2mp4_timestamp(utc_timestamp)

        trk = self.get_track(track_type)
        sample_index = trk.find_sample_index(mp4_timestamp)
        data_offset, data_size = self.get_sample(sample_index, track_type)
        if file_strm is None:
            print "file_strm is None"
            return file_strm
        offset_ = file_strm.tell()
        file_strm.seek(data_offset, os.SEEK_SET)
        data = file_strm.read_byte(data_size)
        file_strm.seek(offset_, os.SEEK_SET)
        return data

    def get_sample_data(self, offset, size, file_strm, track_type=VideTrackType):
        if file_strm is None:
            print "file_strm is None"
            return file_strm
        offset_ = file_strm.tell()
        file_strm.seek(offset, os.SEEK_SET)
        data = file_strm.read_byte(size)
        file_strm.seek(offset_, os.SEEK_SET)
        return data

    def find_sync_sample_index(self, utc_timestamp, track_type=VideTrackType):
        mp4_timestamp = self.utc2mp4_timestamp(utc_timestamp)
        trk = self.get_track(track_type)
        sample_index = trk.find_sample_index(mp4_timestamp)
        sync_sample_index = trk.find_sync_sample_index(sample_index)
        return sync_sample_index

    def get_sync_sample_data(self, file_strm, utc_timestamp, track_type=VideTrackType):
        sync_sample_index = self.find_sync_sample_index(utc_timestamp, track_type)
        data_offset, data_size = self.get_sample(sync_sample_index, track_type)
        if file_strm is None:
            print "file_strm is None"
            return file_strm
        file_strm.seek(data_offset, os.SEEK_SET)
        return file_strm.read_byte(data_size)

    def get_general_meta_data(self):
        general = {}
        general['creation_time'] = UTC_NONE_TIME if (self.mvhd is None) else \
            self.mvhd.creation_time_fmt
        general['modify_time'] = UTC_NONE_TIME if (self.mvhd is None) else \
            self.mvhd.modification_time_fmt
        duration_ = self.duration()
        general['duration'] = Util.time_format(duration_)
        general['bitrate'] = self.bitrate()
        return general

    def get_vide_meta_data(self):
        video = {}
        trk = self.get_track(VideTrackType)
        if trk is None:
            return video
        video['ID'] = trk.track_id()
        duration_ = self.track_duration(VideTrackType)
        video['duration'] = Util.time_format(duration_)
        video['bitrate'] = self.track_bitrate(VideTrackType)
        video['width'] = trk.width()
        video['height'] = trk.height()
        video['fps'] = self.fps()
        video['create_time'] = trk.create_time()
        video['modify_time'] = trk.modify_time()
        return video

    def get_soun_meta_data(self):
        sound = {}
        trk = self.get_track(SounTrackType)
        if trk is None:
            return sound
        sound['ID'] = trk.track_id()
        duration_ = self.track_duration(SounTrackType)
        sound['duration'] = Util.time_format(duration_)
        sound['bitrate'] = self.track_bitrate(SounTrackType)
        sound['fps'] = self.fps()
        sound['create_time'] = trk.create_time()
        sound['modify_time'] = trk.modify_time()
        return sound

    def get_track(self, track_type=VideTrackType):
        for trk in self.trak:
            if trk.mediatype() == track_type:
                return trk
        else:
            pass  # raise

    def utc2mp4_timestamp(self, utc_timestamp):
        mp4_timestamp = utc_timestamp + UTC_MP4_INTERVAL
        return mp4_timestamp

    def dump(self):
        dump_info = Box.dump(self)
        if None != self.mvhd:
            dump_info[self.mvhd.type] = self.mvhd.dump()
        if None != self.trak:
            for trk in self.trak:
                trk_key = '{0}_{1}'.format(trk.mediatype(), trk.type)
                dump_info[trk_key] = trk.dump()
        return dump_info

    def __str__(self):
        logstr = "%s\n%s\n" % (Box.__str__(self), self.mvhd)
        for i in range(len(self.trak)):
            logstr += "\t%08ld. %s" % (i, self.trak[i])
        logstr += "\n"
        return logstr
