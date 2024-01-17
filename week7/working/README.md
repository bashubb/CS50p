CS50p Problem set7: Working 9 to 5
==============

Description
-----------

Welcome to the 9 to 5 converter! This magical script (`working.py`) transforms your work hours from the common 12-hour format to the majestic 24-hour format. 🕘✨

### How It Works

1.  **User Input:**

    -   You provide your working hours in the 12-hour format.
2.  **Conversion Magic:**

    -   The script uses a combination of regex and logical conversion to translate your input into the 24-hour format.
    -   It checks for two specific 12-hour formats: `9 AM to 5 PM` or `9:00 AM to 5:00 PM`.
    -   The input should include spaces before and after "to."
3.  **Output Delight:**

    -   If your input is valid, the script converts and presents the equivalent time in the 24-hour format.
4.  **Error Alert:**

    -   If the input is not in the expected formats or if the times are invalid (e.g., 12:60 AM, 13:00 PM), the script raises a `ValueError`.

### Conversion Table

-   **12-hour Format:** 9:00 AM to 5:00 PM
-   **24-hour Format:** 09:00 to 17:00

### Example


`>>> convert("9 AM to 5 PM") '09:00 to 17:00'`

Now you're ready to experience the magic of the 24-hour realm!

How It Works
------------

The `convert` function employs regular expressions to validate and extract components from the user's input. It then converts the 12-hour times to the 24-hour format and presents the result.

### Additional Details

-   The `convert_time` function ensures accurate conversion, especially handling the nuances of 12:00 AM and 12:00 PM.


That's it! Enjoy your journey into the world of magical time conversion! 🌟
