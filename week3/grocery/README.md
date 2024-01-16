CS50p Problem set3: Grocery List 🛒
===============

This Python program, located in `grocery.py`, provides a solution to CS50's Problem Set 3 - Grocery List. The program prompts the user for grocery items, one per line, until the user signals the end of input with control-d. It then outputs the user's grocery list in all uppercase, sorted alphabetically by item, and prefixes each line with the number of times the user inputted that item. The user's input is treated case-insensitively.

🚀 Implementation
-----------------

The program operates as follows:

1.  **User Input:** The program prompts the user for grocery items, treating each input case-insensitively.

2.  **List Generation:** It generates a list of user-inputted grocery items.

3.  **Sorting:** The program sorts the list alphabetically.

4.  **Counting Occurrences:** It creates a dictionary to count the occurrences of each grocery item.

5.  **Output:** The program prints the grocery list in uppercase, sorted alphabetically, with the count of occurrences for each item.

6.  **End of Input:** The program continues prompting the user until they signal the end of input with control-d.

Example Output
------------------

-   **Example 1:**

    ```
    $ python grocery.py
    mango strawberry
    ^D
    1 MANGO
    1 STRAWBERRY
    ```

-   **Example 2:**

    ```
    $ python grocery.py milk milk
    ^D
    2 MILK
    ```

-   **Example 3:**

    ```
    $ python grocery.py
    tortilla sweet potato
    ^D
    1 SWEET POTATO
    1 TORTILLA
    ```

Happy grocery listing! 🛒📜
