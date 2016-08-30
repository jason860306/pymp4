#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:21:26'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# Table 9 — Values of IPMP_ToolID
# ----------------------------------------------------------
# IPMP_ToolID Semantics
# ----------------------------------------------------------
# 0x0000            | Forbidden
# 0x0001            | Content
# 0x0002            | Terminal
# 0x0003 - 0x2000   | Reserved for ISO use
# 0x2001 - 0xFFFF   | Carry over from 14496-1 RA
# 0x10000 - 0x100FF | Parametric Tools or Alternative Tools
# 0x100FF – 2^128-2 | Open for registration
# 2^128-1           | Forbidden
# ----------------------------------------------------------

IPMPToolID_Forbidden1 = 0x0000
IPMPToolID_Content = 0x0001
IPMPToolID_Terminal = 0x0002
IPMPToolID_ISOReserved0003 = 0x0003
IPMPToolID_ISOReserved2000 = 0x2000
IPMPToolID_14496_1_RA_CarryOver2001 = 0x2001
IPMPToolID_14496_1_RA_CarryOverFFFF = 0xFFFF
IPMPToolID_ParamAltTools10000 = 0x10000
IPMPToolID_ParamAltTools100FF = 0x100FF
IPMPToolID_RegOpen100FF = 0x100FF
IPMPToolID_RegOpen2_128_2 = 2 ^ 128 - 2
IPMPToolID_Forbidden2 = 2 ^ 128 - 1
