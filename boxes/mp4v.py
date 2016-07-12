#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:51:34'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from visual_sample_entry import *


class Mp4v(object, VisualSampleEntry):
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
        super(Mp4v, self).__init__()
        self.esds = None
