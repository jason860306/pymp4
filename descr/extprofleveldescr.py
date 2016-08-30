#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 16:29:10'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *
from descrtagdef import *


class ExtProfLevelDescriptor(object, BaseDescriptor):
    """
    7.2.6.19.1 Syntax
    class ExtensionProfileLevelDescriptor() extends ExtensionDescriptor
        : bit(8) ExtensionProfileLevelDescrTag {
        bit(8) profileLevelIndicationIndex;
        bit(8) ODProfileLevelIndication;
        bit(8) sceneProfileLevelIndication;
        bit(8) audioProfileLevelIndication;
        bit(8) visualProfileLevelIndication;
        bit(8) graphicsProfileLevelIndication;
        bit(8) MPEGJProfileLevelIndication;
        bit(8) TextProfileLevelIndication;
        bit(8) 3DCProfileLevelIndication;
    }
    7.2.6.19.2 Semantics
    The ExtensionProfileLevelDescriptor conveys profile and level extension
    information. This descriptor is used to signal a profile and level
    indication set and its unique index and can be extended by ISO to signal
    any future set of profiles and levels.
    profileLevelIndicationIndex – a unique identifier for the set of profile
                                  and level indications described in this
                                  descriptor within the name scope defined by
                                  the IOD.
    ODProfileLevelIndication – an indication of the profile and level required
                               to process object descriptor streams associated
                               with the InitialObjectDescriptor containing this
                               Extension Profile and Level descriptor.
    sceneProfileLevelIndication – an indication of the profile and level required
                                  to process the scene graph nodes within scene
                                  description streams associated with the
                                  InitialObjectDescriptor containing this Extension
                                  Profile and Level descriptor.
    audioProfileLevelIndication – an indication of the profile and level required to
                                  process audio streams associated with the
                                  InitialObjectDescriptor containing this Extension
                                  Profile and Level descriptor.
    visualProfileLevelIndication – an indication of the profile and level required to
                                   process visual streams associated with the
                                   InitialObjectDescriptor containing this Extension
                                   Profile and Level descriptor.
    graphicsProfileLevelIndication – an indication of the profile and level required
                                     to process graphics nodes within scene description
                                     streams associated with the InitialObjectDescriptor
                                     containing this Extension Profile and Level descriptor.
    MPEGJProfileLevelIndication – an indication as defined in Table 11 of the MPEG-J
                                  profile and level required to process the content
                                  associated with the InitialObjectDescriptor containing
                                  this Extension Profile and Level descriptor.
    TextProfileLevelIndication – an indication as defined in Table 12, of the Text Profile
                                 and Level specified in ISO/IEC 14496-18 and required to
                                 process the content associated with the InitialObjectDescriptor
                                 containing this Text Profile and Level descriptor.
    3DCProfileLevelIndication – an indication of the 3D Compression Profile and Level specified
                                in ISO/IEC 14496-16 and required to process the content
                                associated with the InitialObjectDescriptor containing this
                                3D Compression Profile and Level descriptor
    """

    def __init__(self, offset=0, descr_tag=DescrTag_ExtensionProfileLevelDescrTag):
        BaseDescriptor.__init__(self, offset, descr_tag)
        self.profileLevelIndicationIndex = 0
        self.ODProfileLevelIndication = 0
        self.sceneProfileLevelIndication = 0
        self.audioProfileLevelIndication = 0
        self.visualProfileLevelIndication = 0
        self.graphicsProfileLevelIndication = 0
        self.mpegJProfileLevelIndication = 0
        self.textProfileLevelIndication = 0
        self.threeDCProfileLevelIndication = 0
