CS50p Problem set2: License Plate 🚗
=====================

This Python program, located in `plates.py`, serves as a solution to CS50's Problem Set 2. The program checks whether a given vanity license plate meets the specific requirements set by the Massachusetts Registry of Motor Vehicles. The requirements include:

1.  **Minimum and Maximum Length:** The plate must have a minimum length of 2 characters and a maximum length of 6 characters (letters or numbers).

2.  **Starting with Letters:** All vanity plates must start with at least two letters.

3.  **Numbers at the End:** Numbers are allowed only at the end of the plate.

4.  **Avoiding Periods, Spaces, or Punctuation Marks:** No periods, spaces, or punctuation marks are allowed in the plate.

🚀 Implementation
-----------------

The program operates as follows:

1.  **User Input:** The program prompts the user to input a vanity license plate.

2.  **Validation:** It checks whether the input meets the specified requirements using the `is_valid` function.

3.  **Output:** The program prints "Valid" if the plate is valid and "Invalid" otherwise.

🌟 Example Output
-----------------

-   **Example 1:**

  ```bash

    $ python plates.py
    Plate: CS50 Valid
```

-   **Example 2:**

  ```bash

    $ python plates.py  
    Plate: CS05 Invalid
```

-   **Example 3:**

  ```bash

    $ python plates.py
    Plate: CS50P Invalid
```

-   **Example 4:**

  ```bash

    $ python plates.py
    Plate: PI3.14 Invalid
```

-   **Example 5:**

  ```bash

    $ python plates.py
    Plate: H Invalid
```

-   **Example 6:**

  ```bash

    $ python plates.py
    Plate: OUTATIME Invalid
```

This program provides a quick way to determine the validity of a vanity license plate based on the Massachusetts regulations. Happy driving! 🚗
