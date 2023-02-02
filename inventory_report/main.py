from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys


def main():
    if len(sys.argv) < 3:
        return print("Verifique os argumentos", file=sys.stderr)
    typeFile = sys.argv[1].split(".")[1]

    dict_report = {
        "csv": InventoryRefactor(CsvImporter),
        "json": InventoryRefactor(JsonImporter),
        "xml": InventoryRefactor(XmlImporter),
    }
    try:
        inventory = dict_report[typeFile]
    except KeyError:
        ValueError("tipo do arquivo errado")

    lista = inventory.import_data(sys.argv[1], sys.argv[2])

    print(lista, end="")
