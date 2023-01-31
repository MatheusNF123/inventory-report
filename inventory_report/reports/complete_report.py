from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(lista: list[dict]):
        resultSuperClass = SimpleReport.generate(lista)
        empresa = []
        stra = ""
        for i in lista:
            empresa.append(i["nome_da_empresa"])

        numeroEmpresa = Counter(empresa).most_common()
        for i in numeroEmpresa:
            stra += f"- {i[0]}: {i[1]}\n"

        return (
            f"{resultSuperClass}\n"
            f"Produtos estocados por empresa:\n"
            f"{stra}"
        )
