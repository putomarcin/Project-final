# converters/xml_converter.py
from lxml import etree
import dicttoxml
import xmltodict

class XmlConverter:
    @staticmethod
    def read(file_path):
        try:
            with open(file_path, 'r') as file:
                return xmltodict.parse(file.read())
        except etree.XMLSyntaxError as e:
            raise ValueError(f"Invalid XML file: {str(e)}")
        except Exception as e:
            raise IOError(f"Error reading XML file: {str(e)}")

    @staticmethod
    def write(data, file_path):
        try:
            xml_data = dicttoxml.dicttoxml(data)
            with open(file_path, 'wb') as file:
                file.write(xml_data)
        except Exception as e:
            raise IOError(f"Error writing XML file: {str(e)}")
