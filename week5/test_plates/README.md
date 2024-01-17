
CS50p Problem set 5: Re-requesting a Vanity Plate 🚗
===============================

Description
-----------

Re-requesting a Vanity Plate is a Python program, implemented in `plates.py`, as a solution to CS50p Problem Set 5. This program is a reimagination of Vanity Plates from Problem Set 2, with a code restructuring. The core functionality is housed within the `is_valid` function, which expects a string as input and returns True if the string meets all requirements and False otherwise. The `main` function is only called if the value of `__name__` is `"__main__"`.

Unit Testing with Pytest 🧪
---------------------------

Unit testing is a crucial part of software development that involves testing individual units or components to ensure their correctness. Pytest, a widely-used testing framework for Python, simplifies the process of writing and running tests.

Pytest Framework
----------------

1.  **Test Functions**: Four or more test functions are implemented in `test_plates.py`, each starting with `test_` to indicate that they are test cases.

    ```python 
    def test_valid_plate():
      assert plates.is_valid("CS50")

    def test_invalid_length():
      assertnot plates.is_valid("ABCD12345")

    def test_invalid_characters():
      assert notplates.is_valid("CS!50")

    def test_valid_special_characters():
      assertplates.is_valid("CS-50")
    ```

2.  **Assertions**: Pytest uses assertions to check if the actual result matches the expected result, helping identify issues in the code.

3.  **Running Tests**: The `pytest` command is used to execute tests in the terminal.

    
    ```
     pytest test_plates.py
    ```

    -   Pytest discovers and runs all test functions in the specified file, providing detailed output about test results.
4.  **Test Outcomes**: The test outcomes help in identifying passed, failed, or skipped tests, ensuring the reliability of the program.

Explore Re-requesting a Vanity Plate, verify the correctness of the `is_valid` function, and fortify your code through comprehensive testing! 🚗🧪
