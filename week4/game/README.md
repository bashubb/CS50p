CS50p Problem set4: Guessing Game
=============

Description
-----------

Guessing Game is a Python program, implemented in `game.py`, as a solution to CS50p Problem Set 4. The game engages the user in a number-guessing challenge within a specified range. It incorporates interactive prompts and feedback to guide the user towards the correct answer.

How It Works
------------

1.  **Level Input**: The program prompts the user for a level, ensuring a valid positive integer input. If an invalid input is provided, the program re-prompts for a valid level.

2.  **Random Number Generation**: A random integer is generated between 1 and the specified level (inclusive).

3.  **Guessing Phase**: The user is prompted to guess the generated number. The program provides feedback for each guess:

    -   If the guess is smaller than the generated number, it outputs "Too small!" and prompts the user for another guess.
    -   If the guess is larger than the generated number, it outputs "Too large!" and prompts the user for another guess.
    -   If the guess is the same as the generated number, it outputs "Just right!" and exits the program.

Example
-------

-   **Example 1:**

    -   User inputs `cat` at the prompt for Level.
    -   Program reprompts for a valid level.
-   **Example 2:**

    -   User inputs `-1` at the prompt for Level.
    -   Program reprompts for a valid level.
-   **Example 3:**

    -   User inputs `10` at the prompt for Level.
    -   Program is ready to accept guesses.
-   **Example 4:**

    -   User inputs `10` at the prompt for Level.
    -   User inputs `cat` as a guess.
    -   Program reprompts for a valid guess.
-   **Example 5:**

    -   User inputs `10` at the prompt for Level.
    -   User inputs `-1` as a guess.
    -   Program reprompts for a valid guess.
-   **Example 6:**

    -   User inputs `1` at the prompt for Level.
    -   User inputs `1` as a guess.
    -   Program outputs "Just right!" and exits.
-   **Example 7:**

    -   User inputs `10` at the prompt for Level.
    -   User inputs `100` as a guess.
    -   Program outputs "Too large!" and prompts for another guess.
-   **Example 8:**

    -   User inputs `10000` at the prompt for Level.
    -   User inputs `1` as a guess.
    -   Program outputs "Too small!" and prompts for another guess.

Explore the Guessing Game, challenge yourself, and try to guess the correct number! 🤔🎮
