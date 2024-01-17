CS50p Problem set4: Bitcoin Price Index 📈💰
========================

Description
-----------

Bitcoin Price Index is a Python program, implemented in `bitcoin.py`, as a solution to CS50p Problem Set 4. This program allows users to determine the current cost of a specified number of Bitcoins in USD by querying the CoinDesk Bitcoin Price Index API.

How It Works
------------

1.  **Command-line Argument Handling**: Expects the user to specify the number of Bitcoins they want to buy as a command-line argument. If the argument cannot be converted to a float, the program exits with an appropriate error message.

2.  **API Querying**: Queries the CoinDesk Bitcoin Price Index API (<https://api.coindesk.com/v1/bpi/currentprice.json>) to obtain the current price of Bitcoin in USD. The program catches any exceptions that might occur during the API request.

3.  **Calculation and Output**: Multiplies the number of Bitcoins specified by the user with the current Bitcoin price in USD. It then outputs the result to four decimal places, using a comma as a thousands separator.

Example
-------

-   **Example 1:**

    ```
    python bitcoin.py
    ```

    -   The program exits with an error message: "Missing command-line argument."
-   **Example 2:**

    ```
    python bitcoin.py cat
    ```

    -   The program exits with an error message: "Command-line argument is not a number."
-   **Example 3:**

    ```
    python bitcoin.py 2
    ```

    -   Outputs the price of two Bitcoins to four decimal places in USD.
-   **Example 4:**

    ```
    python bitcoin.py 2.5`
    ```
  

    -   Outputs the price of 2.5 Bitcoins to four decimal places in USD.

Explore Bitcoin Price Index, track the current value of your Bitcoins, and stay informed about cryptocurrency prices! 🚀💹
