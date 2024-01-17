CS50p Problem set5: Testing My Twttr
=====================

Description
-----------

Testing My Twttr is a Python program, implemented in `twttr.py`, as a solution to CS50p Problem Set 5. This program introduces a restructuring of the code from Problem Set 2's "Setting up my twttr." The main functionality is housed within the `shorten` function, which expects a string as input and returns the same string with all vowels (A, E, I, O, and U) omitted, regardless of case.

Unit Testing with Pytest 🧪
---------------------------

Unit testing is a software testing technique where individual units or components of a program are tested in isolation to ensure they work correctly. Pytest is a popular testing framework for Python that simplifies the process of writing and executing tests.

Pytest Framework
----------------

1.  **Test Functions**: Test functions are created with names starting with `test_` to indicate that they are test cases.

    ```python
    def test_shorten():
    
      assert twttr.shorten("Hello") == "Hll"
      assert twttr.shorten("Python") == "Pythn"
      assert twttr.shorten("CS50") == "CS50"
      assert twttr.shorten("") == ""
    ```

2.  **Assertions**: Assertions are used to check if the actual result matches the expected result. If the assertion fails, the test case fails.

3.  **Running Tests**: Tests can be executed using the `pytest` command in the terminal.

    ```
    pytest test_twttr.py
    ```

    -   Pytest discovers and runs all test functions in the specified file, providing detailed output about test results.
4.  **Test Outcomes**: Pytest distinguishes between passed, failed, and skipped tests, providing a clear overview of the test suite's health.

Explore Testing My Twttr, ensure the correctness of the `shorten` function, and enhance the robustness of your code through thorough testing! 🐦
