#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-06-30 18:11:30'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class ObjectDescriptorBase(object, BaseDescriptor):
    """
    7.2.6.2.1 Syntax
    abstract class ObjectDescriptorBase extends BaseDescriptor
        : bit(8) tag=[ObjectDescrTag..InitialObjectDescrTag] {
		// empty. To be filled by classes extending this class.
    }
    7.2.6.2.2 Semantics
    This is an abstract base class for the different types of
    object descriptor classes defined subsequently. The term
    “object descriptor” is used to generically refer to any
    such derived object descriptor class or instance thereof.
    """

    def __init__(self, descr_tag=DescrTag_ObjectDescrTag):
        BaseDescriptor.__init__(self, descr_tag)
