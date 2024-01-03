def main():
    volwes = ["a", "e", "i", "o", "u"]

    input_word = input("Input: ")
    output_word = ""
    for letter in input_word:
        if letter.lower() not in volwes:
           output_word += letter

    print(f"Output: {output_word}")





main()
