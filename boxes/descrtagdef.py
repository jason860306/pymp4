#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # Administrator
__date__ = '2016/6/29 18:31'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


# Table 1 — List of Class Tags for Descriptors
# -------------------------------------------------
# Tag value | Tag name
# -------------------------------------------------
# 0x00      |  Forbidden
# 0x01      |  ObjectDescrTag
# 0x02      |  InitialObjectDescrTag
# 0x03      |  ES_DescrTag
# 0x04      |  DecoderConfigDescrTag
# 0x05      |  DecSpecificInfoTag
# 0x06      |  SLConfigDescrTag
# 0x07      |  ContentIdentDescrTag
# 0x08      |  SupplContentIdentDescrTag
# 0x09      |  IPI_DescrPointerTag
# 0x0A      |  IPMP_DescrPointerTag
# 0x0B      |  IPMP_DescrTag
# 0x0C      |  QoS_DescrTag
# 0x0D      |  RegistrationDescrTag
# 0x0E      |  ES_ID_IncTag
# 0x0F      |  ES_ID_RefTag
# 0x10      |  MP4_IOD_Tag
# 0x11      |  MP4_OD_Tag
# 0x12      |  IPL_DescrPointerRefTag
# 0x13      |  ExtensionProfileLevelDescrTag
# 0x14      |  profileLevelIndicationIndexDescrTag
# 0x15-0x3F |  Reserved for ISO use
# 0x40      |  ContentClassificationDescrTag
# 0x41      |  KeyWordDescrTag
# 0x42      |  RatingDescrTag
# 0x43      |  LanguageDescrTag
# 0x44      |  ShortTextualDescrTag
# 0x45      |  ExpandedTextualDescrTag
# 0x46      |  ContentCreatorNameDescrTag
# 0x47      |  ContentCreationDateDescrTag
# 0x48      |  OCICreatorNameDescrTag
# 0x49      |  OCICreationDateDescrTag
# 0x4A      |  SmpteCameraPositionDescrTag
# 0x4B      |  SegmentDescrTag
# 0x4C      |  MediaTimeDescrTag
# 0x4D-0x5F |  Reserved for ISO use (OCI extensions)
# 0x60      |  IPMP_ToolsListDescrTag
# 0x61      |  IPMP_ToolTag
# 0x62      |  M4MuxTimingDescrTag
# 0x63      |  M4MuxCodeTableDescrTag
# 0x64      |  ExtSLConfigDescrTag
# 0x65      |  M4MuxBufferSizeDescrTag
# 0x66      |  M4MuxIdentDescrTag
# 0x67      |  DependencyPointerTag
# 0x68      |  DependencyMarkerTag
# 0x69      |  M4MuxChannelDescrTag
# 0x6A-0xBF |  Reserved for ISO use
# 0xC0-0xFE |  User private
# 0xFF      |  Forbidden
# -------------------------------------------------

# Class Tags for Descriptors
DescrTagForbidden00 = 0x00
DescrTagObjectDescrTag = 0x01
DescrTagInitialObjectDescrTag = 0x02
DescrTagES_DescrTag = 0x03
DescrTagDecoderConfigDescrTag = 0x04
DescrTagDecSpecificInfoTag = 0x05
DescrTagSLConfigDescrTag = 0x06
DescrTagContentIdentDescrTag = 0x07
DescrTagSupplContentIdentDescrTag = 0x08
DescrTagIPI_DescrPointerTag = 0x09
DescrTagIPMP_DescrPointerTag = 0x0A
DescrTagIPMP_DescrTag = 0x0B
DescrTagQoS_DescrTag = 0x0C
DescrTagRegistrationDescrTag = 0x0D
DescrTagES_ID_IncTag = 0x0E
DescrTagES_ID_RefTag = 0x0F
DescrTagMP4_IOD_Tag = 0x10
DescrTagMP4_OD_Tag = 0x11
DescrTagIPL_DescrPointerRefTag = 0x12
DescrTagExtensionProfileLevelDescrTag = 0x13
DescrTagprofileLevelIndicationIndexDescrTag = 0x14
# DescrTagReserved for ISO use = 0x15-0x3F
DescrTagContentClassificationDescrTag = 0x40
DescrTagKeyWordDescrTag = 0x41
DescrTagRatingDescrTag = 0x42
DescrTagLanguageDescrTag = 0x43
DescrTagShortTextualDescrTag = 0x44
DescrTagExpandedTextualDescrTag = 0x45
DescrTagContentCreatorNameDescrTag = 0x46
DescrTagContentCreationDateDescrTag = 0x47
DescrTagOCICreatorNameDescrTag = 0x48
DescrTagOCICreationDateDescrTag = 0x49
DescrTagSmpteCameraPositionDescrTag = 0x4A
DescrTagSegmentDescrTag = 0x4B
DescrTagMediaTimeDescrTag = 0x4C
# DescrTagReserved for ISO use (OCI extensions) = 0x4D-0x5F
DescrTagIPMP_ToolsListDescrTag = 0x60
DescrTagIPMP_ToolTag = 0x61
DescrTagM4MuxTimingDescrTag = 0x62
DescrTagM4MuxCodeTableDescrTag = 0x63
DescrTagExtSLConfigDescrTag = 0x64
DescrTagM4MuxBufferSizeDescrTag = 0x65
DescrTagM4MuxIdentDescrTag = 0x66
DescrTagDependencyPointerTag = 0x67
DescrTagDependencyMarkerTag = 0x68
DescrTagM4MuxChannelDescrTag = 0x69
# DescrTagReserved for ISO use = 0x6A-0xBF
# DescrTagUser private = 0xC0-0xFE
DescrTagForbiddenFF = 0xFF

# DescrTagAdditional Class Tags for Descriptors
DescrTagExtDescrTagStartRange = 0x6A
DescrTagExtDescrTagEndRange = 0xFE
DescrTagOCIDescrTagStartRange = 0x40
DescrTagOCIDescrTagEndRange = 0x5F
