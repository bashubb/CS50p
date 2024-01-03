from datetime import date
import inflect
import sys
import operator


p = inflect.engine()

def main():
    try:
        string_date_of_birth = input("Date of Birth: ")
        date_of_birth = date.fromisoformat(string_date_of_birth)
    except ValueError:
        sys.exit("Invalid syntax")
    else:
        print(convert_to_words(date_of_birth))


def convert_to_words(date_of_birth):
    today = date.today()
    time = operator.sub(today, date_of_birth)
    minutes = int((time.total_seconds() / 60))
    return f"{p.number_to_words(minutes, andword="").capitalize()} minutes"



if __name__ == "__main__":
    main()
