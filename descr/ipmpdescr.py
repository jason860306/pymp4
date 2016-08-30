#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-06 14:30:43'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class IPMPDescriptor(object, BaseDescriptor):
    """
    7.2.6.14.1 Syntax
    class IPMP_Descriptor() extends BaseDescriptor
        : bit(8) tag = IPMP_DescrTag
    {
        bit(8) IPMP_DescriptorID;
        unsigned int(16) IPMPS_Type;
        if (IPMP_DescriptorID == 0xFF && IPMPS_Type == 0xFFFF){
            bit(16) IPMP_DescriptorIDEx;
            bit(128) IPMP_ToolID;
            bit(8) controlPointCode;
            if (controlPointCode > 0x00)
                bit(8) sequenceCode;
            IPMP_Data_BaseClass IPMPX_data[];
        }
        else if (IPMPS_Type == 0)
            bit(8) URLString[sizeOfInstance-3];
        else
            bit(8) IPMP_data[sizeOfInstance-3];
    }
    7.2.6.14.2 Semantics
    The IPMP_Descriptor carries IPMP information for one or more IPMP System
    or IPMP Tool instances. It shall also contain optional instantiation
    information for one or more IPMP Tool instances.

    IPMP_Descriptors are conveyed in either initial object descriptors, object
    descriptors or object descriptor streams via IPMP_DescriptorUpdate commands.
    Multiple definitions of the same IPMP_Descriptor within a single
    IPMP_DescriptorUpdate command or a single decoder specific information
    structure for an IPMP stream are not allowed. The behavior in such a situation
    is undefined. Note that, however, an IPMP_Descriptor may be modified/updated
    through subsequent IPMP_DescriptorUpdate commands received in the OD stream.
    IPMP_Descriptors shall be referenced by object descriptors or ES_Descriptors,
    using IPMP_DescriptorPointer.

    IPMP_DescriptorID - a unique ID for this IPMP_Descriptor within its name scope.
    Values of “0x00” and “0xFF” are forbidden in the case of signaling an extension
    descriptor. The scope of the IPMP_DescriptorID is suggested to be the same as
    the OD, or IOD in which is it contained. IPMP_DescriptorID is for use in systems
    conforming to the previous definition as well as a signal indicating the use of
    IPMP_DescriptorIDEx for IPMP extensions.

    Note 1: Although it is possible to implement an application supporting both the
    use of IPMP protection schemes defined through the use of IPMP_Descriptors some
    of which contain IPMP_DescriptorID and some of which contain IPMP_DescriptorIDEx
    to protect separate streams, the behavior of the association of a single stream
    to both types of IPMP_Descriptors is undefined.

    IPMP_DescriptorIDEx - a unique ID for this IPMP_Descriptor within its name scope.
    Values of “0x0000” and “0xFFFF” are forbidden. The scope of the IPMP_DescriptorIDEx
    is suggested to be the same as the OD, or IOD in which is it contained.

    IPMP_ToolID – the IPMP_ToolID of the IPMP Tool described by this IPMP_Descriptor.
    A zero, “0” value does not correspond to an IPMP Tool but is used to indicate the
    presence of a URL.

    URLString[] - contains a UTF-8 encoded URL that shall point to the location of a
    remote IPMP_Descriptor. If the IPMPS_Type of this IPMP_Descriptor is 0, another
    URL is referenced. This process continues until an IPMP_Descriptor with a non-zero
    IPMPS_Type is accessed.

    controlPointCode – specifies the IPMP control point at which the IPMP Tool resides,
    and is one of the following values:

    Note 2: The only difference between receiving composition units before the CB and
    after the CB in the MPEG-4 Systems decoder model is the order in which the units
    are received when the associated DTS is different from the CTS; in this case the
    decoding order is different from the composition order. For example, suppose that
    a watermark payload is embedded in more than a single video frame; if the watermark
    payload was embedded in decoding order, it has to be extracted before the CB;
    instead, if it was embedded in composition order, it has to be extracted after the CB.

    Note 3: For streams of type “0x01”, ObjectDescriptor and of type “0x02”,
    ClockReferenceStream, only a controlPointCode of “0x00”, “0x01” or the range
    “0xE0-0xFE” are meaningful. sequenceCode - The higher the sequence code, the
    higher the sequencing priority of the IPMP Tool instance at the given control
    point. Thus the tool with the highest sequenceCode for a given control point
    on a given stream shall process data first for that control point for that stream.
    Two tools shall not have the same sequence number at the same control point for
    the same stream.

    IPMPX_data - The IPMP data that is extended from IPMP_Data_BaseClass, for the
    given IPMP tool.

    IPMP_data – Data of unspecified format.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_IPMP_DescrTag):
        super(IPMPDescriptor, self).__init__(offset, descr_tag)
        self.ipmpDescrId = 0
        self.ipmpsType = 0
        self.ipmpDescrIdEx = 0  # if (IPMP_DescriptorID == 0xFF && IPMPS_Type == 0xFFFF)
        self.ipmpToolId = 0  # if (IPMP_DescriptorID == 0xFF && IPMPS_Type == 0xFFFF)
        self.ctrlPointCode = 0  # if (IPMP_DescriptorID == 0xFF && IPMPS_Type == 0xFFFF)
        self.sequencdCode = 0  # if (IPMP_DescriptorID == 0xFF && IPMPS_Type == 0xFFFF)
        self.ipmpxData = []  # if (IPMP_DescriptorID == 0xFF && IPMPS_Type == 0xFFFF)
        self.urlString = ''  # if (IPMPS_Type == 0)
        self.ipmpData = ''  # if (IPMPS_Type != 0)
