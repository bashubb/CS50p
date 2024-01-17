CS50p Problem set4: Little Professor 🧮
===================

Description
-----------

Little Professor is a Python program, implemented in `professor.py`, as a solution to CS50p Problem Set 4. This program emulates the classic Little Professor toy, generating ten math problems for the user to solve. It provides interactive prompts, instant feedback for incorrect answers, and ultimately outputs the user's score based on correct responses.

Code Structure
--------------

-   **`main()` Function**: Orchestrates the flow of the program, handling level input, problem generation, user interaction, and scoring.

-   **`get_level()` Function**: Prompts and validates the user input for the level, ensuring it's 1, 2, or 3.

-   **`generate_integer(level)` Function**: Generates a random non-negative integer with a specified number of digits based on the provided level.

-   **User Interaction Loop**: Utilizes loops to prompt the user for each math problem, allowing up to three attempts for incorrect answers.

-   **Scoring Logic**: Maintains a score variable and updates it based on the correctness of the user's answers.

Example
-------

-   **Example 1:**

    -   User inputs `1` at the prompt for Level.
    -   Program poses 10 distinct addition problems with single-digit integers.
    -   Outputs the number of correct answers and exits.
-   **Example 2:**

    -   User inputs `3` at the prompt for Level.
    -   Program poses 10 distinct addition problems with three-digit integers.
    -   Outputs the number of correct answers and exits.

Explore Little Professor, reminisce about the classic toy, and test your math skills!
