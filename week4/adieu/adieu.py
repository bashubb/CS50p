import sys

def main():

    names = []
    while True:
        try:
            name = input()
            if name != "":
                names.append(name)
            else:
                break
        except EOFError:
            break

    if len(names) > 1:
        if len(names) == 2:
            print(f"Adieu, adieu, to {names[0]} and {names[1]}")
        else:
            for i in range(0, len(names)):
                        if i < len(names) - 1:
                            names[i] += ","
                        else:
                            names[i] = "and " + names[i]

            print(f"Adieu, adieu, to {" ".join(names)}")
    else:
        print(f"Adieu, adieu, to {"".join(names)}")





main()


