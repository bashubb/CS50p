CS50p Problem set4: Figlet
======

Description
-----------

Figlet is a Python program that transforms ordinary text into stylish ASCII art, resembling large letters. The program, found in `figlet.py`, is part of the CS50p Problem Set 4 solution. It leverages the `pyfiglet` module, a Python adaptation of the 1990s FIGlet program. Dive into the world of creative text visualization with various fonts available at [figlet.org/examples.html](http://www.figlet.org/examples.html).🌈

How It Works
------------

1.  The program checks for the correct number of command-line arguments.
2.  If the user specifies a font, it ensures the font is valid; otherwise, it exits with a friendly error message.🚫❌
3.  The user is prompted to input a text string.
4.  The program outputs the entered text in the chosen font, creating a visually appealing ASCII representation.

Example
-------

-   **Random Font:**

    ```
    python figlet.py
    ```

-   **Specific Font:**

    ```

    python figlet.py -f slant
    ```

    Enter `CS50`, and witness the magic unfold:

    ```
       ___________ __________ 
      / ____/ ___// ____/ __ \
     / /    \__ \/___ \/ / / /
    / /___ ___/ /___/ / /_/ / 
    \____//____/_____/\____/
    
    ```

    

Explore this tool, unleash your creativity, and enjoy the world of text art! 🎨
