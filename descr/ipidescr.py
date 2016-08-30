#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:35:41'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class IPIDescrPtr(object, BaseDescriptor):
    """
    7.2.6.12.1 Syntax
    class IPI_DescrPointer extends BaseDescriptor
        : bit(8) tag=IPI_DescrPointerTag {
        bit(16) IPI_ES_Id;
    }
    7.2.6.12.2 Semantics
    The IPI_DescrPointer class contains a reference to the elementary
    stream that includes the IP_IdentificationDataSets that are valid
    for this stream. This indirect reference mechanism allows to convey
    such descriptors only in one elementary stream while making references
    to it from any ES_Descriptor that shares the same information.

    ES_Descriptors for elementary streams that are intended to be accessible
    regardless of the availability of a referred stream shall explicitly
    include their IP_IdentificationDataSets instead of using an IPI_DescrPointer.

    IPI_ES_Id – the ES_ID of the elementary stream whose ES_Descriptor
    contains the IP Information valid for this elementary stream. If the
    ES_Descriptor for IPI_ES_Id is not available, the IPI status of this
    elementary stream is undefined.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_IPI_DescrPointerTag):
        super(IPIDescrPtr, self).__init__(offset, descr_tag)
        self.IPI_ES_ID = 0

    def decode(self, file_strm):
        return file_strm

    def dump(self):
        dump_info = super(IPIDescrPtr, self).dump()
        return dump_info

    def __str__(self):
        log_str = super(IPIDescrPtr, self).__str__()
        return log_str
