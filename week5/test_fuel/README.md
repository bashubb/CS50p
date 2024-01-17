CS50p Problem set5: Refueling 🚗⛽
=============

Description
-----------

Refueling is a Python program, implemented in `fuel.py`, as a solution to CS50p Problem Set 5. This program is a reimagination of Fuel Gauge from Problem Set 3, with a code restructuring. It introduces two main functions:

1.  **`convert(fraction)`**: Expects a string in X/Y format as input, where X and Y are integers. Returns the fraction as a percentage rounded to the nearest integer between 0 and 100, inclusive. Raises `ValueError` if X and/or Y is not an integer or if X is greater than Y. Raises `ZeroDivisionError` if Y is 0.

2.  **`gauge(percentage)`**: Expects an integer and returns a string:

    -   "E" if the integer is less than or equal to 1,
    -   "F" if the integer is greater than or equal to 99, and
    -   "Z%" otherwise, where Z is the same integer.

Unit Testing with Pytest 🧪
---------------------------

Unit testing is a crucial part of software development, ensuring the correctness and reliability of the code. Pytest, a widely-used testing framework for Python, simplifies the process of writing and running tests.

Pytest Framework
----------------

1.  **Test Functions**: Two or more test functions are implemented in `test_fuel.py`, each starting with `test_` to indicate they are test cases.

    ```python
    def test_valid_conversion():
      assert fuel.convert("5/10") == 50

    def test_invalid_fraction():
      with pytest.raises(ValueError): fuel.convert("abc/10")

    def test_zero_denominator():
      with pytest.raises(ZeroDivisionError): fuel.convert("5/0")

    def test_gauge_full():
      assert fuel.gauge(100) == "F"
    ```

2.  **Assertions and Exceptions**: Pytest uses assertions to check if the actual result matches the expected result. Additionally, it uses `pytest.raises` to check if the function raises an expected exception.

3.  **Running Tests**: The `pytest` command is used to execute tests in the terminal.

    ```
    pytest test_fuel.py
    ```

    -   Pytest discovers and runs all test functions in the specified file, providing detailed output about test results.
4.  **Test Outcomes**: The test outcomes help in identifying passed, failed, or skipped tests, ensuring the robustness of the program.

Explore Refueling, verify the correctness of `convert` and `gauge` functions, and fortify your code through comprehensive testing! 🚗⛽🧪
