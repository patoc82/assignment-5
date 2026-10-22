Overview
    This repository contains two Python programs for Assignment 5. The programs demonstrate conditionals, while loops, exception handling, functions, Python libraries, command-line input, and API usage.

Files
    pos_checkout.py — A point-of-sale checkout system that calculates purchase totals, discounts, and a seed-based member perk.

    inventory_spotcheck.py — An inventory analyzer that identifies products requiring reorder and performs an API spot check using the iTunes Search API.

Requirements

    Python 3.x

    The requests library for the inventory spot-check program

    An internet connection for the API request

Installation

    Install the required dependency by running this command in the VS Code terminal:

    pip install requests

        If pip does not work, try:

        python -m pip install requests

How to Run

Open the repository folder in VS Code and open the terminal.

Exercise 1: Point-of-Sale Checkout

Run:

    python pos_checkout.py

Enter your student key when prompted. Then enter each item's name, unit price, and quantity. Type DONE when you have finished entering items.

The program calculates the subtotal, units purchased, applicable discount, member perk, and final total.

Exercise 2: Inventory Reorder Analyzer

Run:

    python inventory_spotcheck.py

Enter your student key when prompted. Then enter each SKU and its on-hand inventory quantity. Type DONE when you have finished entering inventory items.

The program determines which SKUs require reorder, calculates the reorder statistics, and performs an iTunes Search API spot check.

Personalization

    Both programs calculate a seed using the student's key:

    seed = sum(ord(ch) for ch in student_key.strip())

    The seed determines the checkout perk, inventory reorder threshold, and API search term.

Error Handling

    Both programs validate user input and reprompt when an invalid value is entered.

    The inventory program also handles API request failures and invalid or unexpected JSON responses.

API Used

    The inventory program uses the iTunes Search API:

    https://itunes.apple.com/search

    The request searches for songs using either weezer or drake, depending on whether the seed is even or odd.

Running the Programs

    Run each program separately from the terminal. The checkout program does not require an internet connection, while the inventory program requires the requests library and an internet connection for its API request.