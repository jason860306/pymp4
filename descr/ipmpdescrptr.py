#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-06 14:24:35'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class IPMPDescrPointer(object, BaseDescriptor):
    """
    7.2.6.13.1 Syntax
    class IPMP_DescriptorPointer extends BaseDescriptor
        : bit(8) tag = IPMP_DescrPtrTag
    {
        bit(8) IPMP_DescriptorID;
        if (IPMP_DescriptorID == 0xff){
            bit(16) IPMP_DescriptorIDEx;
            bit(16) IPMP_ES_ID;
        }
    }
    7.2.6.13.2 Semantics
    The IPMP_DescriptorPointer appears in the ipmpDescPtr section of an OD or
    ESD structures.

    The presence of this descriptor in an object descriptor indicates that all
    streams referred to by embedded ES_Descriptors are subject to protection
    and management by the IPMP System or IPMP Tool specified in the referenced
    IPMP_Descriptor.

    The presence of this descriptor in an ES_Descriptor indicates that the stream
    associated with this descriptor is subject to protection and management by
    the IPMP System or IPMP Tool specified in the referenced IPMP_Descriptor.

    The IPMP_DescriptorPointer supports the ability to identify which specific
    IPMP stream or streams the IPMP tools declared in the corresponding
    IPMP_Descriptor, identified by the IPMP_DescriptorIDEx, wish to receive.
    Multiple IPMP tools may receive updates from the same stream.

    IPMP_DescriptorID is the ID of the IPMP_Descriptor being referred to.
    The bit(8) field is to support backward compatibility, for which support for
    extended IPMP stream association is not provided for.

    IPMP_DescriptorIDEx is the ID of the IPMP_Descriptor being referred to.
    The bit(16) field refers to extension defined IPMP_Descriptors and also
    supporting the extended IPMP stream association.

    IPMP_ES_ID is the id of an IPMP stream that may carry messages intended to
    the tool pointed to by IPMP_DescriptorIDEx. In case more than one IPMP stream
    is needed to feed the IPMP tool, several IPMP_DescriptorPointer can be given
    with the same IPMP_DescriptorIDEx and different IPMP_ES_ID. If the IPMP_ES_ID
    is null, it means the IPMP tool does not require an IPMP stream. A value of
    2^16-1 for IPMP_ES_ID indicates that this field should be ignored, meaning that
    the tool pointed to by IPMP_DescriptorIDEx may receive messages from any IPMP
    stream within the presentation.

    The list of IPMP streams identified by occurrences of the IPMP_ES_ID field (with
    a value different than 2^16-1) for a single IPMP_DescriptorIDEx is exhaustive:
    the IPMP tool identified by the IPMP_DescriptorIDEx may not receive messages from
    any other IPMP streams than the ones identified in this list. In order to facilitate
    editing, the IPMP_DescriptorPointer must be modified when stored in a file: the
    IPMP_ES_ID field must be replaced with the corresponding index in the OD track’s
    ‘mpod’ table as defined in ISO/IEC 14496-14.
    """

    def __init__(self, descr_tag):
        super(IPMPDescrPointer, self).__init__(descr_tag)
        self.ipmpDescrId = 0
        self.ipmpDescrIdEx = 0  # if (IPMP_DescriptorID == 0xff)
        self.ipmpESId = 0  # if (IPMP_DescriptorID == 0xff)
