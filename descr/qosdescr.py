#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:49:08'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class QoSDescriptor(object, BaseDescriptor):
    """
    7.2.6.15.1 Syntax
    class QoS_Descriptor extends BaseDescriptor
        : bit(8) tag=QoS_DescrTag {
        bit(8) predefined;
        if (predefined==0) {
            QoS_Qualifier qualifiers[];
        }
    }
    7.2.6.15.2 Semantics
    The QoS_descriptor conveys the requirements that the ES has on the
    transport channel and a description of the traffic that this ES
    will generate. A set of predefined values is to be determined;
    customized values can be used by setting the predefined field to 0.

    predefined – a value different from zero indicates a predefined QoS
    profile according to Table 10.

    qualifier – an array of one or more QoS_Qualifiers.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_QoS_DescrTag):
        super(QoSDescriptor, self).__init__(offset, descr_tag)
        self.predef = 0
        self.qualifiers = []
