#!/usr/bin/python
# encoding: utf-8


"""

"""

__file__ = '$Id$'
__author__ = 'szj0306'  # 志杰
__date__ = '2016-07-12 15:15:46'
__license__ = 'GPLv2'
__version__ = '$Revision$'
__email__ = 'jason860306@gmail.com'
# '$Source$'


from descrtagdef import *
from ipmpdatabaseclass import *


class IPMPParamDescriptor(IPMPDataBaseClass, object):
    """
    7.2.6.14.3.3.1 Syntax
    class IPMP_ParamtericDescription extends IPMP_Data_BaseClass
        : bit(8) tag = IPMP_ParamtericDescription_tag = 0x10
    {
        ByteArray descriptionComment;
        bit(8) majorVersion;
        bit(8) minorVersion;
        bit(32) numOfDescriptions;
        For (int i = 0; i<numOfDescriptions; i++){
            ByteArray class;
            ByteArray subClass;
            ByteArray typeData;
            ByteArray type;
            ByteArray addedData;
        }
    }
    7.2.6.14.3.3.2 Semantics
    class - class of the parametrically described tool, for example, decryption.
    subClass - sub-class of the parametrically described tool, for example,
               AES under decryption class.
    typeData - specific type data to describe a particular type of tool,
               for example, Block_length, to further specify a AES decryption tool.
    type - value of the type data above, for example, 128 for the Block_length.
    addedData - Any additional data which may help to further describe the
                parametrically defined tool.
    """

    class Description(object):
        """
        bit(32) numOfDescriptions;
        For (int i = 0; i<numOfDescriptions; i++){
            ByteArray class;
            ByteArray subClass;
            ByteArray typeData;
            ByteArray type;
            ByteArray addedData;
        }
        """

        def __init__(self):
            self.cls = None
            self.subcls = None
            self.typeData = None
            self.type = None
            self.addedData = None

    def __init__(self, descr_tag=DescrTag_IPMP_ParamtericDescription):
        super(IPMPParamDescriptor, self).__init__(descr_tag)
        self.descComment = 0
        self.majorVer = 0
        self.minorVer = 0
        self.numOfDesc = 0
        self.descs = []  # for i in self.numOfDesc

    def decode(self, file_strm):
        file_strm = super(IPMPParamDescriptor, self).decode(file_strm)
        if file_strm is None:
            # file_strm.seek(strm_pos, os.SEEK_SET)
            return file_strm

        return file_strm

    def dump(self):
        dump_info = super(IPMPParamDescriptor, self).dump()
        return dump_info

    def size(self):
        return super(IPMPParamDescriptor, self).size()

    def __str__(self):
        log_str = super(IPMPParamDescriptor, self).__str__()
        return log_str
