CS50 Problem set2: Coke Bottle 🥤
=====================

This Python program, located in `coke.py`, serves as a solution to CS50's Problem Set 2. The program simulates a Coke machine that sells bottles of Coca-Cola for 50 cents and only accepts coins in denominations of 25 cents, 10 cents, and 5 cents.

🚀 Implementation
-----------------

The program operates as follows:

1.  **Initialization:** The program starts with an initial amount of 50 cents that the user needs to pay.

2.  **User Interaction:** It prompts the user to insert a coin, one at a time, each time informing the user of the amount due.

3.  **Payment:** The user inputs coins, and the program deducts the corresponding value from the amount due.

4.  **Change Calculation:** Once the user has inputted at least 50 cents, the program outputs how many cents in change the user is owed.

🌟 Example Output
-----------------

-   **Example 1:**

   ```bash

    $ python coke.py
    Insert Coin: 25
    Amount Due: 25
    Insert Coin: 10
    Amount Due: 15
    Insert Coin: 5
    Amount Due: 10
    Insert Coin: 30
    Amount Due: 10
    Insert Coin: 25
    Amount Due: 0
    Change Owed: 0
   ```

-   **Example 2:**

    ```bash

    $ python coke.py
    Insert Coin: 25
    Amount Due: 25
    Insert Coin: 10
    Amount Due: 15
    Insert Coin: 25
    Amount Due: 0
    Change Owed: 10
    ```

This program provides a simple simulation of a Coke machine, handling user input and calculating change owed. Cheers! 🥤💰
