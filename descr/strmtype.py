#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 15:54:17'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# Table 6 — streamType Values
# -----------------------------------------------------------------
# streamType value | Stream type description
# -----------------------------------------------------------------
# 0x00             | Forbidden
# 0x01             | ObjectDescriptorStream (see 7.2.5)
# 0x02             | ClockReferenceStream (see 7.3.2.5)
# 0x03             | SceneDescriptionStream (see ISO/IEC 14496-11)
# 0x04             | VisualStream
# 0x05             | AudioStream
# 0x06             | MPEG7Stream
# 0x07             | IPMPStream (see 7.2.3.2)
# 0x08             | ObjectContentInfoStream (see 7.2.4.2)
# 0x09             | MPEGJStream
# 0x0A             | Interaction Stream
# 0x0B             | IPMPToolStream (see [ISO/IEC 14496-13])
# 0x0C - 0x1F      | reserved for ISO use
# 0x20 - 0x3F      | user private
# -----------------------------------------------------------------

StrmType_Forbidden = 0x00
StrmType_ObjectDescriptorStream = 0x01
StrmType_ClockReferenceStream = 0x02
StrmType_SceneDescriptionStream = 0x03
StrmType_VisualStream = 0x04
StrmType_AudioStream = 0x05
StrmType_MPEG7Stream = 0x06
StrmType_IPMPStream = 0x07
StrmType_ObjectContentInfoStream = 0x08
StrmType_MPEGJStream = 0x09
StrmType_InteractionStream = 0x0A
StrmType_IPMPToolStream = 0x0B
StrmType_ISOReserved0C = 0x0C
StrmType_ISOReserved1F = 0x1F
StrmType_UserPrivate20 = 0x20
StrmType_UserPrivate3F = 0x3F
