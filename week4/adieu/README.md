CS50p Problem set4: Adieu
=====

Description
-----------

Adieu is a Python program designed as a solution to CS50p Problem Set 4, inspired by the song "So Long, Farewell" from The Sound of Music. The program, residing in `adieu.py`, prompts the user for names until the user inputs control-d, then gracefully bids adieu to those names. The farewell is crafted in a charming manner, separating two names with one "and," three names with two commas and one "and," and for more than three names, using commas and one "and."

How It Works
------------

1.  The program uses a loop to continuously prompt the user for names until control-d is entered.
2.  The entered names are stored in a list.
3.  Based on the number of names, the program constructs a farewell message:
    -   For one name, it directly bids adieu.
    -   For two names, it uses one "and" between them.
    -   For more than two names, it uses commas between names and one "and" before the last name.

Example
-------

-   **Example 1:**

    ```
    python adieu.py
    ```

    Enter `Liesl` and press Enter, followed by control-d. The program outputs:

    ```
    Adieu, adieu, to Liesl
    ```

-   **Example 2:**

    ```
    python adieu.py
    ```

    Enter `Liesl` and press Enter, then type `Friedrich` and press Enter, followed by control-d. The program outputs:

    ```
    Adieu, adieu, to Liesl and Friedrich
    ```

-   **Example 3:**

    ```
    python adieu.py
    ```

    Enter `Liesl` and press Enter, then type `Friedrich` and press Enter. Now type `Louisa` and press Enter, followed by control-d. The program outputs:

    ```
    Adieu, adieu, to Liesl, Friedrich, and Louisa
    ```

Explore this delightful farewell generator and say adieu to your friends in style! 🎭👋
