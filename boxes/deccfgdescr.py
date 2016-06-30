#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 15:11:13'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from extprofleveldescr import *


class DecoderConfigDescriptor(BaseDescriptor):
    """
    7.2.6.6.1 Syntax
    class DecoderConfigDescriptor extends BaseDescriptor
        : bit(8) tag=DecoderConfigDescrTag {
        bit(8) objectTypeIndication;
        bit(6) streamType;
        bit(1) upStream;
        const bit(1) reserved=1;
        bit(24) bufferSizeDB;
        bit(32) maxBitrate;
        bit(32) avgBitrate;
        DecoderSpecificInfo decSpecificInfo[0 .. 1];
        profileLevelIndicationIndexDescriptor profileLevelIndicationIndexDescr[0..255];
    }

    7.2.6.6.2 Semantics
    The DecoderConfigDescriptor provides information about the decoder type and
    the required decoder resources needed for the associated elementary stream.
    This is needed at the receiving terminal to determine whether it is able to
    decode the elementary stream. A stream type identifies the category of the
    stream while the optional decoder specific information descriptor contains
    stream specific information for the set up of the decoder in a stream specific
    format that is opaque to this layer.
    ObjectTypeIndication – an indication of the object or scene description type
                           that needs to be supported by the decoder for this
                           elementary stream as per Table 5.

    When the objectTypeIndication value is 0x6C (Visual ISO/IEC 10918-1, which is JPEG)
    the stream may contain one or more Access Units, where one Access Unit is defined
    to be a complete JPEG (as defined in Visual ISO/IEC 10918-1). Note, that timing and
    other Access Unit and packetization information is to be carried in the transport
    layer such as the MPEG-4 Sync Layer.

    When the objectTypeIndication value is 0x6E (Visual ISO/IEC 15444-1, which is
    JPEG 2000) the stream may contain one or more Access Units, where one Access
    Unit is defined to be a complete JPEG 2000 (as defined in Visual ISO/IEC
    15444-1). Note, that timing and other Access Unit and packetization information
    is to be carried in the transport layer such as the MPEG-4 Sync Layer.

    NOTE The format defined in ISO/IEC 15444-3 is preferred for the storage of JPEG
    2000 sequences in file format of the ISO/IEC 14496-12 family, including MP4.

    streamType – conveys the type of this elementary stream as per Table 6.
    upStream – indicates that this stream is used for upstream information.
    bufferSizeDB – is the size of the decoding buffer for this elementary stream in byte.
    maxBitrate – is the maximum bitrate in bits per second of this elementary stream
                 in any time window of one second duration.
    avgBitrate – is the average bitrate in bits per second of this elementary stream.
                 For streams with variable bitrate this value shall be set to zero.
    decSpecificInfo[] – an array of zero or one decoder specific information classes
                        as specified in 7.2.6.7.
    ProfileLevelIndicationIndexDescr [0..255] – an array of unique identifiers for
                                                a set of profile and level indications
                                                as carried in the ExtensionProfileLevelDescr
                                                defined in 7.2.6.19.
    """

    def __init__(self, descr_tag=DescrTag_DecoderConfigDescrTag):
        BaseDescriptor.__init__(self, descr_tag)

        self.objectTypeIndication = 0
        self.streamType = 0
        self.upStream = 0
        self.reserved = 0x1
        self.bufferSizeDB = 0
        self.maxBitrate = 0
        self.avgBitrate = 0
        self.decSpecificInfo = []  # DecoderSpecificInfo
        self.profileLevelIndicationIndexDescr = []  # ExtensionProfileLevelDescriptor
