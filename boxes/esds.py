#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:45:19'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from descr.esdescr import *
from fullbox import *


class Esds(FullBox, object):
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
        super(Esds, self).__init__(offset, box)
        self.esDescr = None  # ES_Descriptor

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = super(Esds, self).decode(file_strm)

        tmp_descr = BaseDescriptor(self.offset)
        if tmp_descr.peek(file_strm) is None:
            print "file_strm is None"
            return file_strm
        self.esDescr = create_descr(self.offset, tmp_descr.descr_tag)
        file_strm = self.esDescr.decode(file_strm)
        if file_strm is None:
            print "file_strm is None"
            return file_strm
        self.offset += tmp_descr.size()

        return file_strm

    def get_es_header(self):
        if self.esDescr is not None:
            return self.esDescr.get_es_header()
        return None

    def dump(self):
        dump_info = super(Esds, self).dump()
        dump_info['ES_Descriptor'] = self.esDescr.dump()
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\t%s" % (super(Esds, self), self.esDescr)
        return logstr
