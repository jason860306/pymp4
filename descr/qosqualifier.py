#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:56:06'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'


# '$Source$'


class QoSQualifier(object):
    """
    7.2.6.15.3.1 Syntax
    abstract aligned(8) expandable(228-1) class QoS_Qualifier
        : bit(8) tag=0x01..0xff
    {
        // empty. To be filled by classes extending this class.
    }
    class QoS_Qualifier_MAX_DELAY extends QoS_Qualifier
        : bit(8) tag=0x01 {
        unsigned int(32) MAX_DELAY;
    }
    class QoS_Qualifier_PREF_MAX_DELAY extends QoS_Qualifier
        : bit(8) tag=0x02 {
        unsigned int(32) PREF_MAX_DELAY;
    }
    class QoS_Qualifier_LOSS_PROB extends QoS_Qualifier
        : bit(8) tag=0x03 {
        double(32) LOSS_PROB;
    }
    class QoS_Qualifier_MAX_GAP_LOSS extends QoS_Qualifier
        : bit(8) tag=0x04 {
        unsigned int(32) MAX_GAP_LOSS;
    }
    class QoS_Qualifier_MAX_AU_SIZE extends QoS_Qualifier
        : bit(8) tag=0x41 {
        unsigned int(32) MAX_AU_SIZE;
    }
    class QoS_Qualifier_AVG_AU_SIZE extends QoS_Qualifier
        : bit(8) tag=0x42 {
        unsigned int(32) AVG_AU_SIZE;
    }
    class QoS_Qualifier_MAX_AU_RATE extends QoS_Qualifier
        : bit(8) tag=0x43 {
        unsigned int(32) MAX_AU_RATE;
    }
    class QoS_Qualifier_REBUFFERING_RATIO extends QoS_Qualifier
        : bit(8) tag=0x44 {
        bit(8) REBUFFERING_RATIO;
    }
    7.2.6.15.3.2 Semantics
    QoS qualifiers are defined as derived classes from the abstract
    QoS_Qualifier class. They are identified by means of their class tag.
    Unused tag values up to and including 0x7F are reserved for ISO use.
    Tag values from 0x80 up to and including 0xFE are user private.
    Tag values 0x00 and 0xFF are forbidden.

    MAX_DELAY – Maximum end to end delay for the stream in microseconds.
    PREF_MAX_DELAY – Preferred end to end delay for the stream in microseconds.
    LOSS_PROB – Allowable loss probability of any single AU as a fractional
                value between 0.0 and 1.0.
    MAX_GAP_LOSS – Maximum allowable number of consecutively lost AUs.
    MAX_AU_SIZE – Maximum size of an AU in bytes.
    AVG_AU_SIZE – Average size of an AU in bytes.
    MAX_AU_RATE – Maximum arrival rate of AUs in AUs/second.
    REBUFFERING_RATIO – Ratio of the decoding buffer that should be filled in
                        case of prebuffering or rebuffering. The ratio is
                        expressed in percentage, with an integer value between
                        0 and 100. Values outside that range are reserved.

    7.2.6.15.3.2.1 Rebuffering
    In certain scenarios the System Decoder Model cannot be strictly observed.
    This is the case of e.g. file retrieval scenarios in which the data is pulled
    from a remote server over a network with unpredictable performances. In such
    a case prebuffering and/or rebuffering may be required in order to allow for
    a better quality in the user experience. Note that scenarios involving real
    time streaming servers do not fall in this category, since a streaming server
    presumably delivers content according to the appropriate timeline.

    An elementary stream is prebuffered when the decoder waits until the
    decodingBuffer has been filled up to a certain threshold before starting
    fetching data from it.

    An elementary stream is rebuffered when a decoder stops fetching data from
    the decodingBuffer and before resuming fetching data waits until that buffer
    has been filled again up to a certain threshold.

    In order to inform a receiver whether a certain elementary stream requires
    prebuffering and/or rebuffering the QoS_Qualifier_REBUFFERING_RATIO qualifier
    can be included in the Elementary Stream Descriptor (see 7.2.6.15.3.1).
    By default, in the absence of such qualifier, an elementary stream does not
    require pre-buffering or rebuffering
    """

    def __init__(self, tag=0x01):
        self.tag = tag
