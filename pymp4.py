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
        if fname is None:
            print "file is None"
            return

        self.filename = fname
        self.file_strm = None
        self.root = None

    def parse_mp4(self):
        file_size = os.path.getsize(self.filename)
        with open(self.filename, 'rb') as mp4_file:
            self.file_strm = FileStream(mp4_file)
            self.root = Root(self.file_strm, file_size)
            self.root.decode()
            self.root.rebuild_sample_table()

            out_file = os.path.splitext(self.filename)[0] + "." + \
                       self.root.get_major_brand()
            with open(out_file, 'wb') as es_file:
                for trk in self.root.get_tracks():
                    if trk.type != VideTrackType:
                        continue
                    for sample in trk.get_samples():
                        sample_data = self.root.get_sample_data(
                            sample.offset, sample.size, self.file_strm, trk.type)
                        es_file.write(sample_data)

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
                xml_enc = XmlEnc()
                xml_enc.encode(dump_info)
                xml_enc.dump(ofile)

    def __str__(self):
        meta_data = self.root.get_meta_data()
        logstr = "file = %s\nMetaData:\n%s\n%s" % \
                 (self.filename, Util.dump_dict(meta_data), self.root)
        return logstr


if __name__ == "__main__":

    arg_len = len(sys.argv)
    if arg_len != 2 and arg_len != 3:
        print "usage: %s mp4_file [dump_type(json|xml)]\n" % sys.argv[0]
        sys.exit(0)

    file_name = sys.argv[1]

    pymp4 = PyMp4(file_name)
    pymp4.parse_mp4()
    # print "mp4info: %s\n" % str(pymp4)

    if arg_len == 3:
        # pass
        dump_type = sys.argv[2]
        pymp4.dump(dump_type)