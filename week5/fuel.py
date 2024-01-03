

def main():

    fraction = input("Fraction: ")
    percentage = convert(fraction)
    print(guage(percentage))


def convert(fraction):
    numbers = fraction.split("/")
    x = int(numbers[0])
    y = int(numbers[1])
    if x > y and y != 0:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    percentage = round(x / y * 100)
    return percentage





def gauge(percentage):

    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"

    return f"{percentage}%"



if __name__ == "__main__":
    main()





