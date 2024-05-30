import xml.etree.ElementTree as ET

def parse_xsd(file_path):
    tree = ET.parse(file_path)
    root = tree.getroot()
    elements = []

    for element in root.iter():
        element_info = {
            'tag': element.tag,
            'attributes': list(element.attrib.keys()),
            'text_length': len(element.text) if element.text else 0,
            'name': element.attrib.get('name', element.tag)  # Use tag if name attribute is missing
        }
        elements.append(element_info)

    return elements