C50p Problem set1: Math Interpreter
================

This Python program, located in `interpreter.py`, provides a solution to CS50's Problem Set 1. It serves as a straightforward math interpreter, allowing users to input arithmetic expressions. The program then calculates and outputs the result as a floating-point value formatted to one decimal place.

Description
-----------

Python already supports mathematical operations, but this program enables users to perform math operations without knowing Python syntax. The user is prompted to input an arithmetic expression in the format "x y z," where:

-   x is an integer
-   y is an operator (+, -, *, or /)
-   z is an integer

For example, if the user inputs "1 + 1," the program will output "2.0." This program acts as a basic interpreter for mathematical expressions.

🚀 Implementation
-----------------

The core logic of the program resides in the `main` function within the `interpreter.py` file. It efficiently processes the user's input, performs the mathematical operation, and outputs the result as a floating-point value.

🧐 Supported Operations
-----------------------

-   Addition (+)
-   Subtraction (-)
-   Multiplication (*)
-   Division (/) - Note: Division by zero is not allowed.
