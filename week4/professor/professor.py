import random


def main():
    level = get_level()
    score = 0
    problems = []
    for i in range(10):
        problems.append([generate_integer(level), generate_integer(level)])

    for problem in problems:
        correct_answer = problem[0] + problem[1]
        print(f"{problem[0]} + {problem[1]} = ")
        answer = int(input())
        tries = 3
        while answer != correct_answer and tries > 1:
            print("EEE")
            tries -= 1
            print(f"{problem[0]} + {problem[1]} =")
            answer = int(input())

        if answer != correct_answer:
            print(f"{problem[0]} + {problem[1]} = {correct_answer}")
            continue
        elif answer == correct_answer:
            score += 1

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = input("Level: ")
            if level.isnumeric():
                if int(level) not in range(1, 4):
                    raise ValueError
                break
        except ValueError:
            pass

    return int(level)


def generate_integer(level):
    if level not in range(1, 4):
        raise ValueError
    else:
        if level == 1:
            return random.randint(0, 9)
        elif level == 2:
            return random.randint(10, 99)
        elif level == 3:
            return random.randint(100, 999)


if __name__ == "__main__":
    main()

