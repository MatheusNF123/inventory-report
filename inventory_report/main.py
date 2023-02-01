from inventory_report.importer.csv_importer import CsvImporter
from inventory_report.importer.json_importer import JsonImporter
from inventory_report.importer.xml_importer import XmlImporter
from inventory_report.inventory.inventory_refactor import InventoryRefactor
import sys
from inventory_report.reports.complete_report import CompleteReport

from inventory_report.reports.simple_report import SimpleReport


def main():
    inventory = ""
    if len(sys.argv) < 3:
        sys.stderr = "Verifique os argumentos"
        return

    if ".csv" in sys.argv[1]:
        inventory = InventoryRefactor(CsvImporter)

    elif ".json" in sys.argv[1]:
        inventory = InventoryRefactor(JsonImporter)

    elif ".xml" in sys.argv[1]:
        inventory = InventoryRefactor(XmlImporter)

    # else:
    #     raise ValueError("Arquivo com extensão invalida")
    inventory.import_data(sys.argv[1], sys.argv[2])
    lista = inventory.data

    if sys.argv[2] == "simples":
        print(SimpleReport.generate(lista))

    if sys.argv[2] == "completo":
        print(CompleteReport.generate(lista))


# if __name__ == "__main__":
#     main()
