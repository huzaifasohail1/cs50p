import os
import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) < 2:
        sys.exit(1)
    elif len(sys.argv) > 2:
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("No file with that name")
        sys.exit(1)
    elif not sys.argv[1].endswith(".csv"):
        print("Not supported file")
        sys.exit(1)
    else:
        table_it(sys.argv[1])


def table_it(user_input):
    with open(user_input, "r") as csv_file:
        table = csv.DictReader(csv_file, delimiter=",")
        print(tabulate(table, headers="keys", tablefmt="grid"))


if __name__ == "__main__":
    main()