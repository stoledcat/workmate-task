import argparse
import os
import sys
from parser import Parser


def main(argv=None):
    parser = argparse.ArgumentParser(prog="BrandRatingAnalysis", description="Brand rating processing")
    parser.add_argument("--files", nargs="+")
    parser.add_argument("--report", choices=["average-rating"])
    parser.add_argument("--dir", type=str)
    args = parser.parse_args(argv)

    list_csv = []
    if args.dir:
        if os.path.isdir(args.dir):
            for filename in os.listdir(args.dir):
                if filename.endswith(".csv"):
                    list_csv.append(os.path.join(args.dir, filename))
        else:
            sys.exit("Directory is not valid")
    else:
        list_csv = args.files

    if args.report == "average-rating":
        p = Parser()
        formatted_list_csv = p.check_csv_files(list_csv)
        brands_dict = p.make_brands_dict(formatted_list_csv)
        brands_list = p.sort_brands_list(brands_dict)
        p.make_table(brands_list)


if __name__ == "__main__":
    main()
