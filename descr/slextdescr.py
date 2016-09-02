#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:25:37'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from descrtagdesc import *
from pymp4def import *
from util.filestream import *


class SLExtensionDescriptor(object):
    """
    7.3.2.3.3 SLExtentionDescriptor Syntax
    abstract class SLExtensionDescriptor : bit(8) tag=0 {
    }

    class DependencyPointer extends SLExtensionDescriptor
        : bit(8) tag= DependencyPointerTag {
        bit(6) reserved;
        bit(1) mode;
        bit(1) hasESID;
        bit(8) dependencyLength;
        if (hasESID)
        {
            bit(16) ESID;
        }
    }
    class MarkerDescriptor extends SLExtensionDescriptor
        : bit(8) tag=DependencyMarkerTag {
        int(8) markerLength;
    }
    7.3.2.3.4 SLExtentionDescriptor Semantics
    SLExtensionDescriptor is an abstract class specified so as to be the base
    class of sl extensions.

    7.3.2.3.4.1 DependencyPointer Semantics
    DependencyPointer extends SLExtensionDescriptor and specifies that access
    units from this stream depend on another stream.

    If mode equals 0, the latter stream can be identified through the ESID field
    or if no ESID is present, using the dependsOn_ES_ID ESID, and access units
    from this stream will point to the decodingTimeStamps of that stream.

    If mode equals 1, access units from this stream will convey identifiers, for
    which the system (e.g. IPMP tools) are responsible to know whether dependent
    resources (e.g. keys) are available.

    In both cases, the length of this pointer or identifier is dependencyLength.

    If mode is 0 then dependencyLength shall be the length of the decodingTimeStamp.

    7.3.2.3.4.2 MarkerDescriptor Semantics
    MarkerDescriptor extends SLExtensionDescriptor and allows to tag access units
    so as to be able to refer to them independently from their decodingTimeStamp.

    markerLength – is the length for identifiers tagging access units.
    """

    def __init__(self, offset=0, descr_tag=0):
        self.descr_offset = offset
        self.offset = offset

        self.descr_tag = descr_tag
        self.sizeOfInstance = 0
        self.hdr_size = 0
        self.fullname = ''

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        self.descr_tag = file_strm.read_int8()
        self.offset += UInt8ByteLen

        self.fullname = DescrTagFullName[self.descr_tag]

        self.sizeOfInstance, self.hdr_size = parse_descr_len(file_strm)
        self.offset += self.hdr_size

        return file_strm

    def peek(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm
        self.descr_tag = file_strm.read_uint8()
        self.sizeOfInstance, self.hdr_size = parse_descr_len(file_strm)
        file_strm.seek(self.length() * -1, os.SEEK_CUR)
        return file_strm

    def size(self):
        return self.sizeOfInstance + self.length()

    def length(self):
        hdr_size_ = self.hdr_size
        tag_size_ = 1
        size_ = hdr_size_ + tag_size_
        return size_

    def dump(self):
        dump_info = {}
        dump_info['offset'] = self.descr_offset
        dump_info['tag'] = self.descr_tag
        dump_info['size'] = self.sizeOfInstance
        dump_info['hdr_size'] = self.hdr_size
        dump_info['fullname'] = self.fullname
        return dump_info

    def __str__(self):
        return "offset = 0x%016x, tag = %08ld(0x%08lx), fullname = %s" % \
               (self.descr_offset, self.descr_tag, self.descr_tag, self.fullname)
