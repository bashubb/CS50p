import emoji
import requests

input = input("Input: ")
print(f"Output: {emoji.emojize(input, language = 'alias')}")

