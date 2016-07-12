#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 15:16:14'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'

# Table 5 — objectTypeIndication Values
# -------------------------------------------------------------------------
# Value         | ObjectTypeIndication Description
# -------------------------------------------------------------------------
# 0x00          | Forbidden
# 0x01          | Systems ISO/IEC 14496-1 a
# 0x02          | Systems ISO/IEC 14496-1 b
# 0x03          | Interaction Stream
# 0x04          | Systems ISO/IEC 14496-1 Extended BIFS Configuration c
# 0x05          | Systems ISO/IEC 14496-1 AFX d
# 0x06          | Font Data Stream
# 0x07          | Synthesized Texture Stream
# 0x08          | Streaming Text Stream
# 0x09 - 0x1F   | reserved for ISO use
# 0x20          | Visual ISO/IEC 14496-2 e
# 0x21          | Visual ITU-T Recommendation H.264 | ISO/IEC 14496-10 f
# 0x22          | Parameter Sets for ITU-T Recommendation H.264 | ISO/IEC 14496-10 f
# 0x23 - 0x3F   | reserved for ISO use
# 0x40          | Audio ISO/IEC 14496-3 g
# 0x41 - 0x5F   | reserved for ISO use
# 0x60          | Visual ISO/IEC 13818-2 Simple Profile
# 0x61          | Visual ISO/IEC 13818-2 Main Profile
# 0x62          | Visual ISO/IEC 13818-2 SNR Profile
# 0x63          | Visual ISO/IEC 13818-2 Spatial Profile
# 0x64          | Visual ISO/IEC 13818-2 High Profile
# 0x65          | Visual ISO/IEC 13818-2 422 Profile
# 0x66          | Audio ISO/IEC 13818-7 Main Profile
# 0x67          | Audio ISO/IEC 13818-7 LowComplexity Profile
# 0x68          | Audio ISO/IEC 13818-7 Scaleable Sampling Rate Profile
# 0x69          | Audio ISO/IEC 13818-3
# 0x6A          | Visual ISO/IEC 11172-2
# 0x6B          | Audio ISO/IEC 11172-3
# 0x6C          | Visual ISO/IEC 10918-1
# 0x6D          | reserved for registration authority i
# 0x6E          | Visual ISO/IEC 15444-1
# 0x6F - 0x9F   | reserved for ISO use
# 0xA0 - 0xBF   | reserved for registration authority i
# 0xC0 - 0xE0   | user private
# 0xE1          | reserved for registration authority i
# 0xE2 - 0xFE   | user private
# 0xFF          | no object type specified h
# -------------------------------------------------------------------------
#
# a - This type is used for all 14496-1 streams unless specifically indicated
#     to the contrary. Scene Description scenes, which are identified with
#     StreamType=0x03, using this object type value shall use the BIFSConfig
#     specified in ISO/IEC 14496-11.
# b - This object type shall be used, with StreamType=0x03, for Scene
#     Description streams that use the BIFSv2Config specified in ISO/IEC 14496-11.
#     Its use with other StreamTypes is reserved.
# c - This object type shall be used, with StreamType=0x03, for Scene Description
#     streams that use the BIFSConfigEx specified in 7.2.6.7 of this specification.
#     Its use with other StreamTypes is reserved.
# d - This object type shall be used, with StreamType=0x03, for Scene Description
#     streams that use the AFXConfig specified in 7.2.6.7 of this specification.
#     Its use with other StreamTypes is reserved.
# e - Includes associated Amendment(s) and Corrigendum(a). The actual object types
#     are defined in ISO/IEC 14496-2 and are conveyed in the DecoderSpecificInfo
#     as specified in ISO/IEC 14496-2, Annex K.
# f - Includes associated Amendment(s) and Corrigendum(a). The actual object types
#     are defined in ITU-T Recommendation H.264 | ISO/IEC 14496-10 and are conveyed
#     in the DecoderSpecificInfo as specified in this amendment, I.2.
# g - Includes associated Amendment(s) and Corrigendum(a). The actual object types
#     are defined in ISO/IEC 14496-3 and are conveyed in the DecoderSpecificInfo
#     as specified in ISO/IEC 14496-3 subpart 1 subclause 6.2.1.
# h - Streams with this value with a StreamType indicating a systems stream (values
#     1,2,3, 6, 7, 8, 9) shall be treated as if the ObjectTypeIndication had been
#     set to 0x01.
# i - The latest entries registered can be found at http://www.mp4ra.org/object.html.

ObjTypeIndic_Forbidden = 0x00
ObjTypeIndic_14496_1_a = 0x01
ObjTypeIndic_14496_1_b = 0x02
ObjTypeIndic_InteractionStream = 0x03
ObjTypeIndic_14496_1_c = 0x04
ObjTypeIndic_14496_1_d = 0x05
ObjTypeIndic_FontDataStream = 0x06
ObjTypeIndic_SynthesizedTextureStream = 0x07
ObjTypeIndic_StreamingTextStream = 0x08
ObjTypeIndic_ISOReserved09 = 0x09
ObjTypeIndic_ISOReserved1F = 0x1F
ObjTypeIndic_14496_2_e = 0x20
ObjTypeIndic_14496_10_f = 0x21
ObjTypeIndic_Parameter_Sets_14496_10_f = 0x22
ObjTypeIndic_ISOReserved23 = 0x23
ObjTypeIndic_ISOReserved3F = 0x3F
ObjTypeIndic_14496_3_g = 0x40
ObjTypeIndic_ISOReserved41 = 0x41
ObjTypeIndic_ISOReserved5F = 0x5F
ObjTypeIndic_SimpleProfile_13818_2 = 0x60
ObjTypeIndic_MainProfile_13818_2 = 0x61
ObjTypeIndic_SNRProfile_13818_2 = 0x62
ObjTypeIndic_SpatialProfile_13818_2 = 0x63
ObjTypeIndic_HighProfile_13818_2 = 0x64
ObjTypeIndic_422Profile_13818_2 = 0x65
ObjTypeIndic_MainProfile_13818_7 = 0x66
ObjTypeIndic_LowComplexityProfile_13818_7 = 0x67
ObjTypeIndic_ScaleableSamplingRateProfile_13818_7 = 0x68
ObjTypeIndic_13818_3 = 0x69
ObjTypeIndic_11172_2 = 0x6A
ObjTypeIndic_11172_3 = 0x6B
ObjTypeIndic_10918_1 = 0x6C
ObjTypeIndic_Reserved6D_i = 0x6D
ObjTypeIndic_15444_1 = 0x6E
ObjTypeIndic_ISOReserved6F = 0x6F
ObjTypeIndic_ISOReserved9F = 0x9F
ObjTypeIndic_ReservedA0_i = 0xA0
ObjTypeIndic_ReservedBF_i = 0xBF
ObjTypeIndic_UserPrivateC0 = 0xC0
ObjTypeIndic_UserPrivateE0 = 0xE0
ObjTypeIndic_ReservedE1_i = 0xE1
ObjTypeIndic_UserPrivateE2 = 0xE2
ObjTypeIndic_UserPrivateFE = 0xFE
ObjTypeIndic_NoObjTypeSpecified_h = 0xFF
