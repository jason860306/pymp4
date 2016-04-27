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
            self.root = Root(file_strm, filesize)
            self.root.decode()

    def dump(self, out_file=None):
        if None == out_file:
            return
        dump_json = {}
        dump_json['meta_data'] = self.root.get_meta_data()
        dump_json['mp4_info'] = self.root.dump()
        with open(out_file, 'wb') as ofile:
            ofile.write(JsonEnc().encode(dump_json))

    def __str__(self):
        meta_data = self.root.get_meta_data()
        logstr = "file = %s\nMetaData:\n%s\n%s" % \
                 (self.filename, Util.dump_dict(meta_data), self.root)
        return logstr


if __name__ == "__main__":
    arg_len = len(sys.argv)
    if (arg_len != 2) and (arg_len != 3):
        print "usage: %s mp4_file [out_file]\n" % sys.argv[0]
        sys.exit(0)

    filename = sys.argv[1]
    pymp4 = PyMp4(filename)
    pymp4.ParseMp4()

    if arg_len == 3:
        out_file = sys.argv[2]
        pymp4.dump(out_file)

    print "mp4info: %s\n" % str(pymp4)
