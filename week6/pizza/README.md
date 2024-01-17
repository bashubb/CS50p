CS50p Problem set6: Pizza Py 🍕
===========

Description
-----------

Pizza Py is a Python program that reads a CSV file containing Pinocchio's Pizza & Subs menu and outputs a formatted table as ASCII art. The table is created using the `tabulate` library with a grid format for better readability.

Source Code Overview
--------------------

The program consists of a main function and helper functions:

-   `main()`: Manages command-line arguments, validates files, reads CSV contents, and prints the table.
-   `is_csv_file(file_name)`: Checks if the file has a `.csv` extension.
-   `make_table(lines)`: Creates a table using the `tabulate` library.

How the Program Works
---------------------

1.  **Command-Line Arguments:**

    -   Checks if there is exactly one command-line argument, assumed to be the CSV file to process.
2.  **File Validation:**

    -   Ensures the file has a `.csv` extension.
    -   Exits with an error message if the file is not a CSV.
3.  **CSV File Processing:**

    -   Reads the contents of the CSV file and stores each row in a list.
4.  **Table Generation:**

    -   Uses `tabulate` to format the data into a grid table.
    -   Headers are taken from the first row.
5.  **Output:**

    -   Prints the formatted table to the console.
6.  **Error Handling:**

    -   Exits with an error message if the file does not exist.

Running the Program
-------------------

```
python pizza.py your_menu.csv
```

Replace `your_menu.csv` with the CSV file you want to process.

How to Test
-----------

1.  **Test for Too Few Arguments:**

    ```
    python pizza.py
    ```

    -   Expected: Program exits with an error message.
2.  **Test for Invalid File:**

    ```
    python pizza.py invalid_file.csv
    ```

    -   Expected: Program exits with an error message.
3.  **Test for Not a CSV File:**

    ```
    python pizza.py sicilian.txt
    ```

    -   Expected: Program exits with an error message.
4.  **Test with Valid Input File:**

    ```
    python pizza.py regular.csv
    ```

    -   Expected: Program prints a formatted table similar to the provided example.

Sample Output
-------------

```
+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
| 2 toppings      | $15.95  | $22.95  |
+-----------------+---------+---------+
| 3 toppings      | $16.95  | $24.95  |
+-----------------+---------+---------+
| Special         | $18.50  | $26.95  |
+-----------------+---------+---------+
```
