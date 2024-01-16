CS50p Problem set2: 🐍 Camel Case to Snake Case Converter
=====================================

This Python program, residing in `camel.py`, efficiently transforms variable names from camel case to snake case. It aligns with Python conventions and provides an easy way to convert camel case variable names.

🚀 How It Works
---------------

The program operates in a straightforward manner:

1.  **User Input:** The program prompts the user to input a variable name in camel case.

2.  **Conversion Process:** It iterates through each letter of the camel case input:

    -   If a letter is uppercase, it appends an underscore (`_`) followed by the lowercase version of the letter to the snake case variable.
    -   If a letter is lowercase, it appends the letter as is to the snake case variable.
3.  **Output:** The program then prints the variable name in snake case.

🌟 Example
----------

Suppose the user inputs "camelCase":

-   The program encounters the uppercase "C" and appends "_c" to the snake case variable.
-   For the lowercase letters "a," "m," "e," and "l," the program appends them directly.
-   The final output is "camel_case."

This program streamlines the conversion of camel case variable names to snake case, adhering to Python naming conventions. 
