#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:18:50'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from slcfgdescr import *


class ExtendedSLConfigDescriptor(object, SLConfigDescriptor):
    """
    7.3.2.3.1 Syntax
    class SLConfigDescriptor extends BaseDescriptor
        : bit(8) tag=SLConfigDescrTag {
        bit(8) predefined;
        if (predefined==0) {
            bit(1) useAccessUnitStartFlag;
            bit(1) useAccessUnitEndFlag;
            bit(1) useRandomAccessPointFlag;
            bit(1) hasRandomAccessUnitsOnlyFlag;
            bit(1) usePaddingFlag;
            bit(1) useTimeStampsFlag;
            bit(1) useIdleFlag;
            bit(1) durationFlag;
            bit(32) timeStampResolution;
            bit(32) OCRResolution;
            bit(8) timeStampLength; // must be ≤ 64
            bit(8) OCRLength; // must be ≤ 64
            bit(8) AU_Length; // must be ≤ 32
            bit(8) instantBitrateLength;
            bit(4) degradationPriorityLength;
            bit(5) AU_seqNumLength; // must be ≤ 16
            bit(5) packetSeqNumLength; // must be ≤ 16
            bit(2) reserved=0b11;
        }
        if (durationFlag) {
            bit(32) timeScale;
            bit(16) accessUnitDuration;
            bit(16) compositionUnitDuration;
        }
        if (!useTimeStampsFlag) {
            bit(timeStampLength) startDecodingTimeStamp;
            bit(timeStampLength) startCompositionTimeStamp;
        }
    }
    class ExtendedSLConfigDescriptor extends SLConfigDescriptor
        : bit(8) tag=ExtSLConfigDescrTag {
        SLExtensionDescriptor slextDescr[1..255];
    }

    7.3.2.3.2 Semantics
    The SL packet header may be configured according to the needs of each
    individual elementary stream. Parameters that can be selected include
    the presence, resolution and accuracy of time stamps and clock references.
    This flexibility allows, for example, a low bitrate elementary stream to
    incur very little overhead on SL packet headers.

    For each elementary stream the configuration is conveyed in an
    SLConfigDescriptor, which is part of the associated ES_Descriptor within
    an object descriptor.

    The configurable parameters in the SL packet header can be divided in two
    classes: those that apply to each SL packet (e.g. OCR, sequenceNumber)
    and those that are strictly related to access units (e.g. time stamps,
    accessUnitLength, instantBitrate, degradationPriority).

    predefined – allows to default the values from a set of predefined parameter
    sets as detailed below.

    NOTE — This table will be updated by amendments to ISO/IEC 14496 to include
    predefined configurations as required by future profiles.

    useAccessUnitStartFlag – indicates that the accessUnitStartFlag is present in
    each SL packet header of this elementary stream.

    useAccessUnitEndFlag – indicates that the accessUnitEndFlag is present in each
    SL packet header of this elementary stream.

    If neither useAccessUnitStartFlag nor useAccessUnitEndFlag are set this implies
    that each SL packet corresponds to a complete access unit.

    useRandomAccessPointFlag – indicates that the RandomAccessPointFlag is present
    in each SL packet header of this elementary stream.

    hasRandomAccessUnitsOnlyFlag – indicates that each SL packet corresponds to a
    random access point. In that case the randomAccessPointFlag need not be used.

    usePaddingFlag – indicates that the paddingFlag is present in each SL packet
    header of this elementary stream.

    UseTimeStampsFlag: indicates that time stamps are used for synchronisation of
    this elementary stream. They are conveyed in the SL packet headers. Otherwise,
    the parameters accessUnitDuration, compositionUnitDuration, startDecodingTimeStamp
    and startCompositionTime-Stamp conveyed in this SL packet header configuration
    shall be used for synchronisation.

    NOTE — The use of start time stamps and durations (useTimeStampsFlag=0) may only be
    feasible under some conditions, including an error free environment. Random access
    is not easily possible.

    useIdleFlag – indicates that idleFlag is used in this elementary stream.

    durationFlag – indicates that the constant duration of access units and composition
    units for this elementary stream is subsequently signaled.

    timeStampResolution – is the resolution of the time stamps in clock ticks per second.

    OCRResolution – is the resolution of the object time base in cycles per second.

    timeStampLength – is the length of the time stamp fields in SL packet headers.
    timeStampLength shall take values between zero and 64 bit.

    OCRlength – is the length of the objectClockReference field in SL packet headers.
    A length of zero indicates that no objectClockReferences are present in this
    elementary stream. If OCRstreamFlag is set, OCRLength shall be zero. Else OCRlength
    shall take values between zero and 64 bit.

    AU_Length – is the length of the accessUnitLength fields in SL packet headers for
    this elementary stream. AU_Length shall take values between zero and 32 bit.

    instantBitrateLength – is the length of the instantBitrate field in SL packet headers
    for this elementary stream.

    degradationPriorityLength – is the length of the degradationPriority field in SL
    packet headers for this elementary stream.

    AU_seqNumLength – is the length of the AU_sequenceNumber field in SL packet headers
    for this elementary stream.

    packetSeqNumLength – is the length of the packetSequenceNumber field in SL packet
    headers for this elementary stream.

    timeScale – used to express the duration of access units and composition units.
    One second is evenly divided in timeScale parts.

    accessUnitDuration – the duration of an access unit is accessUnitDuration *
    1/timeScale seconds.

    compositionUnitDuration – the duration of a composition unit is compositionUnitDuration *
    1/timeScale seconds.

    startDecodingTimeStamp – conveys the time at which the first access unit of this
    elementary stream shall be decoded. It is conveyed in the resolution specified by
    timeStampResolution.

    startCompositionTimeStamp – conveys the time at which the composition unit
    corresponding to the first access unit of this elementary stream shall be decoded.
    It is conveyed in the resolution specified by timeStampResolution.

    slextDescr – is an array of ExtensionDescriptors defined for ExtendedSLConfigDescriptor
    as specified in 7.3.2.3.1.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_ExtSLConfigDescrTag):
        super(ExtendedSLConfigDescriptor, self).__init__(offset, descr_tag)
        self.slextDescr = []  # an array of ExtensionDescriptors

    def decode(self, file_strm):
        return file_strm

    def dump(self):
        dump_info = super(ExtendedSLConfigDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(ExtendedSLConfigDescriptor, self).size()

    def __str__(self):
        log_str = super(ExtendedSLConfigDescriptor, self).__str__()
        return log_str
