#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '-$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-18 17:46:13'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from ocidescr import *


class LanguageDescriptor(OCIDescriptor, object):
    """
    7.2.6.18.6.1 Syntax
    class LanguageDescriptor extends OCI_Descriptor
        : bit(8) tag=LanguageDescrTag {
        bit(24) languageCode;
    }
    7.2.6.18.6.2 Semantics
    This descriptor identifies the language of the corresponding
    audio/speech or text object that is being described.

    languageCode – contains the ISO 639-2:1998 bibliographic three
    character language code of the corresponding audio/speech or
    text object that is being described.
    """

    def __init__(self, offset=0, descr_tag=DescrTag_LanguageDescrTag):
        super(LanguageDescriptor, self).__init__(offset, descr_tag)
        self.langCode = 0

    def decode(self, file_strm):
        file_strm = super(LanguageDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(LanguageDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(LanguageDescriptor, self).size()

    def __str__(self):
        log_str = super(LanguageDescriptor, self).__str__()
        return log_str
