#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '2016-09-19 下午6:17'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


# ------------------------------------------------------------------------------------------------------------
# Table 1.17 – Audio Object Types
# ------------------------------------------------------------------------------------------------------------
# Object Type ID | Audio Object Type    | definition of elementary stream | Mapping of audio payloads to access
#                |                      | payloads and detailed syntax    | units and elementary streams
# ------------------------------------------------------------------------------------------------------------
# 0              | NULL                 |                                 |
#              1 | AAC MAIN             | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.1
#              2 | AAC LC               | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.1
#              3 | AAC SSR              | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.1
#              4 | AAC LTP              | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.1
#              5 | SBR                  | ISO/IEC 14496-3 subpart 4       |
#              6 | AAC scalable         | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.2
#              7 | TwinVQ               | ISO/IEC 14496-3 subpart 4       |
#              8 | CELP                 | ISO/IEC 14496-3 subpart 3       |
#              9 | HVXC                 | ISO/IEC 14496-3 subpart 2       |
#             10 | (reserved)           |                                 |
#             11 | (reserved)           |                                 |
#             12 | TTSI                 | ISO/IEC 14496-3 subpart 6       |
#             13 | Main synthetic       | ISO/IEC 14496-3 subpart 5       |
#             14 | Wavetable synthesis  | ISO/IEC 14496-3 subpart 5       |
#             15 | General MIDI         | ISO/IEC 14496-3 subpart 5       |
#             16 | Algorithmic Synthesis|                                 |
#                | and Audio FX         | ISO/IEC 14496-3 subpart 5       |
#             17 | ER AAC LC            | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.3
#             18 | (reserved)           |                                 |
#             19 | ER AAC LTP           | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.3
#             20 | ER AAC scalable      | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.3
#             21 | ER Twin VQ           | ISO/IEC 14496-3 subpart 4       |
#             22 | ER BSAC              | ISO/IEC 14496-3 subpart 4       |
#             23 | ER AAC LD            | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.3
#             24 | ER CELP              | ISO/IEC 14496-3 subpart 3       |
#             25 | ER HVXC              | ISO/IEC 14496-3 subpart 2       |
#             26 | ER HILN              | ISO/IEC 14496-3 subpart 7       |
#             27 | ER Parametric        | ISO/IEC 14496-3 subpart 2 and 7 |
#             28 | SSC                  | ISO/IEC 14496-3 subpart 8       |
#             29 | PS                   | ISO/IEC 14496-3 subpart 8       |
#             30 | MPEG Surround        | ISO/IEC 23003-1                 |
#             31 | (escape)             |                                 |
#             32 | Layer-1              | ISO/IEC 14496-3 subpart 9       |
#             33 | Layer-2              | ISO/IEC 14496-3 subpart 9       |
#             34 | Layer-3              | ISO/IEC 14496-3 subpart 9       |
#             35 | DST                  | ISO/IEC 14496-3 subpart 10      |
#             36 | ALS                  | ISO/IEC 14496-3 subpart 11      |
#             37 | SLS                  | ISO/IEC 14496-3 subpart 12      |
#             38 | SLS non-core         | ISO/IEC 14496-3 subpart 12      |
#             39 | ER AAC ELD           | ISO/IEC 14496-3 subpart 4       | see subclause 1.6.2.2.2.4
#             40 | SMR Simple           | ISO/IEC 14496-23                |
#             41 | SMR Main             | ISO/IEC 14496-23                |
# ------------------------------------------------------------------------------------------------------------

AOT_NULL = 0
AOT_AAC_MAIN = 1
AOT_AAC_LC = 2
AOT_AAC_SSR = 3
AOT_AAC_LTP = 4
AOT_SBR = 5
AOT_AAC_Scalable = 6
AOT_TwinVQ = 7
AOT_CELP = 8
AOT_HVXC = 9
AOT_Reserved10 = 10
AOT_Reserved11 = 11
AOT_TTSI = 12
AOT_Main_Synthetic = 13
AOT_Wavetable_Synthesis = 14
AOT_General_MIDI = 15
AOT_Algorithmic_Synthesis_Audio_FX = 16
AOT_ER_AAC_LC = 17
AOT_Reserved18 = 18
AOT_ER_AAC_LTP = 19
AOT_ER_AAC_Scalable = 20
AOT_ER_Twin_VQ = 21
AOT_ER_BSAC = 22
AOT_ER_AAC_LD = 23
AOT_ER_CELP = 24
AOT_ER_HVXC = 25
AOT_ER_HILN = 26
AOT_ER_Parametric = 27
AOT_SSC = 28
AOT_PS = 29
AOT_MPEG_Surround = 30
AOT_Escape = 31
AOT_Layer1 = 32
AOT_Layer2 = 33
AOT_Layer3 = 34
AOT_DST = 35
AOT_ALS = 36
AOT_SLS = 37
AOT_SLS_Non_Core = 38
AOT_ER_AAC_ELD = 39
AOT_SMR_Simple = 40
AOT_SMR_Main = 41
