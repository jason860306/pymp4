#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 18:25:13'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from objdescr import *


class InitObjectDescriptor(ObjectDescriptor, object):
    """
    7.2.6.4.1 Syntax
    class InitialObjectDescriptor extends ObjectDescriptorBase
        : bit(8) tag=InitialObjectDescrTag {
        bit(10) ObjectDescriptorID;
        bit(1) URL_Flag;
        bit(1) includeInlineProfileLevelFlag;
        const bit(4) reserved=0b1111;
        if (URL_Flag) {
            bit(8) URLlength;
            bit(8) URLstring[URLlength];
        } else {
            bit(8) ODProfileLevelIndication;
            bit(8) sceneProfileLevelIndication;
            bit(8) audioProfileLevelIndication;
            bit(8) visualProfileLevelIndication;
            bit(8) graphicsProfileLevelIndication;
            ES_Descriptor esDescr[1 .. 255];
            OCI_Descriptor ociDescr[0 .. 255];
            IPMP_DescriptorPointer ipmpDescrPtr[0 .. 255];
            IPMP_Descriptor ipmpDescr [0 .. 255];
            IPMP_ToolListDescriptor toolListDescr[0 .. 1];
        }
        ExtensionDescriptor extDescr[0 .. 255];
    }
    When an InitialObjectDescriptor is used in the OD track in an MP4 file,
    the InitialObjectDescrTag is replaced by MP4_IOD_Tag.

    7.2.6.4.2 Semantics
    The InitialObjectDescriptor is a variation of the ObjectDescriptor specified
    in the previous Subclause that allows to signal profile and level information
    for the content refered by it. It shall be used to gain initial access to
    ISO/IEC 14496 content (see 7.2.7.3).

    Profile and level information indicated in the InitialObjectDescriptor indicates
    the profile and level supported by at least the first base layer stream (i.e.
    an elementary stream with a streamDependenceFlag set to 0) in each object
    descriptor depending on this initial object descriptor.

    objectDescriptorId – This syntax element uniquely identifies the
                         InitialObjectDescriptor within its name scope
                         (see 7.2.7.2.4). The value 0 is forbidden and
                         the value 1023 is reserved.
    URL_Flag – a flag that indicates the presence of a URLstring.
    includeInlineProfileLevelFlag – a flag that, if set to one, indicates that the
                                    subsequent profile indications take into
                                    account the resources needed to process any
                                    content that might be inlined.
    URLlength – the length of the subsequent URLstring in bytes.
    URLstring[] – A string with a UTF-8 (ISO/IEC 10646-1) encoded URL that shall
                  point to another InitialObjectDescriptor. Only the content of
                  this object descriptor shall be returned by the delivery entity
                  upon access to this URL. Within the current name scope, the new
                  object descriptor shall be referenced by the objectDescriptorId
                  of the object descriptor carrying the URLstring. On name scopes
                  see 7.2.7.2.4. Permissible URLs may be constrained by profile
                  and levels as well as by specific delivery layers.
    ODProfileLevelIndication – an indication as defined in Table 3 of the object
                               descriptor profile and level required to process
                               the content associated with this InitialObjectDescriptor.
    sceneProfileLevelIndication – an indication as defined in ISO/IEC 14496-11 of the
                                  scene graph profile and level required to process the
                                  content associated with this InitialObjectDescriptor.
    audioProfileLevelIndication – an indication as defined in ISO/IEC 14496-3 of the
                                  audio profile and level required to process the
                                  content associated with this InitialObjectDescriptor.
    visualProfileLevelIndication – an indication as defined in ISO/IEC 14496-2 and in
                                   Table 4 of the visual profile and level required to
                                   process the content associated with this
                                   InitialObjectDescriptor.
    graphicsProfileLevelIndication – an indication as defined in ISO/IEC 14496-11 of
                                     the graphics profile and level required to process
                                     the content associated with this InitialObjectDescriptor.
    esDescr[] – an array of ES_Descriptors as defined in 7.2.6.5. The array shall have any
                number of one up to 255 elements.
    ociDescr[] – an array of OCI_Descriptors as defined in 7.2.6.18 that relates to the set
                 of audio-visual objects that are described by this initial object descriptor.
                 The array shall have any number of zero up to 255 elements.
    ipmpDescrPtr[] – an array of IPMP_DescriptorPointer, as defined in 7.2.6.13, that points
                     to the IPMP_Descriptors related to the elementary stream(s) described
                     by this object descriptor. The array shall have any number of zero up
                     to 255 elements.
    ipmpDescr [] – a list of IPMP_Descriptors that may be referenced by streams declared
                   in esDescr. The array shall have any number of zero up to 255 elements.
                   The following scope and usage rules apply:
                   i. Entries in the ipmpDescr table define IPMP System/Tools that can
                      be referenced by IPMP_DescriptorPointers located in the IOD itself
                      or ESDs declared in this IOD.
                   ii. IOD contained IPMP_Descriptors have scope within the given IOD only
                       and shall not be referenced by subsequently declared IODs, ODs,
                       streams nor available for updating via IPMP_DescriptorUpdates.
                   iii. The IOD contained IPMP_Descriptors shall not be referenced by IODs,
                        ODs, streams declared in IOD declared OD or Scene streams.
    toolListDescr – a list of all IPMP tools required for the processing of the content.
                    The array shall have zero or 1 element.
    extDescr[] – an array of ExtensionDescriptors as defined in 7.2.6.16. The array shall
                 have any number of zero up to 255 elements.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_InitialObjectDescrTag):
        super(InitObjectDescriptor, self).__init__(offset, descr_tag)

        self.objDescrID = 0
        self.urlFlag = 0
        self.incInlineProfLevelFlag = 0
        self.reserved = 0

        self.urlLen = 0  # if URL_FLAG
        self.urlString = ''  # if URL_FLAG

        self.odProfLevelIndic = 0  # if not URL_FLAG
        self.sceneProfLevelIndic = 0  # if not URL_FLAG
        self.audioProfLevelIndic = 0  # if not URL_FLAG
        self.visualProfLevelIndic = 0  # if not URL_FLAG
        self.graphicsProfLevelIndic = 0  # if not URL_FLAG
        self.esDescr = []  # if not URL_FLAG
        self.ociDescr = []  # if not URL_FLAG
        self.ipmpDescrPtr = []  # if not URL_FLAG
        self.ipmpDescr = []  # if not URL_FLAG
        self.toolListDescr = []  # if not URL_FLAG

        self.extDescr = []

    def decode(self, file_strm):
        file_strm = super(InitObjectDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(InitObjectDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(InitObjectDescriptor, self).size()

    def __str__(self):
        log_str = super(InitObjectDescriptor, self).__str__()
        return log_str
