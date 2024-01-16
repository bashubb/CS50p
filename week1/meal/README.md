CS50p Problem set1: Meal Time
=============

This Python program, residing in `meal.py`, is a solution to CS50's Problem Set 1. It helps you figure out if it's time for breakfast, lunch, or dinner based on the time you input. The program works with 24-hour time, where you type the time as either #:## or ##:##.

📝 Description
--------------

Imagine you're in a country where people typically eat:

-   Breakfast between 7:00 and 8:00
-   Lunch between 12:00 and 13:00
-   Dinner between 18:00 and 19:00

This program asks you for the current time and tells you if it's breakfast, lunch, or dinner time. If it's not mealtime, it won't say anything.

🚀 Implementation
-----------------

The program includes a `convert` function that turns the time into a number so the program can understand it better. The `main` function takes care of getting your input, deciding the mealtime, and giving you the answer.

🎉 Sample Output
----------------

-   If you type "7:00," it will say:

    ```bash

    breakfast time
    ```

-   If you type "12:42," it will say:

    ```bash

    lunch time
    ```

-   If you type "18:32," it will say:

    ```bash

    dinner time
    ```

-   If you type "11:11," it won't say anything because it's not mealtime.

Feel free to try different times and see when the program thinks it's time to eat!

This program makes deciding meal times easy based on the time you provide. Bon appétit! 🍽️
