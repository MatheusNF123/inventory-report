from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(lista: list[dict]):
        dataF = min(lista, key=lambda x: x["data_de_fabricacao"])
        dataV = min(lista, key=lambda x: x["data_de_validade"])
        a = []
        for i in lista:
            a.append(i["nome_da_empresa"])

        numeroEmpresa = Counter(a).most_common()[0][0]

        return (
            f"""Data de fabricação mais antiga: {dataF['data_de_fabricacao']}
Data de validade mais próxima: {dataV['data_de_validade']}
Empresa com mais produtos: {numeroEmpresa}""")
