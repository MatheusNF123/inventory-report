from inventory_report.inventory.product import Product


def test_relatorio_produto():
    product = Product(
        "1",
        "farinha",
        "Farinini",
        "01-05-2021",
        "02-06-2023",
        "FM500",
        "ao abrigo de luz",
    )

    assert product.__repr__() == (
        f"O produto {product.nome_do_produto} fabricado em "
        f"{product.data_de_fabricacao} por {product.nome_da_empresa} "
        f"com validade até {product.data_de_validade} precisa ser armazenado "
        f"{product.instrucoes_de_armazenamento}."
    )
