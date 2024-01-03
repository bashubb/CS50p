import sys

def main():
    if len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    else:
        if is_python_file(sys.argv[1]):
            lines = 0
            try:
                with open(sys.argv[1]) as file:
                    for line in file:
                        if check_if_line_is_comment(line):
                            continue
                        elif check_if_line_is_whitespace(line):
                            continue
                        else:
                            lines += 1

                print(lines)

            except FileNotFoundError:
                sys.exit("File does not exist")

        else:
            sys.exit("Not a Python file")




def is_python_file(file_name):
    return file_name.endswith(".py")

def check_if_line_is_comment(line):
    return line.strip().startswith("#")

def check_if_line_is_whitespace(line):
    return len(line.strip()) == 0


if __name__ == "__main__":
    main()
