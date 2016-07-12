#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 16:38:31'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# Table 11 — MPEGJProfileLevelIndication Values
# -----------------------------------------------------------
# Value     | Profile                       | Level
# -----------------------------------------------------------
# 0x00      | Reserved for ISO use          | -
# 0x01      | Personal profile              | L1
# 0x02      | Main profile                  | L1
# 0x03-0x7F | reserved for ISO use          | -
# 0x80-0xFD | user private                  | -
# 0xFE      | no MPEG-J profile specified   | -
# 0xFF      | no MPEG-J capability required | -
# -----------------------------------------------------------
# Note Usage of the value 0xFE may indicate that the content
# described by this InitialObjectDescriptor does not comply
# to any conformance point specified in ISO/IEC 14496-1

MJPLI_ISOReserved00 = 0x00
MJPLI_PersonalProf = 0x01
MJPLI_MainProfile = 0x02
MJPLI_ISOReserved03 = 0x03
MJPLI_ISOReserved7F = 0x7F
MJPLI_UserPrivate80 = 0x80
MJPLI_UserPrivateFD = 0xFD
MJPLI_NoMPEGJProfSpecified = 0xFE
MJPLI_NoMPEGJCapabilityRequired = 0xFF
