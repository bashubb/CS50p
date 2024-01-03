def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 1 and len(s) < 7:

        if s[0].isalpha() and s[1].isalpha():

            spaces = True
            punctuation_marks = True
            numbers = True
            for i in range(0, len(s)):
                if s[i].isalpha() == False and s[i].isnumeric() == False:
                    spaces = False
                    punctuation_marks = False
                if (i == len(s) - 1 and s[i].isnumeric() == False) and s[len(s)-2].isnumeric():
                    numbers = False
                if i != 0 and (s[i].isnumeric() and s[i] == "0") and (s[i-1].isnumeric() == False):
                    numbers = False
            if s[-1].isnumeric() and s[-2].isnumeric() == False:
                numbers = False

            if spaces and punctuation_marks and numbers:
                return True
    else:
        return False


main()

