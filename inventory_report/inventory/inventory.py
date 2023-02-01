import csv
import json
from xml.etree import cElementTree

# import xmltodict

# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class OpenSupport:
    def __init__(self, path):
        if ".csv" in path:
            self.__file = OpenCSV.open(path)
        if ".json" in path:
            self.__file = OpenJSON.open(path)
        if ".xml" in path:
            self.__file = OpenXML.open(path)

    @property
    def file(self):
        return self.__file


class OpenCSV:
    @staticmethod
    def open(path):
        with open(path) as file:
            dicts = csv.DictReader(file)
            lista = [i for i in dicts]
            return lista


class OpenJSON:
    @staticmethod
    def open(path):
        with open(path) as file:
            dicts = json.load(file)
            lista = [i for i in dicts]
            return lista


class OpenXML:
    @staticmethod
    def open(path):
        # with cElementTree.parse(path) as file:
        xml_file = cElementTree.parse(path)
        root_xml = xml_file.getroot()
        dict_xml = [chave.attrib for chave in root_xml]
        return dict_xml


class Inventory:
    @staticmethod
    def import_data(path: str, typeReport):
        lista = OpenSupport(path).file
        return lista
        # if typeReport == "simples":
        #     return SimpleReport.generate(lista)
        # if typeReport == "completo":
        #     return CompleteReport.generate(lista)


print(Inventory.import_data("inventory_report/data/inventory.xml", "simples"))
