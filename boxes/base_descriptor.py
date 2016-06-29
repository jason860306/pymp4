#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # Administrator
__date__ = '2016/6/29 17:58'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from descrtagdef import *


class BaseDescriptor:
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

    def __init__(self, descr_tag=DescrTagForbidden00):
        self.descriptor_tag = descr_tag
