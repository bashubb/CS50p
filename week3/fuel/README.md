CS50p Problem set3:Fuel Gauge 🚗⛽
==============

This Python program, located in `fuel.py`, provides a solution to CS50's Problem Set 3. The program prompts the user for a fuel fraction in the format X/Y, where both X and Y are integers, and then outputs the fuel level as a percentage rounded to the nearest integer. Additionally, it handles various error cases, such as invalid input, division by zero, and other exceptions.

🚀 Implementation
-----------------

The program operates as follows:

1.  **User Input:** The program prompts the user for a fuel fraction in the format X/Y.

2.  **Percentage Calculation:** It calculates the fuel level as a percentage and rounds it to the nearest integer.

3.  **Output:**

    -   If 1% or less remains, it outputs "E" to indicate that the tank is essentially empty.
    -   If 99% or more remains, it outputs "F" to indicate that the tank is essentially full.
    -   Otherwise, it outputs the calculated percentage.
4.  **Error Handling:** The program handles various exceptions, including `ValueError` and `ZeroDivisionError`. If invalid input or division by zero occurs, the user is prompted to enter the fraction again.

🌟 Example Output
-----------------

-   **Example 1:**

    ```
    $ python fuel.py
    Fraction: 3/4
    75%
    ```

-   **Example 2:**

    ```
    $ python fuel.py
    Fraction: 1/4
    25%
    ```

-   **Example 3:**

    ```
    $ python fuel.py
    Fraction: 4/4
    F
    ```

-   **Example 4:**

    ```
    $ python fuel.py
    Fraction: 0/4
    E
    ```

-   **Example 5:**

     ```
    $ python fuel.py
    Fraction: 4/0
    ```
    (Handles a `ZeroDivisionError` and prompts the user again)

-   **Example 6:**

     ```
    $ python fuel.py
    Fraction: three/four
    ```

    (Handles a `ValueError` and prompts the user again)

-   **Example 7:**

    ```
    $ python fuel.py    
    Fraction: 1.5/3
    ```

    (Handles a `ValueError` and prompts the user again)

-   **Example 8:**

    ```
    $ python fuel.py
    Fraction: 5/4
    ```

    (Prompts the user again due to invalid input)

This program provides a convenient way to determine the fuel level and ensures robustness against invalid input. Safe travels! 🚗⛽
