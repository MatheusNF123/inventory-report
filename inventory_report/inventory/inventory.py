import csv
import json

import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


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
        with open(path) as file:
            xml_file = file.read()
            dict_xml = xmltodict.parse(xml_file)
            list_dict_product = dict_xml["dataset"]["record"]

            return list_dict_product


class Inventory:
    @staticmethod
    def import_data(path: str, typeReport):
        lista = OpenSupport(path).file

        if typeReport == "simples":
            return SimpleReport.generate(lista)
        if typeReport == "completo":
            return CompleteReport.generate(lista)
