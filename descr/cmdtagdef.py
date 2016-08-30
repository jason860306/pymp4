#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # Administrator
__date__ = '2016/6/29 18:51'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


# Table 2 — List of Class Tags for Commands
# --------------------------------------------
# Tag value   Tag name
# --------------------------------------------
# 0x00      | forbidden
# 0x01      | ObjectDescrUpdateTag
# 0x02      | ObjectDescrRemoveTag
# 0x03      | ES_DescrUpdateTag
# 0x04      | ES_DescrRemoveTag
# 0x05      | IPMP_DescrUpdateTag
# 0x06      | IPMP_DescrRemoveTag
# 0x07      | ES_DescrRemoveRefTag
# 0x08      | ObjectDescrExecuteTag
# 0x09-0xBF | Reserved for ISO (command tags)
# 0xC0-0xFE | User private
# 0xFF      | forbidden
# --------------------------------------------

CmdTag_Forbidden00 = 0x00
CmdTag_ObjectDescrUpdateTag = 0x01
CmdTag_ObjectDescrRemoveTag = 0x02
CmdTag_ES_DescrUpdateTag = 0x03
CmdTag_ES_DescrRemoveTag = 0x04
CmdTag_IPMP_DescrUpdateTag = 0x05
CmdTag_IPMP_DescrRemoveTag = 0x06
CmdTag_ES_DescrRemoveRefTag = 0x07
CmdTag_ObjectDescrExecuteTag = 0x08
CmdTag_ISOReserved09 = 0x09
CmdTag_ISOReservedBF = 0xBF
CmdTag_PrivateUserC0 = 0xC0
CmdTag_PrivateUserFE = 0xFE
CmdTag_ForbiddenFF = 0xFF
