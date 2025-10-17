import argparse
import csv

from tabulate import tabulate


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="BrandRatingAnalysis", description="Анализ рейтинга брендов"
    )

    parser.add_argument("--files", nargs="+")  # "+" один и больше аргументов
    parser.add_argument("--report", choices=["average-rating"])
    args = parser.parse_args()
    list_csv = parser.parse_args().files

    if args.report == "average-rating":
        formatted_list_csv = check_csv_files(list_csv)
        brands_dict = make_brands_dict(formatted_list_csv)
        brands_list = sort_brands_list(brands_dict)
        make_table(brands_list)
    return args


def check_csv_files(list_csv):
    # def check_csv_files():  # FIXME не забыть удалить
    # list_csv = ["products1.csv", "products2.csv"] # FIXME не забыть удалить
    for idx, file in enumerate(list_csv):
        if not file.endswith(".csv"):
            list_csv[idx] = file + ".csv"

    return list_csv


def make_brands_dict(list_csv: list) -> list:
    """
    Функция для дальнейшего расчета рейтинга формирует словарь в виде
    [["brand": rating, counter], ["brand": rating, counter], ...]
    """
    brands_dict = {}

    for file in list_csv:
        with open(file, newline="") as csvfile:
            filereader = csv.reader(csvfile)
            next(filereader)  # Пропустить шапку документа (name brand price rating)

            for row in filereader:
                if len(row) < 4:  # Пропустить пустые или поврежденные строки
                    continue

                brand = row[1]
                rating = float(row[3])

                if brand in brands_dict:
                    brands_dict[brand][0] += rating
                    brands_dict[brand][1] += 1
                else:
                    # Записать новый ключ (бренд: рейтинг, счётчик)
                    brands_dict[brand] = [rating, 1]
    return brands_dict


def sort_brands_list(brands_dict):
    """
    Функция формирует отсортированный список брендов
    """
    brands_list = []

    for brand in brands_dict:
        brand_total_rating = brands_dict.get(brand)[0]
        brand_repeat_counters = brands_dict.get(brand)[1]
        brands_list.append(
            [brand, round(brand_total_rating / brand_repeat_counters, 2)]
        )

    sorted_brands_list = sorted(brands_list, key=lambda x: x[1], reverse=True)
    return sorted_brands_list


def make_table(brands_list: list):
    """
    Функция пересобирает переданный отсортированный список в новый
    с добавлением столбца нумерации
    Результат в виде таблицы выводит в консоль
    """
    numbered_list = [[i + 1] + row for i, row in enumerate(brands_list)]
    print(tabulate(numbered_list, headers=[" ", "brand", "rating"], tablefmt="grid"))


if __name__ == "__main__":
    main()
    # check_csv_files() # FIXME не забыть удалить
