CS50 p Problem set7: IPv4 Address Validator
======================

The `numb3rs.py` program is your friendly IPv4 address checker! 🌐✨

How It Works
------------

1.  **User Input:**

    -   You type in an IPv4 address, like `127.0.0.1`.
    -   Press Enter.
2.  **Validation Magic:**

    -   The program uses a smart trick called a "regular expression" to see if your input looks like a real IPv4 address.
    -   Checks if your address has four groups of numbers separated by dots, with each group ranging from 0 to 255.
    -   It then decides: Is it a valid IPv4 or not?
3.  **The Verdict:**

    -   If your address checks out, it shouts out a cheerful `True`!
    -   If something seems fishy, it says `False`.

Example
-------

```
$ python numb3rs.py
IPv4 Address: 127.0.0.1
True
```

🎉 Voila! Your IPv4 address is validated!

Feel free to play around and explore. Happy validating! 🚀🕵️‍♂️
