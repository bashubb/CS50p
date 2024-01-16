CS50p Problem set0: Tip Calculator
====================================

This Python program, `tip.py`, is my solution to the CS50p (CS50 Problems) Problem Set 0 challenge, which involves creating a tip calculator. 

How It Works 🧮
---------------

The tip calculator is designed to take user input for the meal cost and the desired tip percentage, then calculate and output the appropriate tip amount.

1.  **User Input**: The program prompts the user to enter the cost of the meal and the desired tip percentage.

2.  **Conversion Functions**:

    -   `dollars_to_float`: Converts the input representing the meal cost (formatted as $##.##) to a float. It removes the leading $ and returns the amount as a float.
    -   `percent_to_float`: Converts the input representing the tip percentage (formatted as ##%) to a float. It removes the trailing % and returns the percentage as a float.
3.  **Tip Calculation**: The program calculates the tip amount by multiplying the meal cost by the tip percentage.

4.  **Output**: The calculated tip amount is then printed to the console.

Example Usage 💸
----------------

Suppose the user inputs a meal cost of $50.00 and a tip percentage of 15%:

```bash

How much was the meal?
$50.00
What percentage would you like to tip?
15%
Leave $7.50
```

In this example, the program calculates and suggests leaving a $7.50 tip on a $50.00 meal with a 15% tip.
