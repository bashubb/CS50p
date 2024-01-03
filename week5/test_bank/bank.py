def main():
    greeting = input("Greeting: ")
    print(value(greeting))


def value(greeting):
    if  "hello" in greeting.strip().lower() :
        return 0
    elif greeting.strip().lower()[0] == "h" :
        return 20
    else:
        return 100



if __name__ == "__main__":
    main()


