CS50p Problem set 6: Lines of Code Counter 📊
========================

Description
-----------

Lines of Code Counter is a Python program, implemented in `lines.py`, as a solution to CS50p Problem Set 6. This program counts the number of lines of code (LOC) in a Python file, excluding comments and blank lines. The complexity of a program is often measured by its LOC, although it's important to note that this metric should be taken with a grain of salt, as the number of lines doesn't always correlate with complexity.

Source Code Overview
--------------------

The source code is structured with a main function and several helper functions. Here's a brief overview of the functions:

-   `main()`: Handles command-line arguments, file validation, and counts the lines of code in the specified Python file.
-   `is_python_file(file_name)`: Checks if the specified file has a `.py` extension, indicating it is a Python file.
-   `check_if_line_is_comment(line)`: Checks if a line is a comment by examining if it starts with `#`.
-   `check_if_line_is_whitespace(line)`: Checks if a line is blank (only contains whitespace).

How the Program Works
---------------------

1.  **Command-Line Arguments:**

    -   The program checks the number of command-line arguments. If there are too few or too many, it exits with an error message.
    -   It ensures that there is exactly one command-line argument, which is assumed to be the Python file to be analyzed.
2.  **File Validation:**

    -   It checks if the specified file has a `.py` extension, using the `is_python_file` function.
    -   If the file is not a Python file, it exits with an error message.
3.  **Line Counting:**

    -   The program reads the specified file line by line.
    -   For each line, it checks if it's a comment (`check_if_line_is_comment`) or blank (`check_if_line_is_whitespace`). If neither, it increments the line count.
4.  **Output:**

    -   The total line count (excluding comments and blank lines) is printed to the console.
5.  **Error Handling:**

    -   If the specified file does not exist, the program exits with an appropriate error message.
