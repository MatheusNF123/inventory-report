from collections import Counter

from inventory_report.reports.simple_report import SimpleReport


class CompleteReport(SimpleReport):
    @staticmethod
    def generate(lista: list[dict]):
        resultSuperClass = SimpleReport.generate(lista)
        infoCompany = ""
        empresa = [i["nome_da_empresa"] for i in lista]

        numeroEmpresa = Counter(empresa).most_common()
        for i in numeroEmpresa:
            infoCompany += f"- {i[0]}: {i[1]}\n"

        return (
            f"{resultSuperClass}\n"
            f"Produtos estocados por empresa:\n"
            f"{infoCompany}"
        )
