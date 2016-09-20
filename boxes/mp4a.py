#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:54:58'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


import mp4boxes
from audio_sample_entry import *


class Mp4a(AudioSampleEntry, object):
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

    def __init__(self, offset=0, box=None):
        super(Mp4a, self).__init__(offset, box)
        self.esds = None

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = super(Mp4a, self).decode(file_strm)

        tmp_box = Box()
        file_strm = tmp_box.peek(file_strm)
        if tmp_box.type == FourCCMp4Esds:
            self.esds = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
            file_strm = self.esds.decode(file_strm)
            self.offset += self.esds.Size()
        else:
            file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
            self.offset += tmp_box.Size()

        return file_strm

    def dump(self):
        dump_info = super(Mp4a, self).dump()
        dump_info['Esds'] = self.esds.dump()
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t%s" % (str(super(Mp4a, self)), self.esds)
        return logstr
