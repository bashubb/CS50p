def main():
    time = input("What time is it? ")

    if time.endswith("a.m.") or time.endswith("p.m."):
        hour_time, am_pm = sufix(time)
        time_decimal = convert(hour_time)
        if (time_decimal >= 7.00 and time_decimal <= 8.00) and am_pm == "a.m.":
            print("breakfast time")
        elif  (time_decimal >= 12.00 and time_decimal >= 12.99 and am_pm == "am") or (time_decimal == 1.00  and am_pm == "p.m."):
            print("lunch time")
        elif  (time_decimal >= 6.00 and time_decimal <= 7.00) and am_pm == "p.m.":
            print("dinner time")

    else:
        time_decimal = convert(time)

        if time_decimal >= 7.00 and time_decimal <= 8.00:
            print("breakfast time")
        elif time_decimal >= 12.00 and time_decimal <= 13.00:
            print("lunch time")
        elif time_decimal >= 18.00 and time_decimal <= 19.00:
            print("dinner time")


def convert(time):
    hours, minutes = time.split(":")
    if int(minutes) > 0:
        float_minutes = 10 / (60.00 / float(minutes)) * 0.1
        new_time = float(hours) + float_minutes
        return new_time
    elif int(minutes) == 0:
        return float(hours)

def sufix(time):
    hour_time, am_pm = time.split(" ")
    return hour_time, am_pm



if __name__ == "__main__":
    main()

