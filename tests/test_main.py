import main


def test_check_csv_files():
    list_csv = ["products1", "products2"]
    output_list_csv = main.check_csv_files(list_csv)
    assert output_list_csv == ["products1.csv", "products2.csv"]


def test_main():
    pass


def test_make_brands_dict():
    pass
