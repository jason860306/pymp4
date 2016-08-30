#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 18:31:25'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# Table 3 — ODProfileLevelIndication Values
# ------------------------------------------------------------
# Value     | Profile                                | Level
# ------------------------------------------------------------
# 0x00      | Forbidden                              | -
# 0x01      | Reserved for ISO use (no SL extension) | -
# 0x02-0x7F | Reserved for ISO use (SL extension)    | -
# 0x03-0x7F | Reserved for ISO use                   |
# 0x80-0xFD | user private                           | -
# 0xFE      | No OD profile specified                | -
# 0xFF      | No OD capability required              | -
# ------------------------------------------------------------
# NOTE — Usage of the value 0xFE indicates that the content
# described by this InitialObjectDescriptor does not comply
# to any OD profile specified in ISO/IEC 14496-1. Usage of
# the value 0xFF indicates that none of the OD profile
# capabilities are required for this content. Usage of the
# value 0x01 also indicates that the SL extension mechanism
# is not present.

OdProfLevelIndic_Forbidden00 = 0x00
OdProfLevelIndic_ReservedISONoSLExtension = 0x01
OdProfLevelIndic_ReservedISOSLExtension02 = 0x02
OdProfLevelIndic_ReservedISOSLExtension7F = 0x7F
OdProfLevelIndic_ReservedISO03 = 0x03
OdProfLevelIndic_ReservedISO7F = 0x7F
OdProfLevelIndic_UserPrivate80 = 0x80
OdProfLevelIndic_UserPrivateFD = 0xFD
OdProfLevelIndic_NoODProfileSpecified = 0xFE
OdProfLevelIndic_NoODCapabilityRequired = 0xFF
