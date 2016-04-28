#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # szj0306
__date__ = '3/11/16 5:30 PM'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


import sys

from jsoncodec import *
from root import *
from util import Util
from xmlcodec import *


class PyMp4:
    """
    the main class to parse a mp4 file
    """

    def __init__(self, fname):
        if fname == None:
            print "file == None"
            return

        self.filename = fname
        self.root = None

    def ParseMp4(self):
        filesize = os.path.getsize(self.filename)
        with open(self.filename, 'rb') as mp4_file:
            file_strm = FileStream(mp4_file)
            cur_pos = file_strm.Tell()
            file_strm.Seek(0, os.SEEK_SET)
            self.root = Root(file_strm, filesize)
            self.root.decode()

    def dump(self, dump_type=DUMP_TYPE_JSON):
        dump_info = {}
        dump_info['file'] = self.filename
        dump_info['meta_data'] = self.root.get_meta_data()
        dump_info['mp4_info'] = self.root.dump()

        out_file = os.path.splitext(self.filename)[0] + "." + dump_type
        with open(out_file, 'wb') as ofile:
            if dump_type == DUMP_TYPE_JSON:
                ofile.write(JsonEnc().encode(dump_info))
            elif dump_type == DUMP_TYPE_XML:
                xmlEnc = XmlEnc()
                xmlEnc.encode(dump_info)
                xmlEnc.dump(ofile)

    def __str__(self):
        meta_data = self.root.get_meta_data()
        logstr = "file = %s\nMetaData:\n%s\n%s" % \
                 (self.filename, Util.dump_dict(meta_data), self.root)
        return logstr


if __name__ == "__main__":

    arg_len = len(sys.argv)
    if (arg_len != 2) and (arg_len != 3):
        print "usage: %s mp4_file [dump_type(json|xml)]\n" % sys.argv[0]
        sys.exit(0)

    filename = sys.argv[1]
    dumptype = sys.argv[2]

    pymp4 = PyMp4(filename)
    pymp4.ParseMp4()

    if arg_len == 3:
        pymp4.dump(dumptype)

        # print "mp4info: %s\n" % str(pymp4)
