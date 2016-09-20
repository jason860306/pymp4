#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 19:06:53'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from descr.base_descriptor import *


class OCIDescriptor(BaseDescriptor, object):
    """
    7.2.6.18.2.1 Syntax
    abstract class OCI_Descriptor extends BaseDescriptor
        : bit(8) tag= OCIDescrTagStartRange .. OCIDescrTagEndRange
    {
        // empty. To be filled by classes extending this class.
    }
    7.2.6.18.2.2 Semantics
    This class is an abstract base class that is extended by the classes
    specified in the subsequent Clauses. A descriptor or an OCI_Event
    that allows to aggregate classes of type OCI_Descriptor may actually
    aggregate any of the classes that extend OCI_Descriptor.
    """

    def __init__(self, descr_tag=DescrTag_OCIDescrTagStartRange):
        super(OCIDescriptor, self).__init__(descr_tag)

    def decode(self, file_strm):
        file_strm = super(OCIDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(OCIDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(OCIDescriptor, self).size()

    def __str__(self):
        log_str = super(OCIDescriptor, self).__str__()
        return log_str
