

def main():

    message = input()
    print(convert(message))


def convert(message):
    new_message = message.replace(":)", "🙂").replace(":(", "🙁")

    return new_message

main()

