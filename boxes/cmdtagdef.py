#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$id$'
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

CmdTagForbidden00 = 0x00
CmdTagObjectDescrUpdateTag = 0x01
CmdTagObjectDescrRemoveTag = 0x02
CmdTagES_DescrUpdateTag = 0x03
CmdTagES_DescrRemoveTag = 0x04
CmdTagIPMP_DescrUpdateTag = 0x05
CmdTagIPMP_DescrRemoveTag = 0x06
CmdTagES_DescrRemoveRefTag = 0x07
CmdTagObjectDescrExecuteTag = 0x08
# CmdTagReserved for ISO (command tags) = 0x09-0xBF
# CmdTagUser private = 0xC0-0xFE
CmdTagForbiddenFF = 0xFF
