import lxml.etree as ET

with open("./xml_resources/annotation_schema.xsd") as f:
    export_annotation_xml_response_schema = ET.XMLSchema(ET.parse(f))
with open("./xml_resources/export_annotation_transform.xsl") as f:
    export_annotation_transform = ET.XSLT(ET.parse(f))


def export_annotation_validate_and_transform(xml_string):
    xml_root = ET.fromstring(xml_string)
    if not export_annotation_xml_response_schema.validate(xml_root):
        raise Exception("Xml response validation failed!")
    transformed_xml_root = export_annotation_transform(xml_root)
    return ET.tostring(transformed_xml_root, pretty_print=True)
