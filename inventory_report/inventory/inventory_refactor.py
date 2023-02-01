# from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.inventory.inventory_iterator import InventoryIterator


class InventoryRefactor:
    def __init__(self, importer):
        self.importer = importer
        self.data = []

    def import_data(self, path: str, typeReport: str):
        lista = self.importer.import_data(path)

        self.data += lista

    def __iter__(self):
        return InventoryIterator(self.data)
