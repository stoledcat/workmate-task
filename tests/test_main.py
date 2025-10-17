import main
import pytest


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
    brands_dict = {"apple": [11.20, 4], "samsung": [13.6, 3], "xiaomi": [13.1, 3]}
    sorted_brands_list = main.sort_brands_list(brands_dict)
    for i in range(len(sorted_brands_list) - 1):
        assert sorted_brands_list[i][1] > sorted_brands_list[i + 1][1]


def test_one_brand():
    brands_dict = {"apple": [18.200000000000003, 4]}
    sorted_brands_list = main.sort_brands_list(brands_dict)
    assert sorted_brands_list == [["apple", 4.55]]


def test_read_from_directory():
    parser = main.main_parser(["--dir", "files", "--report", "average-rating"])
    assert parser.report == "average-rating"


def test_wrong_name_directory():
    argv = ["--dir", "filesss", "--report", "average-rating"]

    with pytest.raises(SystemExit) as exit_info:
        main.main_parser(argv)

    assert exit_info.value.code == "\nУказано неверное имя каталога\n"
