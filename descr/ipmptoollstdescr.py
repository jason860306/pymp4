#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:01:21'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class IPMPToolListDescriptor(object, BaseDescriptor):
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

    def __init__(self, descr_tag=DescrTag_IPMP_ToolsListDescrTag):
        super(IPMPToolListDescriptor, self).__init__(descr_tag)
        self.ipmpTool = []
