import sys
from tabulate import tabulate
import csv

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if is_csv_file(sys.argv[1]):
            try:
                lines = []
                with open(sys.argv[1]) as file:
                    reader = csv.reader(file)
                    for row in reader:
                        lines.append(row)
                print(make_table(lines))


            except FileNotFoundError:
                sys.exit("File does not exist")

        else:
            sys.exit("Not a CSV file")




def is_csv_file(file_name):
    return file_name.endswith(".csv")

def make_table(lines):
    return tabulate(lines, headers="firstrow", tablefmt="grid")


if __name__ == "__main__":
    main()
