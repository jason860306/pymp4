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
        if isinstance(data, tuple):
            xml_elem = XmlEnc._encode_tuple(self, 'tuple', data)
        elif isinstance(data, list):
            xml_elem = XmlEnc._encode_list(self, 'list', data)
        elif isinstance(data, dict):
            xml_elem = XmlEnc._encode_dict(self, 'dict', data)
        else:
            pass  # raise
        root_elem.extend(xml_elem)

        self.xml_tree = ET.ElementTree(root_elem)

    def dump(self, xml_file):
        self.xml_tree.write(xml_file)

    def _encode_tuple(self, key, tuple_data):
        """
        :format k=(v, v, v, k=(), k={}, k=[])
        :param key:
        :param tuple_data:
        :return: xml_elem
        """
        xml_elem = ET.Element(key)
        for tdata in tuple_data:
            if not isinstance(tdata, basestring):
                ET.SubElement(xml_elem, "{0}".format(tdata))
            else:
                ET.SubElement(xml_elem, tdata)
        return xml_elem

    def _encode_list(self, key, list_data):
        """
        :format k=[v, v, k=(), k={}, k=[]]
        :param key:
        :param list_data:
        :return:
        """
        xml_elem = ET.Element(key)
        for ldata in list_data:
            if isinstance(ldata, dict):
                sub_elem = ET.SubElement(xml_elem, key)
                sub_elem.extend(XmlEnc._encode_dict(self, key, ldata))
            else:
                if not isinstance(ldata, basestring):
                    ET.SubElement(xml_elem, "{0}".format(ldata))
                else:
                    ET.SubElement(xml_elem, ldata)
        return xml_elem

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
            # elif isinstance(d, list):
            #     sub_elem = ET.SubElement(xml_elem, k)
            #     sub_elem.extend(XmlEnc._encode_list(self, k, d))
            # elif isinstance(d, tuple):
            #     sub_elem = ET.SubElement(xml_elem, k)
            #     sub_elem.extend(XmlEnc._encode_tuple(self, k, d))
            else:
                elem = ET.SubElement(xml_elem, k)
                if isinstance(d, basestring):
                    elem.text = d
                else:
                    elem.text = "{0}".format(d)
        return xml_elem
