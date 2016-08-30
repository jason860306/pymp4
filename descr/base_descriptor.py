#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # Administrator
__date__ = '2016/6/29 17:58'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$' $Id$


from descrtagdesc import *
from util.filestream import *


class BaseDescriptor(object):
    """
    7.2.2.2.1 Syntax
    abstract aligned(8) expandable(228-1) class BaseDescriptor : bit(8) tag=0 {
        // empty. To be filled by classes extending this class.
    }
    7.2.2.2.2 Semantics

    This class is an abstract base class that is extended by the descriptor
    classes specified in 7.2.6. Each descriptor constitutes a self-describing
    class, identified by a unique class tag. This abstract base class establishes
    a common name space for the class tags of these descriptors. The values of
    the class tags are defined in Table 1. As an expandable class the size of
    each class instance in bytes is encoded and accessible through the instance
    variable sizeOfInstance (see 8.3.3).

    A class that allows the aggregation of classes of type BaseDescriptor
    may actually aggregate any of the classes that extend BaseDescriptor.

    NOTE — User private descriptors may have an internal structure, for example
    to identify the country or manufacturer that uses a specific descriptor.
    The tags and semantics for such user private descriptors may be managed by
    a registration authority if required.

    The following additional symbolic names are introduced:

    ExtDescrTagStartRange = 0x6A
    ExtDescrTagEndRange = 0xFE
    OCIDescrTagStartRange = 0x40
    OCIDescrTagEndRange = 0x5F

    """

    def __init__(self, offset=0, box=None, descr_tag=DescrTag_Forbidden00):
        self.descr_offset = offset
        self.offset = offset

        self.descr_tag = descr_tag

        self.fullname = DescrTagFullName[self.descr_tag]

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.descr_tag = file_strm.read_int8()
        self.offset += UInt8ByteLen

        return file_strm

    def dump(self):
        dump_info = {}
        dump_info['offset'] = self.descr_offset
        dump_info['tag'] = self.descr_tag
        dump_info['fullname'] = self.fullname
        return dump_info

    def __str__(self):
        return "offset = 0x%016x, tag = %08ld(0x%08lx), fullname = %s" % \
               (self.descr_offset, self.descr_tag, self.descr_tag, self.fullname)
