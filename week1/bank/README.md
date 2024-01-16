CS50p Problem set 1: Home Federal Savings Bank  💰
================================================================

Description
-----------

In this Python program, `bank.py`, the Home Federal Savings Bank Greet-O-Meter evaluates greetings and rewards the user based on specific criteria. The program prompts the user for a greeting and then determines the monetary reward as follows:

1.  If the greeting starts with "hello," the output is $0.
2.  If the greeting starts with an "h" (but not "hello"), the output is $20.
3.  For all other greetings, where neither "hello" nor an "h" initiates the salutation, the output is $100.

The program ignores any leading whitespace in the user's greeting and treats the greeting case-insensitively.

How It Works
------------

1.  **Prompt User**: The program asks the user to input a greeting.

2.  **Evaluate Greeting**: It checks the user's input against specific conditions:

    -   If the greeting contains "hello" at the beginning, the reward is $0.
    -   If the greeting starts with an "h" (excluding "hello"), the reward is $20.
    -   For all other greetings, the reward is $100.
3.  **Output Reward**: The program then prints the corresponding monetary reward based on the evaluation.
