import xmltodict
from inventory_report.importer.importer import Importer


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            xml_file = file.read()
            dict_xml = xmltodict.parse(xml_file)
            list_dict_product = dict_xml["dataset"]["record"]

            return list_dict_product
