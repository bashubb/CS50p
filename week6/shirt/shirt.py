import sys
from PIL import Image, ImageOps

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif check_extension(sys.argv[1]) != check_extension(sys.argv[2]):
        sys.exit("Input and output have different extensions")
    else:
        try:
            shirt= Image.open("shirt.png")
            muppet =Image.open(sys.argv[1])
            merge(shirt, muppet, sys.argv[2])

        except FileNotFoundError:
            sys.exit("The file does not exist")
        else:
            shirt.close()
            muppet.close()



def check_extension(file_name):
    if file_name.lower().endswith(".jpg"):
        return "jpg"
    elif file_name.lower().endswith(".jpeg"):
        return "jpeg"
    elif file_name.lower().endswith(".png"):
        return "png"
    else:
        sys.exit("Invalid input")


def merge(shirt, muppet, new_file_name):
    size = shirt.size
    resized = ImageOps.fit(muppet, size, bleed=0.0, centering=(0.5, 0.5))
    resized.paste(shirt, mask=shirt)
    resized.save(new_file_name)


if __name__ == "__main__":
    main()
