from inventory_report.inventory.inventory_iterator import InventoryIterator
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, typeReport: str):
        lista = self.importer.import_data(path)
        self.data += lista

        if typeReport == "simples":
            return SimpleReport.generate(self.data)
        if typeReport == "completo":
            return CompleteReport.generate(self.data)

    def __iter__(self):
        return InventoryIterator(self.data)
