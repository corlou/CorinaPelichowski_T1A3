# Welcome to the Tarot Reader Terminal App

## R1 - Documentation

Answers to all the documentation requirements below.

## R2 README Requirements

Your README.md should have a separate heading for each documentation requirement and answers organised under the appropriate headings.

## R3 Reference List

Provide full attribution to referenced sources (where applicable).

### References:

Ankthon (2018) _Python: Random.sample() function_, _GeeksforGeeks_. Available at: https://www.geeksforgeeks.org/python-random-sample-function/?ref=rp (Accessed: December 13, 2022).

Battaglia, G. (2022) _Kerykeion - Python Library for Astrology_, _PyPI_. Available at: https://pypi.org/project/kerykeion/ (Accessed: December 10, 2022).

Hadzhiev, B. (2022) _Get Random Key and Value from a Dictionary in Python_, _bobbyhadz_. Available at: https://bobbyhadz.com/blog/python-get-random-key-value-from-dictionary (Accessed: December 11, 2022).

JRK (2020) _Fullmoon Python Package_, _PyPI_. Available at: https://pypi.org/project/fullmoon/ (Accessed: December 10, 2022).

Kim, T., Wurster, K. and Jalilov, T. (2022) _Emoji Python Package_, _PyPI_. Available at: https://pypi.org/project/emoji/ (Accessed: December 12, 2022).

Lepa, K. (no date) _Termcolor Python Package_, _PyPI_. Available at: https://pypi.org/project/termcolor/ (Accessed: December 12, 2022).

Ramos, L.P. (2019) _How to run your Python Scripts_, _Real Python_. Real Python. Available at: https://realpython.com/run-python-scripts/ (Accessed: December 11, 2022).

Rigoulet, X. (2022) _The Python Requirements File and How to Create it_, _LearnPython.com_. LearnPython.com. Available at: https://learnpython.com/blog/python-requirements-file/ (Accessed: December 17, 2022).

Says, C. and Says, W. (2022) _The Complete 78 Tarot Cards List_, _A Little Spark of Joy_. Available at: https://www.alittlesparkofjoy.com/tarot-cards-list/ (Accessed: December 13, 2022).

Van Rossum, G., Warsaw, B. and Coghlan, N. (2001) _PEP 8 - Style Guide for Python Code_. Available at: https://peps.python.org/pep-0008/ (Accessed: December 8, 2022).

Vishal, V. (2021) _Python random choice() function to select a random item from a list and set_, _PYnative_. Available at: https://pynative.com/python-random-choice/#h-select-multiple-random-choices-from-a-list (Accessed: December 13, 2022).

## R4 Link to Repo

Link to source control repository: https://github.com/corlou/CorinaPelichowski_T1A3
Link to Presentation on Vimeo: https://vimeo.com/782220290/ff6f2a5d3d

## R5 Code Style

PEP 8 - Style Guide for Python Code has been utilised.
Some examples include (but not limited to):

- Use 4 spaces per indentation level.
- The closing bracket on multiline constructs may either line up under the first non-whitespace character of the last line of list, or it may be lined up under the first character of the line that starts the multiline construct. See deck.py for example.
- Imports are listed with Standard library imports first and then Related third party imports second.
- Comments should be complete sentences. The first word should be capitalized, unless it is an identifier that begins with a lower case letter (never alter the case of identifiers!).

## R6 List of Features

### Features of the App

#### Feature 1: New Reading

A user selects 1 to get a Tarot reading. There are many ways to get a Tarot reading so I went for the simplest option. Using the inbuilt Python option "sample" with the class "NUMBER_OF_CARDS_IN_READING = 3", the code was able to loop three times until it got to three and then return three random cards from list in deck.py file.

#### Feature 2: History of Readings

Every time a user gets a reading, that reading is appended to history which is then called in this menu option. But it's just just being called and returned; the object is also changed slightly to display in way that has ease of readability.

#### Feature 3: Card of the Day

This gets a random card from the list in deck.py and returns it to the user. It does this with the python in-built function called "choice".

#### Feature 4: Star Sign Information

This was used with the Kerykeion package, specifically importing the KrInstance module.

#### Feature 5: Print Star Chart

This was also used with the Kerykeion package

#### Feature 6: Next Full Moon

This was used with the fullmoon python package

#### Feature 7: Quit

This stops the app and returns a message "Goodbye" with the crystal ball emoji.

##### Error Handling:

A way to handle errors was to have a range of numbers for the user to choose between. If their input was out of the range or not a number; an error message would display that provides clear instructions for how to proceed.

NOTE:

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

## R7 Implementation Plan

NOTE:

- outlines how each feature will be implemented and a checklist of tasks for each feature

- prioritise the implementation of different features, or checklist items within a feature
- provide a deadline, duration or other time indicator for each feature or checklist/checklist-item

Utilise a suitable project management platform to track this implementation plan.

Provide screenshots/images and/or a reference to an accessible project management platform used to track this implementation plan.

## R8 Instructions for Installation

This app requires both pip and python.

#### Pip install instructions: https://pip.pypa.io/en/stable/installation/

#### Python install instructions: https://www.python.org/downloads/

- Once those have been completed, open a Terminal or Powershell and go into the folder src.
- Type the command ./start.sh and wait for any packages/dependencies to be installed
- Then you will be presented with the app menu and you're free to make your selections to use the app.

### When the App is running:

When you run the app, select from the following options:

1. Get a new card reading
2. Get history of card readings
3. Get a random "Card of the Day"
4. Get your star sign and element
5. Print out a Star Chart
6. Find out when the next full moon is
7. Quit

Please note, when selecting Option 4: Star Sign, you will need to type the day as a number, press Enter, then type your month as a number, and press Enter to reveal your star sign. For example: 31st October will be 31 + enter + 10 + enter which will reveal "Sco Water" which is Scorpio and the element is Water.

Key:
Aqu ♒️ = Aquarius
Pis ♓️ = Pisces
Ari ♈️ = Aries
Tau ♉️ = Taurus
Gem ♊️ = Gemini
Can ♋️ = Cancer
Leo ♌️ = Leo
Vir ♍️ = Virgo
Lib ♎️ = Libra
Sco ♏️ = Scorpio
Sag ♐️ = Sagittarius
