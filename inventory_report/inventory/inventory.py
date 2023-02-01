import csv
import json

import xmltodict

from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


class Inventory:
    @staticmethod
    def import_data(path: str, typeReport):
        if ".csv" in path:
            lista = Inventory.open_csv(path)
        if ".json" in path:
            lista = Inventory.open_json(path)
        if ".xml" in path:
            lista = Inventory.open_xml(path)

        if typeReport == "simples":
            return SimpleReport.generate(lista)
        if typeReport == "completo":
            return CompleteReport.generate(lista)

    @staticmethod
    def open_csv(path):
        with open(path) as file:
            dicts = csv.DictReader(file)
            lista = [i for i in dicts]
            return lista

    @staticmethod
    def open_json(path):
        with open(path) as file:
            dicts = json.load(file)
            lista = [i for i in dicts]
            return lista

    @staticmethod
    def open_xml(path):
        with open(path) as file:
            xml_file = file.read()
            lista = []
            dict_xml = xmltodict.parse(xml_file)
            for i in dict_xml["dataset"]["record"]:
                dicts = {
                    "id": i["id"],
                    "nome_do_produto": i["nome_do_produto"],
                    "nome_da_empresa": i["nome_da_empresa"],
                    "data_de_fabricacao": i["data_de_fabricacao"],
                    "data_de_validade": i["data_de_validade"],
                    "numero_de_serie": i["numero_de_serie"],
                    "instrucoes_de_armazenamento": i[
                        "instrucoes_de_armazenamento"
                    ],
                }
                lista.append(dicts)

            return lista


# class OpenSupport:
#     def __init__(self, path):
#         if ".csv" in path:
#             self.__file = OpenCSV.open(path)
#         if ".json" in path:
#             self.__file = OpenJSON.open(path)
#         if ".xml" in path:
#             self.__file = OpenXML.open(path)

#     @property
#     def file(self):
#         return self.__file


# class OpenCSV:
#     @staticmethod
#     def open(path):
#         with open(path) as file:
#             dicts = csv.DictReader(file)
#             lista = [i for i in dicts]
#             return lista


# class OpenJSON:
#     @staticmethod
#     def open(path):
#         with open(path) as file:
#             dicts = json.load(file)
#             lista = [i for i in dicts]
#             return lista


# class OpenXML:
#     @staticmethod
#     def open(path):
#         with open(path) as file:
#             xml_file = file.read()
#             lista = []
#             dict_xml = xmltodict.parse(xml_file)
#             for i in dict_xml["dataset"]["record"]:
#                 dicts = {
#                     "id": i["id"],
#                     "nome_do_produto": i["nome_do_produto"],
#                     "nome_da_empresa": i["nome_da_empresa"],
#                     "data_de_fabricacao": i["data_de_fabricacao"],
#                     "data_de_validade": i["data_de_validade"],
#                     "numero_de_serie": i["numero_de_serie"],
#                     "instrucoes_de_armazenamento": i[
#                         "instrucoes_de_armazenamento"
#                     ],
#                 }
#                 lista.append(dicts)

#             return lista


# class Inventory:
#     @staticmethod
#     def import_data(path: str, typeReport):
#         lista = OpenSupport(path).file

#         if typeReport == "simples":
#             return SimpleReport.generate(lista)
#         if typeReport == "completo":
#             return CompleteReport.generate(lista)
