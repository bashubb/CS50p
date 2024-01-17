CS50 Problem set7: Regular, um, Expressions
========================

Description
-----------

Welcome to the "um" counter! In this magical script (`um.py`), we focus on the subtle art of counting the occurrences of the word "um" in a given line of text. 🧙‍♂️📜

### How It Works

1.  **User Input:**

    -   You provide a line of text where our script will diligently count the occurrences of the word "um."
2.  **Counting Magic:**

    -   The script uses regular expressions to find instances where "um" is a word unto itself, not part of another word.
    -   It's case-insensitive, so "Um," and "um" are both counted.
3.  **Output Delight:**

    -   The script returns the total count of "um" in the provided text.
4.  **Error Alert:**

    -   If there are no instances of "um," the script returns 0.

### Examples


`>>> count("Um, thanks for the album.") 1 >>> count("Um? Um, thanks, um...") 2 >>> count("um") 1`

How It Works
------------

The `count` function employs regular expressions to find instances of "um" as a separate word in the given text. The count is then returned for your um-tastic discovery.

That's it! Now you can confidently count the "ums" in any given text! 🎉
