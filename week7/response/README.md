CS50p Problem set 7: Response Validation
===================

Description
-----------

Welcome to the Response Validation tool! This handy program, `response.py`, uses the power of validators from PyPI to determine whether an email address is syntactically valid. 📧✨

### How It Works

1.  **User Input:**

    -   The program prompts you for an email address.
2.  **Validation Magic:**

    -   Utilizing the `validators` library, the program checks if the input is a syntactically valid email address.
3.  **Output Delight:**

    -   The program prints "Valid" if the email address is valid and "Invalid" otherwise.

### Examples

```python
>>> validate("malan@harvard.edu")
Valid >>>
validate("your_email@example.com")
Valid
>>> validate("malan@@@harvard.edu")
Invalid
>>> validate("typo.email@example..com")
Invalid
```

How It Works
------------

The `validate` function uses the `validators.email` method to check if the provided input is a syntactically valid email address. It returns "Valid" if true, and "Invalid" if not.


That's it! Now you can effortlessly validate email addresses with this nifty tool. 🌐✅
