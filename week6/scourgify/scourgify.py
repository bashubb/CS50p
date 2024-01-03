import sys
import csv

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        lines_before = []
        if is_csv_file(sys.argv[1]):
            try:
                file = open(sys.argv[1])
                reader = csv.DictReader(file)

            except FileNotFoundError:
                qsys.exit(f"Could not read {sys.argv[1]}")

            else:
                for row in reader:
                    lines_before.append(row)
                file.close()
                lines_after = convert(lines_before)
                write_new_csv(lines_after, sys.argv[2])

        else:
            sys.exit(f"Could not read {sys.argv[1]}")


def is_csv_file(file_name):
    return file_name.endswith(".csv")


def convert(lines):
    lines_after = []
    for student in lines:
        last, first = student["name"].strip('"').split(",")
        new_student = {"first": first.strip() , "last": last.strip()cd, "house": student["house"]}
        lines_after.append(new_student)
    return lines_after


def write_new_csv(lines_after, new_file_name):
    with open(new_file_name, "w") as new_file:
        fieldnames = ["first", "last", "house"]
        writer = csv.DictWriter(new_file, fieldnames=fieldnames)
        writer.writeheader()
        for student in lines_after:
            writer.writerow({"first": student["first"], "last": student["last"], "house": student["house"]})


if __name__ == "__main__":
    main()
