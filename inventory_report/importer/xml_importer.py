import xmltodict
from inventory_report.importer.importer import Importer

# from inventory_report.reports.simple_report import SimpleReport
# from inventory_report.reports.complete_report import CompleteReport


class XmlImporter(Importer):
    @staticmethod
    def import_data(path):
        if ".xml" not in path:
            raise ValueError("Arquivo inválido")

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
            # if typeReport == "simples":
            #     return SimpleReport.generate(lista)

            # if typeReport == "completo":
            #     return CompleteReport.generate(lista)
