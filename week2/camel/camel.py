def main():

    camel_case = input("camelCase: ")

    snake_case = ""
    for letter in camel_case:
        if letter.isupper():
            snake_case += "_"
            snake_case += letter.lower()
        else:
            snake_case += letter

    print(f"snake_case: {snake_case}")



main()

