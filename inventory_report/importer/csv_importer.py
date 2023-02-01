import csv
from inventory_report.importer.importer import Importer


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            dicts = csv.DictReader(file)
            lista = [i for i in dicts]
            return lista
