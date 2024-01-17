CS50p Problem set2: Nutrition Facts 🍏🥑🍓
======================

This Python program, located in `nutrition.py`, serves as a solution to CS50's Problem Set 2. The program prompts users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, based on the FDA's poster for fruits.

🚀 Implementation
-----------------

The program operates as follows:

1.  **User Input:** The program prompts the user to input a fruit (case-insensitively).

2.  **Calorie Lookup:** It checks the user's input against a predefined dictionary (`fruits`) containing fruit names as keys and their corresponding calorie values as values.

3.  **Output:** If the input is a valid fruit, the program prints the number of calories in one portion of that fruit.

🌟 Example Output
-----------------

-   **Example 1:**

    ```

    $ python nutrition.py
    Item: Apple
    Calories: 130
    ```

-   **Example 2:**


    ```
    $ python nutrition.py
    Item: Avocado
    Calories: 50
    ```

-   **Example 3:**

    ```
    $ python nutrition.py
    Item: Sweet Cherries
    Calories: 100
    ```

-   **Example 4:**

    ```
    $ python nutrition.py
    Item: Tomato`

    (No output as Tomato is not in the predefined list of fruits)
    ```

Be sure to try other fruits and vary the casing of your input. The program behaves as expected, case-insensitively.

🍎 Fruits Dictionary
--------------------

The predefined dictionary `fruits` contains calorie information for the following fruits:

-   Apple: 130
-   Avocado: 50
-   Banana: 110
-   Cantaloupe: 50
-   Grapefruit: 60
-   Grapes: 90
-   Honeydew Melon: 50
-   Kiwifruit: 90
-   Lemon: 15
-   Lime: 20
-   Nectarine: 60
-   Orange: 80
-   Peach: 60
-   Pear: 100
-   Pineapple: 50
-   Plums: 70
-   Strawberries: 50
-   Sweet Cherries: 100
-   Tangerine: 50
-   Watermelon: 80

This program provides a quick way to find out the calorie content of various fruits. Enjoy a healthy diet! 🍏🥑🍓
