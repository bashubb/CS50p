import re


def main():
    print(count(input("Text: ")))


def count(s):

    if match := re.findall(r"(^|\W)um($|\W)", s, re.IGNORECASE):
        return(len(match))


if __name__ == "__main__":
    main()
