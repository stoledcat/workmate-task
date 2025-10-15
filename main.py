import argparse
# import csv
# import tabulate


def make_parser():
    parser = argparse.ArgumentParser(
        prog="BrandRatingAnalysis", description="Анализ рейтинга брендов"
    )
    
    parser.add_argument("--files", nargs="+")  # "+" 1 и больше аргументов
    parser.add_argument("--report")
    list_csv = parser.parse_args().files
    parse_csv_files(list_csv)


def parse_csv_files(list_csv):
    pass


if __name__ == "__main__":
    make_parser()
