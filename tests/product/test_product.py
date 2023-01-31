from inventory_report.inventory.product import Product


def test_cria_produto():
    produto = Product(
        "1",
        "nome",
        "empresa",
        "2023-01-20",
        "2024-01-20",
        "2521",
        "armazenar no teste por ate 2 dias",
    )
    assert produto.id == "1"
    assert produto.nome_do_produto == "nome"
    assert produto.nome_da_empresa == "empresa"
    assert produto.data_de_fabricacao == "2023-01-20"
    assert produto.data_de_validade == "2024-01-20"
    assert produto.numero_de_serie == "2521"
    assert (
        produto.instrucoes_de_armazenamento
        == "armazenar no teste por ate 2 dias"
    )
