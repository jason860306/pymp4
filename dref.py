#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/8 22:14'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


from fullbox import *
from util import *


class DataEntryBox(FullBox):
    """
    """
    pass


class DataEntryUrlBox(DataEntryBox):
    """
    aligned(8) class DataEntryUrlBox (bit(24) flags) extends FullBox(‘url ’, version = 0, flags) {
        string location;
    }
    """

    def __init__(self):
        DataEntryBox.__init__(self)
        self.location = ""

    def decode(self, file=None):
        DataEntryBox.decode(self, file)

        file_strm = Util(file)

        # self.location

    def __str__(self):
        logstr = "%s, location = %s" % (DataEntryBox.__str__(self), self.location)
        return logstr


class DataEntryUrnBox(DataEntryBox):
    """
    aligned(8) class DataEntryUrnBox (bit(24) flags) extends FullBox(‘urn ’, version = 0, flags) {
        string name;
        string location;
    }
    """

    def __init__(self):
        DataEntryBox.__init__(self)
        self.name = ""
        self.location = ""

    def decode(self, file=None):
        DataEntryBox.decode(self, file)

    def __str__(self):
        logstr = "%s, name = %s, location = %s" % \
                 (DataEntryBox.__str__(self), self.name, self.location)
        return logstr


class Dref(FullBox):
    """
    aligned(8) class DataReferenceBox extends FullBox(‘dref’, version = 0, 0) {
        unsigned int(32) entry_count;
        for (i=1; i <= entry_count; i++) {
             DataEntryBox(entry_version, entry_flags) data_entry;
        }
    }
    """

    def __init__(self):
        FullBox.__init__(self)
        self.entry_count = 0
        self.data_entries = []

    def decode(self, file=None):
        FullBox.decode(self, file)

        file_strm = Util(file)

        self.entry_count = file_strm.read_uint32_lit()
        for cnt in range(self.entry_count):
            data_entry = DataEntryBox()
            data_entry.decode(file_strm)
            self.data_entries.append(data_entry)

    def __str__(self):
        logstr = "%s, entry_count = %d, entries = [" % \
                 (FullBox.__str__(self), self.entry_count)
        for i in range(self.entry_count):
            logstr += "%d. %s, ], [" % (i, self.data_entries[i])
        logstr += "]"
        return logstr
