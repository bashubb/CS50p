
while True:
    try:
        fraction = input("Fraction: ")
        numbers = fraction.split("/")
        x = int(numbers[0])
        y = int(numbers[1])
        precentage = round(x / y * 100)
        if x > y and y != 0:
            continue
        elif precentage >= 99:
            print("F")
            break
        elif precentage <= 1:
            print("E")
            break
        print(f"{precentage}%")
        break
    except ValueError:
        pass
    except ZeroDivisionError:
        pass

