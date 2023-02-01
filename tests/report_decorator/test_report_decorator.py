from inventory_report.reports.colored_report import ColoredReport
from inventory_report.reports.simple_report import SimpleReport
from inventory_report.reports.complete_report import CompleteReport


def test_decorar_relatorio():
    lista = [
        {
            "id": "1",
            "nome_do_produto": "farinha",
            "nome_da_empresa": "Farinini",
            "data_de_fabricacao": "01-05-2021",
            "data_de_validade": "02-06-2023",
            "numero_de_serie": "FM500",
            "instrucoes_de_armazenamento": "ao abrigo de luz",
        },
        {
            "id": "2",
            "nome_do_produto": "torrada",
            "nome_da_empresa": "Farinini",
            "data_de_fabricacao": "02-05-2021",
            "data_de_validade": "20-06-2023",
            "numero_de_serie": "FM500",
            "instrucoes_de_armazenamento": "ao abrigo de luz",
        },
    ]

    simpleReport = ColoredReport(SimpleReport)
    completeReport = ColoredReport(CompleteReport)

    coloredReporSimple = simpleReport.generate(lista)
    coloredReportCompĺete = completeReport.generate(lista)

    # test da class ColoredReport passando SimpleReport
    assert (
        "\033[32mData de fabricação mais antiga:\033[0m" in coloredReporSimple
    )
    assert "\033[36m01-05-2021\033[0m" in coloredReporSimple

    assert (
        "\033[32mData de validade mais próxima:\033[0m" in coloredReporSimple
    )
    assert "\033[36m02-06-2023\033[0m" in coloredReporSimple

    assert "\033[32mEmpresa com mais produtos:\033[0m" in coloredReporSimple
    assert "\033[31mFarinini\033[0m" in coloredReporSimple

    # test da class ColoredReport passando CompleteReport
    assert (
        "\033[32mData de fabricação mais antiga:\033[0m"
        in coloredReportCompĺete
    )
    assert "\033[36m01-05-2021\033[0m" in coloredReportCompĺete

    assert (
        "\033[32mData de validade mais próxima:\033[0m"
        in coloredReportCompĺete
    )
    assert "\033[36m02-06-2023\033[0m" in coloredReportCompĺete

    assert "\033[32mEmpresa com mais produtos:\033[0m" in coloredReportCompĺete
    assert "\033[31mFarinini\033[0m" in coloredReportCompĺete
