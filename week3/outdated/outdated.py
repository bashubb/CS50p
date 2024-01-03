MONTHS = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]




def main():
    date_not_ok = True

    while date_not_ok:
        date = input("Date: ")
        splited_date = date.split("/")
        if len(splited_date) != 1:
            if splited_date[0].isalpha() or splited_date[1].isalpha() or splited_date[0].isalpha():
                    continue
            if int(splited_date[0]) > 12 or int(splited_date[1]) > 31 :
                continue
            else:
                print(f"{splited_date[2].strip()}-{int(splited_date[0].strip()):02}-{int(splited_date[1].strip()):02}")
                date_not_ok = False
        else:
            words_date = splited_date[0].split(" ")
            if len(words_date) != 3:
                continue
            if words_date[0].isnumeric():
                continue
            else:
                month = MONTHS.index(words_date[0]) + 1
                year = words_date[2]
                day = int(words_date[1].strip(","))
                if words_date[1][-1] != "," or day > 31:
                    continue
                print(f"{year}-{month:02}-{day:02}")
                date_not_ok = False









main()

