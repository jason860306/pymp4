#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:32:45'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from descrtagdef import *
from slextdescr import *


class MarkerDescriptor(SLExtensionDescriptor, object):
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

    def __init__(self, offset=0, descr_tag=DescrTag_DependencyMarkerTag):
        super(MarkerDescriptor, self).__init__(offset, descr_tag)
        self.markerLen = 0
