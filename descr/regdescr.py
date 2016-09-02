#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 18:04:55'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from base_descriptor import *


class RegistrationDescriptor(BaseDescriptor, object):
    """
    The registration descriptor provides a method to uniquely and
    unambiguously identify formats of private data streams.

    7.2.6.17.1 Syntax
    class RegistrationDescriptor extends BaseDescriptor
        : bit(8) tag=RegistrationDescrTag {
        bit(32) formatIdentifier;
        bit(8) additionalIdentificationInfo[sizeOfInstance-4];
    }

    7.2.6.17.2 Semantics
    formatIdentifier – is a value obtained from a Registration Authority
    as designated by ISO.
    additionalIdentificationInfo – The meaning of additionalIdentificationInfo,
    if any, is defined by the assignee of that formatIdentifier, and once defined,
    shall not change.

    The registration descriptor is provided in order to enable users of
    ISO/IEC 14496-1 to unambiguously carry elementary streams with data
    whose format is not recognized by ISO/IEC 14496-1. This provision will
    permit ISO/IEC 14496-1 to carry all types of data streams while providing
    for a method of unambiguous identification of the characteristics of the
    underlying private data streams.

    In the following Subclause and Annex B, the benefits and responsibilities
    of all parties to the registration of private data format are outlined.

    7.2.6.17.2.1 Implementation of a Registration Authority (RA)

    ISO/IEC JTC 1/SC 29 shall issue a call for nominations from Member Bodies
    of ISO or National Committees of IEC in order to identify suitable
    organizations that will serve as the Registration Authority for the
    formatIdentifier as defined in this Subclause. The selected organization
    shall serve as the Registration Authority. The so-named Registration
    Authority shall execute its duties in compliance with Annex E of the JTC 1
    Directives. The registered private data formatIdentifier is hereafter
    referred to as the Registered Identifier (RID).
    Upon selection of the Registration Authority, JTC 1 shall require the
    creation of a Registration Management Group (RMG) which will review appeals
    filed by organizations whose request for an RID to be used in conjunction
    with ISO/IEC 14496-1 has been denied by the Registration Authority.
    Annex B provides information on the procedure for registering a unique
    format identifier.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_RegistrationDescrTag):
        super(RegistrationDescriptor, self).__init__(offset, descr_tag)
        self.formatIdentifier = 0
        self.additionIdentificationinfo = []

    def decode(self, file_strm):
        file_strm = super(RegistrationDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(RegistrationDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(RegistrationDescriptor, self).size()

    def __str__(self):
        log_str = super(RegistrationDescriptor, self).__str__()
        return log_str
