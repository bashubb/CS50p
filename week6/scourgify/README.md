CS50p Problem set6: Scourgify ✨
===========

Description
-----------

Scourgify is a Python program inspired by the magical spell from Harry Potter. This program aims to clean and reformat data in a CSV file. It specifically focuses on transforming a CSV file with combined first and last names into a new CSV file with separate columns for first name, last name, and house.

Problem Overview
----------------

The provided CSV file, `before.csv`, contains student data with combined first and last names. The goal is to create a new CSV file, `after.csv`, where each student's name is split into first and last names, along with their corresponding house.

How the Program Works
---------------------

The program accomplishes this task through the following steps:

1.  **Command-Line Arguments:**

    -   Expects two command-line arguments:
        -   The name of an existing CSV file to read as input.
        -   The name of a new CSV file to write as output.
2.  **File Validation:**

    -   Ensures the input file has a `.csv` extension.
    -   Exits with an error message if the input file does not exist.
3.  **CSV File Processing:**

    -   Reads the contents of the input CSV file.
4.  **Data Conversion:**

    -   Splits each combined name into a first name and last name.
    -   Creates a new dataset with separate columns for first name, last name, and house.
5.  **New CSV File Creation:**

    -   Writes the transformed data into a new CSV file.
6.  **Error Handling:**

    -   Exits with an error message if there are too few or too many command-line arguments.
    -   Exits with an error message if the input file cannot be read.
