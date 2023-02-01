import json
from inventory_report.importer.importer import Importer


class JsonImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".json" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            dicts = json.load(file)
            lista = [i for i in dicts]
            return lista
