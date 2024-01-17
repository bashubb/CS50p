CS50 Problem set8: Seasons of Love
===============

Description
-----------

Welcome to the Seasons of Love calculator! 📅⏳ This heartwarming program, `seasons.py`, helps you measure your life in love---eh, we mean, minutes! Inspired by the iconic song from Rent, it converts the time since your birth into words.

### How It Works

1.  **User Input:**

    -   The program prompts you for your date of birth in the format YYYY-MM-DD.
2.  **Age Calculation:**

    -   Using the `datetime` module, the program calculates the difference between your date of birth and today's date in minutes.
3.  **Magical Conversion:**

    -   The program then beautifully converts this duration into words, echoing the lyrical magic of "Seasons of Love."
4.  **Output Serenade:**

    -   Finally, your age in minutes is sung back to you!

### Example

```python
>>> main()
Date of Birth: 1990-01-01
Twenty-six million, two hundred twenty-nine thousand, six hundred minutes
```

How It Works
------------

The `main` function takes your date of birth, calculates the age in minutes, and prints it using the `convert_to_words` function. The `convert_to_words` function utilizes the `inflect` library to convert the minutes into a lyrical representation.

Celebrate your life in minutes, just like the song suggests! 🎶💖
