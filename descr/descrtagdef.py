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
DescrTag_Forbidden00 = 0x00
DescrTag_ObjectDescrTag = 0x01
DescrTag_InitialObjectDescrTag = 0x02
DescrTag_ES_DescrTag = 0x03
DescrTag_DecoderConfigDescrTag = 0x04
DescrTag_DecSpecificInfoTag = 0x05
DescrTag_SLConfigDescrTag = 0x06
DescrTag_ContentIdentDescrTag = 0x07
DescrTag_SupplContentIdentDescrTag = 0x08
DescrTag_IPI_DescrPointerTag = 0x09
DescrTag_IPMP_DescrPointerTag = 0x0A
DescrTag_IPMP_DescrTag = 0x0B
DescrTag_QoS_DescrTag = 0x0C
DescrTag_RegistrationDescrTag = 0x0D
DescrTag_ES_ID_IncTag = 0x0E
DescrTag_ES_ID_RefTag = 0x0F
DescrTag_MP4_IOD_Tag = 0x10
DescrTag_MP4_OD_Tag = 0x11
DescrTag_IPL_DescrPointerRefTag = 0x12
DescrTag_ExtensionProfileLevelDescrTag = 0x13
DescrTag_profileLevelIndicationIndexDescrTag = 0x14
DescrTag_ISOReserved15 = 0x15
DescrTag_ISOReserved3F = 0x3F
DescrTag_ContentClassificationDescrTag = 0x40
DescrTag_KeyWordDescrTag = 0x41
DescrTag_RatingDescrTag = 0x42
DescrTag_LanguageDescrTag = 0x43
DescrTag_ShortTextualDescrTag = 0x44
DescrTag_ExpandedTextualDescrTag = 0x45
DescrTag_ContentCreatorNameDescrTag = 0x46
DescrTag_ContentCreationDateDescrTag = 0x47
DescrTag_OCICreatorNameDescrTag = 0x48
DescrTag_OCICreationDateDescrTag = 0x49
DescrTag_SmpteCameraPositionDescrTag = 0x4A
DescrTag_SegmentDescrTag = 0x4B
DescrTag_MediaTimeDescrTag = 0x4C
DescrTag_ISO_OCI_Reserved4D = 0x4D
DescrTag_ISO_OCI_Reserved5F = 0x5F
DescrTag_IPMP_ToolsListDescrTag = 0x60
DescrTag_IPMP_ToolTag = 0x61
DescrTag_M4MuxTimingDescrTag = 0x62
DescrTag_M4MuxCodeTableDescrTag = 0x63
DescrTag_ExtSLConfigDescrTag = 0x64
DescrTag_M4MuxBufferSizeDescrTag = 0x65
DescrTag_M4MuxIdentDescrTag = 0x66
DescrTag_DependencyPointerTag = 0x67
DescrTag_DependencyMarkerTag = 0x68
DescrTag_M4MuxChannelDescrTag = 0x69
DescrTag_ISOReserved6A = 0x6A
DescrTag_ISOReservedBF = 0xBF
DescrTag_UserPrivateC0 = 0xC0
DescrTag_UserPrivateFE = 0xFE
DescrTag_ForbiddenFF = 0xFF

DescrTag_IPMP_ParamtericDescription = 0x10

# Additional Class Tags for Descriptors
DescrTag_ExtDescrTagStartRange = 0x6A
DescrTag_ExtDescrTagEndRange = 0xFE
DescrTag_OCIDescrTagStartRange = 0x40
DescrTag_OCIDescrTagEndRange = 0x5F
