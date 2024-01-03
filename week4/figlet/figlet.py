import pyfiglet
import sys


if len(sys.argv) != 1 and len(sys.argv) != 3:
    sys.exit("Invalid usage")



if len(sys.argv) == 1:
    text_to_format = input("Input: ")
    result = pyfiglet.figlet_format(text_to_format)
    print("Output:")
    print(result)

if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
    if sys.argv[2] in pyfiglet.FigletFont.getFonts():
        text_to_format = input("Input: ")
        result = pyfiglet.figlet_format(text_to_format, font = sys.argv[2])
        print("Output:")
        print(result)
    else:
        sys.exit("Invalid usage")
else:
    sys.exit("Invalid usage")




