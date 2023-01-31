from collections import Counter
# from inventory_report.reports.simple_report import SimpleReport


class CompleteReport:
    @staticmethod
    def generate(lista: list[dict]):
        empresa = []
        for i in lista:
            empresa.append(i["nome_da_empresa"])

        numeroEmpresa = Counter(empresa).most_common()
        return numeroEmpresa


# super().generate(lista)
print(
    CompleteReport.generate(
        [
            {
                "id": 1,
                "nome_do_produto": "MESA",
                "nome_da_empresa": "Forces of Nature",
                "data_de_fabricacao": "2022-05-04",
                "data_de_validade": "2023-02-09",
                "numero_de_serie": "FR48",
                "instrucoes_de_armazenamento": "Conservar ao abrigo de luz",
            }
        ]
    )
)
