import csv

from tabulate import tabulate


class Parser:
    def __init__(self):
        pass

    def check_csv_files(self, list_csv):
        list_csv_checked = []
        for idx, file in enumerate(list_csv):
            if not file.endswith('.csv'):
                list_csv_checked.append(f"{idx} {file} .csv")
        return list_csv_checked or list_csv

    def make_brands_dict(self, list_csv):
        brands_dict = {}
        for file in list_csv:
            with open(file, newline='') as csv_file:
                filereader = csv.reader(csv_file)
                next(filereader)
                for row in filereader:
                    if len(row) < 4:
                        continue
                    brand = row[1]
                    rating = float(row[3])
                    if brand in brands_dict:
                        brands_dict[brand][0] += rating
                        brands_dict[brand][1] += 1
                    else:
                        brands_dict[brand] = [rating, 1]
        return brands_dict

    def sort_brands_list(self, brands_dict):
        brands_list = []
        for brand in brands_dict:
            total_rating = brands_dict[brand][0]
            count = brands_dict[brand][1]
            brands_list.append((brand, round(total_rating / count, 2)))
        sorted_brands_list = sorted(brands_list, key=lambda x: x[1], reverse=True)
        return sorted_brands_list

    def make_table(self, brands_list):
        numbered_list = [(i + 1, row[0], row[1]) for i, row in enumerate(brands_list)]
        print(tabulate(numbered_list, headers=['', 'Brand', 'Rating'], tablefmt='grid'))
