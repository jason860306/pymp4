#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-06 15:33:06'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'


# '$Source$'


class IPMPDataBaseClass(object):
    """
    7.2.3.2.6.2 Syntax
    abstract aligned(8) expandable(2^28-1) class IPMP_Data_BaseClass
        : bit(8) tag=0…255
    {
        bit(8) Version;
        bit(32)dataID;
        // Fields and data extending this message.
    }

    7.2.3.2.6.3 Semantics

    Version - indicates the version of syntax used in the IPMP Data and
    shall be set to “0x01”.

    dataID – used for the purpose of identifying the message. Tools replying
    directly to a message shall include the same dataID in any response.

    tag indicates the tag for the extended IPMP data. The exact values for
    the extension tags are defined in ISO/IEC 14496-13.

    IPMP data extending from IPMP_Data_BaseClass can be carried in the
    following three places:
    • IPMP_Descriptor
    • IPMP_Message defined in ISO/IEC 14496-13 which is subsequently carried
      in IPMP Stream.
    • Messages defined in ISO/IEC 14496-13 specified to carry messages between
      IPMP tools.
    """

    def __init__(self):
        self.version = 0
        self.dataId = 0
