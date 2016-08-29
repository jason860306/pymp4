#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:57:03'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


import mp4boxes
from sample_entry import *


class Mp4s(object, SampeEntry):
    """
    5.6.1 Syntax
    aligned(8) class Esds extends FullBox(‘esds’, version = 0, 0) {
        ES_Descriptor ES;
    }
    // Visual Streams
    class MP4VisualSampleEntry() extends VisualSampleEntry ('mp4v'){
        Esds ES;
    }
    // Audio Streams
    class MP4AudioSampleEntry() extends AudioSampleEntry ('mp4a'){
        Esds ES;
    }
    // all other Mpeg stream types
    class MpegSampleEntry() extends SampleEntry ('mp4s'){
        Esds ES;
    }
    aligned(8) class SampleDescriptionBox (unsigned int(32) handler_type)
        extends FullBox('stsd', 0, 0){
        int i ;
        unsigned int(32) entry_count;
        for (i = 0 ; i < entry_count ; i++){
            switch (handler_type){
                case ‘soun’: // AudioStream
                    AudioSampleEntry();
                    break;
                case ‘vide’: // VisualStream
                    VisualSampleEntry();
                    break;
                case ‘hint’: // Hint track
                    HintSampleEntbry();
                    break;
                default :
                    MpegSampleEntry();
                    break;
            }
        }
    }

    5.6.2 Semantics
    Entry_count — is an integer that gives the number of entries in the following table.
    SampleEntry — is the appropriate sample entry.
    width in the VisualSampleEntry is the maximum visual width of the stream described
          by this sample description, in pixels, as described in ISO/IEC 14496-2, 6.2.3,
          video_object_layer_width in the visual headers; it is repeated here for the
          convenience of tools;
    height in the VisualSampleEntry is the maximum visual height of the stream described
           by this sample description, in pixels, as described in ISO/IEC 14496-2, 6.2.3,
           video_object_layer_height in the visual headers; it is repeated here for the
           convenience of tools;
    compressorname in the sample entries shall be set to 0
    ES — is the ES Descriptor for this stream.
    """

    def __init__(self):
        self.esds = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = Box.decode(self, file_strm)

        left_size = Box.Size(self) - Box.GetLength(self)
        while left_size > 0:
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Esds:
                self.mvhd = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = self.mvhd.decode(file_strm)
                self.offset += self.mvhd.Size()
            else:
                file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()
            left_size -= tmp_box.Size()

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = Box.dump(self)
        return dump_info

    def __str__(self):
        # logstr = "%s, data = %s" % (Box.__str__(self), self.data)
        logstr = "%s\n" % (Box.__str__(self))
        return logstr
