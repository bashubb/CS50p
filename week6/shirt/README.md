CS50p Problem set6: P-Shirt 🎽
===============

Description
-----------

CS50 P-Shirt is a Python program designed to virtually try on a CS50-themed shirt on a photo. The program overlays a transparent CS50 shirt image on the input photo after resizing and cropping to ensure a perfect fit.

Problem Overview
----------------

Upon completing CS50, students traditionally receive a CS50 t-shirt. This program allows users to visualize themselves wearing a CS50 shirt virtually. It reads an input photo, resizes and crops it to match the CS50 shirt's dimensions, overlays the shirt image, and saves the result as the output.

How the Program Works
---------------------

The program operates with two command-line arguments:

1.  `sys.argv[1]`: The name or path of the input JPEG or PNG photo.
2.  `sys.argv[2]`: The name or path of the output JPEG or PNG file.

The process involves:

1.  Opening the input and shirt images using `Image.open` from the Pillow library.
2.  Checking if the input and output filenames have valid extensions (`jpg`, `jpeg`, or `png`).
3.  Resizing and cropping the input photo to match the dimensions of the CS50 shirt using `ImageOps.fit`.
4.  Overlaying the CS50 shirt on the resized input using `Image.paste`.
5.  Saving the final result as the output file using `Image.save`.

The program exits via `sys.exit` in case:

-   The user does not provide exactly two command-line arguments.
-   The input and output filenames do not end in `.jpg`, `.jpeg`, or `.png` (case-insensitive).
-   The input's extension differs from the output's extension.
-   The specified input file does not exist.

Sample Output
-------------

The resulting output will be a new image file with the CS50 shirt overlaid on the input photo.

*** before: 

<img src="https://github.com/bashubb/CS50p/blob/main/week6/shirt/before1.jpg" alt="before" width="40%" height="40%"/>

*** after: 

<img src="https://github.com/bashubb/CS50p/blob/main/week6/shirt/after1.jpg" alt="after" width="40%" height="40%"/>


Feel free to share a photo of yourself wearing your virtual CS50 shirt in CS50's communities!
