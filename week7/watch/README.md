CS50p Problem set7: YouTube URL Extractor
=====================

Description
-----------

In this magical YouTube URL extractor (`watch.py`), a function called `parse` performs the enchantment of converting an HTML snippet into a shareable YouTube link. 🪄🔗

### How It Works

1.  **User Input:**

    -   You provide a snippet of HTML, hoping it contains an embedded YouTube video.
2.  **Extraction Magic:**

    -   The program uses a magical technique called "regular expression" (regex) to find YouTube URLs in the HTML.
    -   Specifically, it looks for `iframe` elements with `src` attributes pointing to YouTube's embed links.
    -   If found, it extracts the unique video ID.
3.  **Short and Shareable:**

    -   The extracted video ID is then used to create the shorter, shareable `youtu.be` link.
    -   This link is then presented to you.

### Problem Details

-   The `parse` function is designed to take HTML input and return the corresponding `youtu.be` link if a YouTube video is found. Otherwise, it returns `None`.

-   The expected YouTube URLs are in the following formats:

    -   `http://youtube.com/embed/xvFZjo5PgG0`
    -   `https://youtube.com/embed/xvFZjo5PgG0`
    -   `https://www.youtube.com/embed/xvFZjo5PgG0`


How It Works
------------

The `parse` function uses regular expressions to scan the HTML snippet for `iframe` elements with YouTube embed links (`src`). If a match is found, the video ID is extracted, and a shareable `youtu.be` link is generated.

That's the magic behind the YouTube URL Extractor! 🌟
