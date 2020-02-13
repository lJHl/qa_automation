# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
from framework.singleton import Singleton


class XmlParser(metaclass=Singleton):

    @staticmethod
    def convert_xml_to_dict(xml):
        dict = {}
        root = ET.fromstringlist(xml)
        for one in root:
            value = list(one.attrib.values())
            any_dict = {}
            for two in one.getchildren():
                any_dict.update({two.tag: two.text})
            dict[value[0]] = any_dict
        return dict
