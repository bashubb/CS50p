CS50p Problem set5: Back to the Bank 💰
===================

Description
-----------

Back to the Bank is a Python program, implemented in `bank.py`, as a solution to CS50p Problem Set 5. This program reintroduces Home Federal Savings Bank from Problem Set 1, with a restructuring of the code. The main functionality is housed within the `value` function, which expects a string as input and returns an integer. It returns 0 if the string starts with "hello," 20 if it starts with an "h" (but not "hello"), and 100 otherwise, treating the string case-insensitively. The `main` function is responsible for calling `print`.

Unit Testing with Pytest 🧪
---------------------------

Unit testing is a software testing technique where individual units or components of a program are tested in isolation to ensure they work correctly. Pytest is a popular testing framework for Python that simplifies the process of writing and executing tests.

Pytest Framework
----------------

1.  **Test Functions**: Test functions are created with names starting with `test_` to indicate that they are test cases.

    ```python 
    def test_value_hello():
      assert bank.value("hello") == 0

    deftest_value_h():
      assert bank.value("hello") == 20

    deftest_value_default():
      assert bank.value("What's up") == 100
    
    ```

2.  **Assertions**: Assertions are used to check if the actual result matches the expected result. If the assertion fails, the test case fails.

3.  **Running Tests**: Tests can be executed using the `pytest` command in the terminal.

    ```
    pytest test_bank.py
    ```

    -   Pytest discovers and runs all test functions in the specified file, providing detailed output about test results.
4.  **Test Outcomes**: Pytest distinguishes between passed, failed, and skipped tests, providing a clear overview of the test suite's health.

Explore Back to the Bank, ensure the correctness of the `value` function, and enhance the robustness of your code through thorough testing! 💰🧪
