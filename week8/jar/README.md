CS50 Problem set8: Cookie Jar  
==================================

Hello there! So, I managed to tackle the Cookie Jar challenge, and this README breaks down my solution. Let's dive into the world of cookies and code without the unnecessary drama.

Meet My Cookie Jar - The `Jar` Class
------------------------------------

Here's the lowdown on the `Jar` class, a solid piece of work designed to handle cookies efficiently.

### `__init__(self, capacity=12):`

I kicked things off by creating a cookie jar with a given capacity. The catch? It needed to be a non-negative integer; otherwise, a ValueError would throw shade.

### `__str__(self):`

To keep it simple, the `__str__` method allowed the jar to display the number of cookies with the help of 🍪 emojis.

### `deposit(self, n):`

Depositing cookies became straightforward. Still, I made sure it didn't go overboard, and if it did, a ValueError would be there to keep things in check.

### `withdraw(self, n):`

For withdrawals, I ensured it was a smooth experience. Attempting to grab more cookies than available triggered a ValueError - just to keep things fair.

### `@property capacity(self):` & `@property size(self):`

These properties spilled the beans on the jar's capacity and the actual cookie count. No surprises, just the facts!

Reveling in Testing Triumphs
----------------------------

In `test_jar.py`, I put the `Jar` class through various tests to ensure its reliability. Each successful test validated my solution and ensured the jar was up to the challenge.

Wrapping It Up
--------------

This README isn't just about code; it's a snapshot of my journey overcoming the Cookie Jar challenge. The `Jar` class stands as proof of my coding prowess, making every line of code as satisfying as a batch of freshly baked cookies. 🍪 Here's to conquering challenges and the joy of coding triumphs!
