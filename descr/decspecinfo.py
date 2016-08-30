#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 16:21:48'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class DecoderSpecificInfo(object, BaseDescriptor):
    """
    7.2.6.7.1 Syntax
    abstract class DecoderSpecificInfo extends BaseDescriptor
        : bit(8) tag=DecSpecificInfoTag
    {
        // empty. To be filled by classes extending this class.
    }
    7.2.6.7.2 Semantics
    The decoder specific information constitutes an opaque container with
    information for a specific media decoder. The existence and semantics
    of decoder specific information depends on the values of
    DecoderConfigDescriptor.streamType and DecoderConfigDescriptor.objectTypeIndication.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to
    streams complying with ISO/IEC 14496-2 the syntax and semantics of decoder
    specific information are defined in Annex K of that part.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to
    streams complying with ISO/IEC 14496-3 the syntax and semantics of decoder
    specific information are defined in subpart 1, subclause 1.6 of that part.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to scene
    description streams the semantics of decoder specific information is defined
    in ISO/IEC 14496-11.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to streams
    complying with ISO/IEC 13818-7 the decoder specific information consists of
    an „adif_header()“ and an access unit is a „raw_data_block()“ as defined in
    ISO/IEC 13818-7.

    For values of DecoderConfigDescriptor.objectTypeIndication that refer to streams
    complying with ISO/IEC 11172-3 or ISO/IEC 13818-3 the decoder specific information
    is empty since all necessary data is contained in the bitstream frames itself.
    The access units in this case are the „frame()“ bitstream element as is defined
    in ISO/IEC 11172-3
    """

    def __init__(self, descr_tag=DescrTag_DecSpecificInfoTag):
        BaseDescriptor.__init__(self, descr_tag)
