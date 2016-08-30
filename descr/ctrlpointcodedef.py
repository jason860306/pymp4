#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-06 14:38:18'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# ---------------------------------------------------------------------------------
# controlPointCode Description
# ---------------------------------------------------------------------------------
# 0x00      | No control point.
# 0x01      | Control Point between the decode buffer and the decoder. This is between
#           | the decode buffer and class loader for MPEG-J streams.
# 0x02      | Control Point between the decoder and the composition buffer.
# 0x03      | Control Point between the composition buffer and the compositor.
# 0x04      | BIFS Tree
# 0x05-0xDF | ISO Reserved
# 0xE0-0xFE | User defined
# 0xFF      | Forbidden
# ---------------------------------------------------------------------------------

CtrlPoint_None = 0x00
CtrlPoint_MpegJ_DecBuf_Decoder = 0x01
CtrlPoint_Decoder_CompositionBuf = 0x02
CtrlPoint_CompositionBuf_Compositor = 0x03
CtrlPoint_BIFS_Tree = 0x04
CtrlPoint_ISOReserved05 = 0x05
CtrlPoint_ISOReservedDF = 0xDF
CtrlPoint_Forbidde = 0xFF
