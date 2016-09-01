#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016/3/8 22:14'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import os

import mp4boxes
from fullbox import *
from mp4boxdesc import *

FLAG_SELF_CONTAINED = 0x000001


class Url(FullBox, object):
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
                self.location = file_strm.read_byte(left_size)
                self.offset += Int8ByteLen * left_size
            else:
                file_strm.seek(left_size, os.SEEK_CUR)
                self.offset += left_size

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['location'] = self.location
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\tlocation = %s" % (FullBox.__str__(self), self.location)
        return logstr


class Urn(FullBox, object):
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
                self.location = file_strm.read_byte(left_size)
                self.offset += Int8ByteLen * left_size
            else:
                self.name = file_strm.read_byte(left_size)
                self.offset += left_size

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['name'] = self.name
        dump_info['location'] = self.location
        return dump_info

    def __str__(self):
        logstr = "%s\n\t\t\t\t\t\tname = %s\n\t\t\t\t\t\tlocation = %s" % \
                 (FullBox.__str__(self), self.name, self.location)
        return logstr


class Dref(FullBox, object):
    """
    aligned(8) class DataReferenceBox extends FullBox(‘dref’, version = 0, 0) {
        unsigned int(32) entry_count;
        for (i=1; i <= entry_count; i++) {
             DataEntryBox(entry_version, entry_flags) data_entry;
        }
    }
    version - is an integer that specifies the version of this box
    entry_count - is an integer that counts the actual entries
    entry_version - is an integer that specifies the version of the entry format
    entry_flags - is a 24‐bit integer with flags; one flag is defined (x000001) which
                means that the media data is in the same file as the Movie Box containing
                this data reference.
    data_entry - is a URL or URN entry. Name is a URN, and is required in a URN entry.
                 Location is a URL, and is required in a URL entry and optional in a URN
                 entry, where it gives a location to find the resource with the given name.
                 Each is a null‐terminated string using UTF‐8 characters. If the self‐contained
                 flag is set, the URL form is used and no string is present; the box terminates
                 with the entry‐flags field. The URL type should be of a service that delivers
                 a file (e.g. URLs of type file, http, ftp etc.), and which services ideally
                 also permit random access. Relative URLs are permissible and are relative to
                 the file containing the Movie Box that contains this data reference.
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

        self.entry_count = file_strm.read_uint32()
        self.offset += UInt32ByteLen

        for cnt in range(self.entry_count):
            tmp_box = Box()
            file_strm = tmp_box.peek(file_strm)
            if tmp_box.type == FourCCMp4Url:
                data_entry = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = data_entry.decode(file_strm)
                self.offset += data_entry.Size()
                self.data_entries.append(data_entry)
            elif tmp_box.type == FourCCMp4Urn:
                data_entry = mp4boxes.MP4Boxes[tmp_box.type](self.offset, tmp_box)
                file_strm = data_entry.decode(file_strm)
                self.offset += data_entry.Size()
                self.data_entries.append(data_entry)
            else:
                file_strm.seek(tmp_box.Size(), os.SEEK_CUR)
                self.offset += tmp_box.Size()

        tmp_size = self.offset - self.box_offset
        if tmp_size != self.Size():
            file_strm.seek(self.Size() - tmp_size, os.SEEK_CUR)

        return file_strm

    def dump(self):
        dump_info = FullBox.dump(self)
        dump_info['entry_count'] = self.entry_count
        if None != self.data_entries:
            entries = {}
            for entry in self.data_entries:
                entries[entry.type] = entry.dump()
            dump_info['data_entries'] = entries
        return dump_info

    def __str__(self):
        logstr = "\t\t\t\t%s\n\t\t\t\tentry_count = %08ld(0x%016lx)\n\t\t\t\t" \
                 "entries = [" % (FullBox.__str__(self), self.entry_count,
                                  self.entry_count)
        for i in range(self.entry_count):
            logstr += "\n\t\t\t\t\t%08ld. %s" % (i, self.data_entries[i])
        logstr += "\n\t\t\t\t]\n"
        return logstr
