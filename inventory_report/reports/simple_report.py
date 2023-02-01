from collections import Counter


class SimpleReport:
    @staticmethod
    def generate(lista: list[dict]):
        data = min(lista, key=lambda x: x["data_de_fabricacao"])
        dataV = min(lista, key=lambda x: x["data_de_validade"])
        empresa = [i["nome_da_empresa"] for i in lista]

        numeroEmpresa = Counter(empresa).most_common()[0][0]

        return f"""Data de fabricação mais antiga: {data['data_de_fabricacao']}
Data de validade mais próxima: {dataV['data_de_validade']}
Empresa com mais produtos: {numeroEmpresa}"""
