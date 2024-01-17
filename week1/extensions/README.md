CS50p Problem set 1: File Extensions Checker
=======================

This Python program, located in `extensions.py`, represents my solution to CS50's Problem Set 1. The program interacts with the user by prompting them for a file name and then outputs the corresponding media type based on the file's extension. Recognized extensions include .gif, .jpg, .jpeg, .png, .pdf, .txt, or .zip. If the file has a different or no recognized extension, the program defaults to "application/octet-stream."

Description
-----------

While some operating systems may hide file extensions, they play a crucial role in determining how files are processed. In this program, I've simulated web server behavior by associating file extensions with media types. The user inputs a file name, and the program, through the `main` function in `extensions.py`, identifies the file's extension (case-insensitive) to output the appropriate media type.

🚀 Implementation
-----------------

The heart of the program lies in the `main` function, efficiently determining the media type based on the file's extension and printing the result.

🧐 Supported File Extensions
----------------------------

-   .gif
-   .jpg
-   .jpeg
-   .png
-   .pdf
-   .txt
-   .zip
