def main():

    greeting = input("Greeting: ")

    if  "hello" in greeting.strip().lower() :
        print("$0")
    elif greeting.strip().lower()[0] == "h" :
        print("$20")
    else:
        print("$100")


main()

