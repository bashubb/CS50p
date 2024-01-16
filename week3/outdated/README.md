CS50p Problem set3: Date Format Converter 📅
========================

This Python program, named `outdated.py`, is a solution to CS50's Problem Set 3 - Outdated. The program prompts the user for a date in the middle-endian format (MM/DD/YYYY), or a formatted date with words (e.g., September 8, 1636), and converts it to the ISO 8601 format (YYYY-MM-DD). The program handles valid and invalid date inputs, providing an opportunity for the user to retry if the input is not in an acceptable format.

🚀 Implementation
-----------------

The program operates as follows:

1.  **User Input:** The program prompts the user for a date in either MM/DD/YYYY or a formatted date with words.

2.  **Validation:** It checks the input to ensure it's a valid date, treating cases like invalid month or day values.

3.  **Conversion:** The program converts the input to ISO 8601 format (YYYY-MM-DD) and prints the result.

4.  **Retry:** If the input is not valid, the program prompts the user again for a correct date.

🗓️ Example Output
------------------

-   **Example 1:**

    ```
    $ python outdated.py
    9/8/1636
    1636-09-08
    ```

-   **Example 2:**

    ```
    $ python outdated.py
    September 8,
    1636 1636-09-08
    ```

-   **Example 3:**

    ```
    $ python outdated.py
    23/6/1912
    Please enter a valid date.
    ```

-   **Example 4:**

    ```
    $ python outdated.py
    December 80, 1980
    Please enter a valid date.
    ```



Happy date formatting! 🗓️
