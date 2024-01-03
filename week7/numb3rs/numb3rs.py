import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if match := re.search(r"^((\d{1,2}|(1\d{2})|2[01234]\d|25[0-5])\.?){4}$", ip):
        return True
    return False


if __name__ == "__main__":
    main()
