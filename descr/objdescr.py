#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 18:14:03'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class ObjectDescriptor(BaseDescriptor, object):
    """
    7.2.6.3.1 Syntax
    class ObjectDescriptor extends ObjectDescriptorBase
        : bit(8) tag=ObjectDescrTag {
        bit(10) ObjectDescriptorID;
        bit(1) URL_Flag;
        const bit(5) reserved=0b1111.1;
        if (URL_Flag) {
            bit(8) URLlength;
            bit(8) URLstring[URLlength];
        } else {
            ES_Descriptor esDescr[1 .. 255];
            OCI_Descriptor ociDescr[0 .. 255];
            IPMP_DescriptorPointer ipmpDescrPtr[0 .. 255];
            IPMP_Descriptor ipmpDescr [0 .. 255];
        }
        ExtensionDescriptor extDescr[0 .. 255];
    }
    When an ObjectDescriptor is used in the OD track of an MP4 file,
    the ObjectDescrTag is replaced by MP4_OD_Tag.

    7.2.6.3.2 Semantics
    The ObjectDescriptor consists of three different parts.

    The first part uniquely labels the object descriptor within its name
    scope (see 7.2.7.2.4) by means of an objectDescriptorId. Nodes in the
    scene description use objectDescriptorID to refer to the related object
    descriptor. An optional URLstring indicates that the actual object
    descriptor resides at a remote location.

    The second part consists of a list of ES_Descriptors, each providing
    parameters for a single elementary as well as an optional set of object
    content information descriptors and pointers to IPMP descriptors for the
    contents for elementary stream content described in this object descriptor.

    The third part is a set of optional descriptors that support the inclusion
    of future extensions as well as the transport of private data in a backward
    compatible way.

    objectDescriptorId – This syntax element uniquely identifies the
                         ObjectDescriptor within its name scope. The value 0
                         is forbidden and the value 1023 is reserved.
    URL_Flag – a flag that indicates the presence of a URLstring.
    URLlength – the length of the subsequent URLstring in bytes.
    URLstring[] – A string with a UTF-8 (ISO/IEC 10646-1) encoded URL that shall
                  point to another ObjectDescriptor. Only the content of this
                  object descriptor shall be returned by the delivery entity upon
                  access to this URL. Within the current name scope, the new object
                  descriptor shall be referenced by the objectDescriptorId of the
                  object descriptor carrying the URLstring. On name scopes see 7.2.7.2.4.
                  Permissible URLs may be constrained by profile and levels as well
                  as by specific delivery layers.
    esDescr[] – an array of ES_Descriptors as defined in 7.2.6.5. The array shall
                have any number of one up to 255 elements.
    ociDescr[] – an array of OCI_Descriptors, as defined in 7.2.6.18.2, that relates
                 to the audio-visual object(s) described by this object descriptor.
                 The array shall have any number of zero up to 255 elements.
    ipmpDescrPtr[] – an array of IPMP_DescriptorPointer, as defined in 7.2.6.13,
                     that points to the IPMP_Descriptors related to the elementary
                     stream(s) described by this object descriptor. The array shall
                     have any number of zero up to 255 elements.
    ipmpDescr[] – a list of IPMP_Descriptors that may be referenced by streams
                  declared in esDescr. The array shall have any number of zero up
                  to 255 elements. The following scope and usage rules apply:
                  i. Entries in the ipmpDescr table define IPMP System/Tools that
                     can be referenced by IPMP_DescriptorPointers located in the
                     OD itself or ESDs declared in this OD.
                  ii. OD contained IPMP_Descriptors have scope within the given
                      OD only and shall not be referenced by subsequently declared
                      IODs, ODs, streams nor available for updating via
                      IPMP_DescriptorUpdates.
                  iii. The OD contained IPMP_Descriptors shall not be referenced
                       by IODs, ODs or streams declared in OD declared OD or
                       Scene streams.
    extDescr[] – an array of ExtensionDescriptors as defined in 7.2.6.16. The array
                 shall have any number of zero up to 255 elements.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_ObjectDescrTag):
        super(ObjectDescriptor, self).__init__(offset, descr_tag)
        self.objDescrID = 0
        self.urlFlag = 0
        self.reserved = 0

        self.urlLen = 0  # if URL_FLAG
        self.urlString = ''  # if URL_FLAG

        self.esDescr = []  # if not URL_FLAG
        self.ociDescr = []  # if not URL_FLAG
        self.ipmpDescrPtr = []  # if not URL_FLAG
        self.ipmpDescr = []  # if not URL_FLAG

        self.extDescr = []

    def decode(self, file_strm):
        file_strm = super(ObjectDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(ObjectDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(ObjectDescriptor, self).size()

    def __str__(self):
        log_str = super(ObjectDescriptor, self).__str__()
        return log_str
