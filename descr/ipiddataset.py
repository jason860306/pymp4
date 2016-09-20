#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:40:25'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from descr.base_descriptor import *


class IPIdentificationDataSet(BaseDescriptor, object):
    """
    7.2.6.9.1 Syntax
    abstract class IP_IdentificationDataSet extends BaseDescriptor
        : bit(8) tag=ContentIdentDescrTag..SupplContentIdentDescrTag
    {
        // empty. To be filled by classes extending this class.
    }
    7.2.6.9.2 Semantics
    This class is an abstract base class that is extended by the
    descriptor classes that implement IP identification. A descriptor
    that allows to aggregate classes of type IP_IdentificationDataSet
    may actually aggregate any of the classes that extend
    IP_IdentificationDataSet.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_ContentIdentDescrTag):
        super(IPIdentificationDataSet, self).__init__(offset, descr_tag)

    def decode(self, file_strm):
        file_strm = super(IPIdentificationDataSet, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(IPIdentificationDataSet, self).dump()
        return dump_info

    def size(self):
        return super(IPIdentificationDataSet, self).size()

    def __str__(self):
        log_str = super(IPIdentificationDataSet, self).__str__()
        return log_str
