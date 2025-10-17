import main


def test_main_parser():
    parser = main.main_parser(
        ["--files", "products1.csv", "products2.csv", "--report", "average-rating"]
    )
    assert parser.files == ["products1.csv", "products2.csv"]
    assert parser.report == "average-rating"


def test_check_csv_files():
    list_csv = ["products1", "products2"]
    output_list_csv = main.check_csv_files(list_csv)
    assert output_list_csv == ["products1.csv", "products2.csv"]


def test_sort_brands_list():
    pass
