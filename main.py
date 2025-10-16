import argparse
import csv
# import tabulate


def main():
    parser = argparse.ArgumentParser(
        prog="BrandRatingAnalysis", description="Анализ рейтинга брендов"
    )

    parser.add_argument("--files", nargs="+")  # "+" 1 и больше аргументов
    parser.add_argument("--report", choices=["average-rating"])
    args = parser.parse_args()

    if args.report == "average-rating":
        brands_dict = average_rating(parser)
        print(brands_dict)


def average_rating(parser):
    list_csv = parser.parse_args().files
    return parse_csv_files(list_csv)


def parse_csv_files(list_csv: list) -> list:
    """
    Функция рассчитывает рейтинг из полученных данных и
    и формирует список в виде
    [["brand", rating], ["brand", rating], ...]
    """

    brands_dict = {}
    brands_list = []

    for file in list_csv:
        with open(file, newline="") as csvfile:
            filereader = csv.reader(csvfile)
            next(filereader)  # Пропустить шапку документа (name brand price rating)

            for row in filereader:
                brand = row[1]
                rating = float(row[3])

                if brand in brands_dict:
                    brands_dict[brand][0] += rating
                    brands_dict[brand][1] += 1
                else:
                    # Записать новый ключ (бренд: рейтинг, счётчик)
                    brands_dict[brand] = [rating, 1]

    for brand in brands_dict:
        brand_total_rating = brands_dict.get(brand)[0]
        brand_repeat_counters = brands_dict.get(brand)[1]
        brands_dict[brand] = round(brand_total_rating / brand_repeat_counters, 2)
        brands_list.append(
            [brand, round(brand_total_rating / brand_repeat_counters, 2)]
        )
    sorted_brands_list = sorted(brands_list, key=lambda x: x[1], reverse=True)
    return sorted_brands_list


if __name__ == "__main__":
    main()
