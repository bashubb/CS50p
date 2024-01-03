def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    print(check(answer.strip()))


def check(answer):
    if answer == "42" or answer.lower() == "forty two" or answer.lower() == "forty-two" :
        return "Yes"
    else:
        return "No"


main()

