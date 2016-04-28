#!/usr/bin/python
# encoding: utf-8

"""

"""

__file__ = '$id$'
__author__ = 'szj0306'  # 志杰
__date__ = '4/28/2016 11:49:37'
__license__ = "Public Domain"
__version__ = '$Revision$'
__email__ = "jason860306@gmail.com"
# '$Source$'


try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class XmlEnc:
    """
    encode data to xml via ElementTree
    """

    def __init__(self):
        self.xml_tree = None

    def encode(self, data=None):
        if None == data:
            pass  # raise
        root_elem = ET.Element('root')

        xml_elem = None
        if isinstance(data, dict):
            xml_elem = XmlEnc._encode_dict(self, 'dict', data)
        else:
            pass  # raise
        root_elem.extend(xml_elem)

        self.xml_tree = ET.ElementTree(root_elem)

    def dump(self, xml_file):
        self.xml_tree.write(xml_file)

    def _encode_dict(self, key, dict_data):
        """
        :format k={k=v, k=v, k=v}
        :param key:
        :param dict_data:
        :return:
        """
        if not isinstance(dict_data, dict):
            pass  # raise
        xml_elem = ET.Element(key)
        for k, d in dict_data.items():
            if isinstance(d, dict):
                sub_elem = ET.SubElement(xml_elem, k)
                sub_elem.extend(XmlEnc._encode_dict(self, k, d))
            else:
                elem = ET.SubElement(xml_elem, k)
                if isinstance(d, basestring):
                    elem.text = d
                else:
                    elem.text = "{0}".format(d)
        return xml_elem
