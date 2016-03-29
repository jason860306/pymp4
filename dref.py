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

FLAG_SELF_CONTAINED = 0x000001


class DataEntryUrlBox(FullBox):
    """
    aligned(8) class DataEntryUrlBox (bit(24) flags) extends FullBox(‘url ’, version = 0, flags) {
        string location;
    }
    // If the self‐contained flag is set, the URL form is used and no string is present;
    // Each is a null‐terminated string using UTF‐8 characters.
    // the box terminates with self‐contained flag isthe entry‐flags field.
    """

    def __init__(self, offset=0, box=None):
        FullBox.__init__(self, offset, box)
        self.location = ""

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)
        left_size = self.Size() - self.GetLength()
        if left_size > 0:
            if self.flags != FLAG_SELF_CONTAINED:
                self.location = file_strm.ReadByte(left_size)
                self.offset += Int8ByteLen * left_size
            else:
                file_strm.Seek(left_size, os.SEEK_CUR)
                self.offset += left_size

        return file_strm

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\tlocation = %s" % (FullBox.__str__(self), self.location)
        return logstr


class DataEntryUrnBox(FullBox):
    """
    aligned(8) class DataEntryUrnBox (bit(24) flags) extends FullBox(‘urn ’, version = 0, flags) {
        string name;
        string location;
    }
    // If the self‐contained flag is set, the URL form is used and no string is present;
    // Each is a null‐terminated string using UTF‐8 characters.
    // the box terminates with self‐contained flag isthe entry‐flags field.
    """

    def __init__(self, offset=0, box=None):
        FullBox.__init__(self, offset, box)
        self.name = ""
        self.location = ""

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)
        left_size = self.Size() - self.GetLength()
        if left_size > 0:
            if self.flags != FLAG_SELF_CONTAINED:
                self.location = file_strm.ReadByte(left_size)
                self.offset += Int8ByteLen * left_size
            else:
                self.name = file_strm.ReadByte(left_size)
                self.offset += left_size

        return file_strm

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\tname = %s\n\t\t\t\t\t\tlocation = %s" % \
                 (FullBox.__str__(self), self.name, self.location)
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

    def __init__(self, offset=0, box=None):
        if isinstance(box, Box):
            Box.__init__(self, offset, box)
        elif isinstance(box, FullBox):
            FullBox.__init__(self, offset, box)

        self.entry_count = 0
        self.data_entries = []

    def decode(self, file_strm):
        if file_strm is None:
            print "file_strm is None"
            return file_strm

        file_strm = FullBox.decode(self, file_strm)

        self.entry_count = file_strm.ReadUInt32()
        self.offset += UInt32ByteLen

        for cnt in range(self.entry_count):
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Url:
                data_entry = DataEntryUrlBox(self.offset, tmp_box)
                file_strm = data_entry.decode(file_strm)
                self.offset += data_entry.Size()
                self.data_entries.append(data_entry)
            elif tmp_box.type == FourCCMp4Urn:
                data_entry = DataEntryUrnBox(self.offset, tmp_box)
                file_strm = data_entry.decode(file_strm)
                self.offset += data_entry.Size()
                self.data_entries.append(data_entry)
            else:
                file_strm.Seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.Seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)\n\t\t\t\tentries = [" % \
                 (FullBox.__str__(self), self.entry_count, self.entry_count)
        for i in range(self.entry_count):
            logstr += "\n\t\t\t\t\t%08ld. %s" % (i, self.data_entries[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
