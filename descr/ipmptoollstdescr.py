#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:01:21'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from descr.base_descriptor import *


class IPMPToolListDescriptor(BaseDescriptor, object):
    """
    7.2.6.14.3.1.1 Syntax
    class IPMP_ToolListDescriptor extends BaseDescriptor
        : bit(8) tag=IPMP_ToolsListDescrTag
    {
        IPMP_Tool ipmpTool[0 .. 255];
    }
    7.2.6.14.3.1.2 Semantics
    IPMP_Tool – a class describing a logical IPMP Tool required to
                access the content.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_IPMP_ToolsListDescrTag):
        super(IPMPToolListDescriptor, self).__init__(offset, descr_tag)
        self.ipmpTool = []

    def decode(self, file_strm):
        file_strm = super(IPMPToolListDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(IPMPToolListDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(IPMPToolListDescriptor, self).size()

    def __str__(self):
        log_str = super(IPMPToolListDescriptor, self).__str__()
        return log_str
