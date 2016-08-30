#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-06 14:58:01'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class ExtDescriptor(object, BaseDescriptor):
    """
    7.2.6.16.1 Syntax
    abstract class ExtensionDescriptor extends BaseDescriptor
    : bit(8) tag = ExtensionProfileLevelDescrTag,
                   ExtDescrTagStartRange .. ExtDescrTagEndRange {
        // empty. To be filled by classes extending this class.
    }
    7.2.6.16.2 Semantics
    This class is an abstract base class that may be extended for
    defining additional descriptors in future. The available range
    of class tag values allow ISO defined extensions as well as
    private extensions. A descriptor that allows to aggregate
    ExtensionDescriptor classes may actually aggregate any of the
    classes that extend ExtensionDescriptor. Extension descriptors
    may be ignored by a terminal that conforms to ISO/IEC 14496-1.
    """

    def __init__(self, descr_tag=DescrTag_ExtensionProfileLevelDescrTag):
        super(ExtDescriptor, self).__init__(descr_tag)
