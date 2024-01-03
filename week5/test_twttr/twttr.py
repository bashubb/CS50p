def main():
    input_word = input("Input: ")
    output_word =shorten(input_word)
    print(f"Output: {output_word}")

def shorten(word):
    volwes = ["a", "e", "i", "o", "u"]
    output_word = ""
    for letter in word:
        if letter.lower() not in volwes:
           output_word += letter
    return output_word


if __name__ == "__main__":
    main()

