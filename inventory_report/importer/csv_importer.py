import csv
from inventory_report.importer.importer import Importer

# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class CsvImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".csv" not in path:
            raise ValueError("Arquivo inválido")

        with open(path) as file:
            dicts = csv.DictReader(file)
            lista = [i for i in dicts]
            return lista
        # if typeReport == "simples":
        #     return SimpleReport.generate(lista)
        # if typeReport == "completo":
        #     return CompleteReport.generate(lista)
