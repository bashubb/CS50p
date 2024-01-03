import random


def main():
    level = level_input()
    number_to_guess = random.randint(0, level)
    guess = guess_value(level)

    while guess != number_to_guess:
        if guess < number_to_guess:
            print("Too small!")
            guess = guess_value(level)
        else:
            print("Too large!")
            guess = guess_value(level)
    print("Just right!")


def level_input():
    level = input("Level: ")
    while level.isnumeric() == False or int(level) < 0:
        level = input("Level: ")
    return int(level)


def guess_value(guess_in_range):
    while True:
        guess = input("Guess: ")
        if guess.isnumeric() and int(guess) in range(1,guess_in_range+1) :
            break
    return int(guess)


if __name__ == "__main__":
    main()

