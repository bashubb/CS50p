CS50p Problem set 8: CS50 Shirtificate Generator 
====================================================

Overview
--------

The CS50 Shirtificate Generator is a Python script developed as a solution for Problem Set 8 of CS50. This script leverages the `fpdf` library to create personalized CS50 shirtificates in PDF format. It provides users with a unique and visually appealing certificate by overlaying their name on the iconic CS50 shirt image.

Features
--------

-   **Header Design:** The PDF opens with a professional header, centered horizontally, displaying "CS50 Shirtificate" using a specified font and size.

-   **Main Attraction:** The CS50 shirt image is positioned at the center of the PDF, creating the visual foundation for the shirtificate. The user's name, provided as input, is overlaid on the shirt in white text, adding a personal touch.

How It Works
------------

1.  **Initialization:** The script creates an instance of the `PDF` class, extending the `fpdf.FPDF` class, to define the PDF structure and design.

2.  **Header Design:** The `header` method in the `PDF` class sets up the PDF header, including the placement of the CS50 shirt image and the "CS50 Shirtificate" text.

3.  **Main Attraction:** The `shirt` function generates a new PDF page with Portrait orientation and A4 format. It sets the font and text color, positioning the user's name at a specified location on the shirt image.

4.  **User Interaction:** The `main` function prompts the user for their name, serving as the personalized element for the shirtificate.

5.  **PDF Output:** The script generates the PDF file, `shirtificate.pdf`, containing the CS50 shirt image with the user's name.


Additional Information
----------------------

-   **Problem Set 8 Solution:** This script is a solution for Problem Set 8 of CS50.

-   **Dependencies:** Ensure the `fpdf` library is installed (`pip install fpdf`).

-   **CS50 Shirt Image:** The script requires the `shirtificate.png` image in the same directory.

-   **Customization:** Users can modify the script to tailor the appearance further.


Sample Output
----------------------

<img src="https://github.com/bashubb/CS50p/blob/main/week8/shirtificate/shirtificate.png" width="40%" height="40%" />
<img src="https://github.com/bashubb/CS50p/blob/main/week8/shirtificate/shirtificate-jpg.jpg"  width="40%" height="40%">


Feel free to run the script and create your personalized CS50 Shirtificate!
