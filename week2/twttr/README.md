CS50p Problem set 2: Just Setting Up My Twttr 
===========================

This Python program, located in `twttr.py`, serves as a solution to CS50's Problem Set 2. The program mimics the concept of shortening words for text or tweets by omitting vowels. The user is prompted to input a string of text, and the program outputs the same text with all vowels (A, E, I, O, and U) omitted, regardless of case.

🚀 Implementation
-----------------

The program operates as follows:

1.  **User Input:** The program prompts the user to input a string of text.

2.  **Vowel Omission:** It iterates through each letter in the input text, and if the letter is a vowel (either uppercase or lowercase), it omits it from the output.

3.  **Output:** The program then prints the modified text with all vowels removed.

🌟 Example Output
-----------------

-   **Example 1:**

    ```bash
    $ python twttr.py
    Input: Twitter
    Output: Twttr
    ```

-   **Example 2:**

    ```bash
    $ python twttr.py
    Input: What's your name?
    Output: Wht's yr nm?
    ```

-   **Example 3:**

    ```bash
    $ python twttr.py
    Input: CS50
    Output: CS50
    ```

This program provides a simple way to shorten text by removing vowels, replicating the style often used in tweets or texting. Happy Twttring! 🐦
