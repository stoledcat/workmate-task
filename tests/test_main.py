import main
import pytest
from parser import Parser


def test_main_parser():
    parser = main.main(["--files", "products1.csv", "products2.csv", "--report", "average-rating"])
    import argparse

    parser_obj = argparse.ArgumentParser(prog="BrandRatingAnalysis", description="Brand rating processing")
    parser_obj.add_argument("--files", nargs="+")
    parser_obj.add_argument("--report", choices=["average-rating"])
    parser_obj.add_argument("--dir", type=str)
    args = parser_obj.parse_args(["--files", "products1.csv", "products2.csv", "--report", "average-rating"])
    assert args.files == ["products1.csv", "products2.csv"]
    assert args.report == "average-rating"


def test_check_csv_files():
    list_csv = ["products1", "products2"]
    p = Parser()
    output_list_csv = p.check_csv_files(list_csv)
    assert output_list_csv == ["0 products1 .csv", "1 products2 .csv"]


def test_sort_brands_list():
    brands_dict = {"apple": [11.20, 4], "samsung": [13.6, 3], "xiaomi": [13.1, 3]}
    p = Parser()
    sorted_brands_list = p.sort_brands_list(brands_dict)
    for i in range(len(sorted_brands_list) - 1):
        assert sorted_brands_list[i][1] > sorted_brands_list[i + 1][1]


def test_one_brand():
    brands_dict = {"apple": [18.200000000000003, 4]}
    p = Parser()
    sorted_brands_list = p.sort_brands_list(brands_dict)
    assert sorted_brands_list == [("apple", 4.55)]


def test_read_from_directory(tmp_path):
    csv_file = tmp_path / "test.csv"
    csv_file.write_text("id,brand,model,rating\n1,apple,model1,4.7\n")

    import argparse

    parser_obj = argparse.ArgumentParser(prog="BrandRatingAnalysis", description="Brand rating processing")
    parser_obj.add_argument("--files", nargs="+")
    parser_obj.add_argument("--report", choices=["average-rating"])
    parser_obj.add_argument("--dir", type=str)
    args = parser_obj.parse_args(["--dir", str(tmp_path), "--report", "average-rating"])
    assert args.report == "average-rating"


def test_wrong_name_directory():
    argv = ["--dir", "filesss", "--report", "average-rating"]

    with pytest.raises(SystemExit) as exit_info:
        main.main(argv)

    assert exit_info.type == SystemExit

    assert exit_info.value.code == "\nУказано неверное имя каталога\n" or exit_info.value.code
