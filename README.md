# Welcome to the Tarot Reader Terminal App

## Start the App:

1. Create a new virtual environment: python3 -m venv myenv
   Replace myenv with the desired name for your virtual environment.

2. source myenv/bin/activate

3. Type ./start.sh into the terminal

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

This gets a random card from the list in deck.py and returns it to the user. It does this with the python in-built function called "choice" which loops through the tarot_cards list, selects one random card, and returns it to the user.

#### Feature 4: Star Sign Information

This was used with the Kerykeion package, specifically importing the KrInstance module. It takes three inputs from a user and returns their star sign information with the name, emoji, and the associated element.

#### Feature 5: Print Star Chart

This was also used with the Kerykeion package, specifically the Report module. The user inputs the Day, Month, and Year (all of which have been given a range) and the Report Module returns a table to the user. There's room for expansion there's an option for the user can add other user inputs to view star chart compatibility (not implemented just yet).

#### Feature 6: Next Full Moon

This was used with the fullmoon python package, specifically the NextFullMoon module. A user puts in the request to the module to get the next full moon date and time and the module returns it to the user.

#### Feature 7: Quit

This stops the app and returns a message "Goodbye" with the crystal ball emoji by implementing the Python emoji package.

##### Error Handling:

A way to handle errors was to have a range of numbers for the user to choose between. If their input was out of the range or not a number; an error message would display that provides clear instructions for how to proceed.

NOTE:

- use of variables and the concept of variable scope
- loops and conditional control structures
- error handling

## R7 Implementation Plan

#### Feature 3: Card of the Day

This was the first feature I did as it was the easiest: Take an input from a user and return a random result. I expected this to take 2-3 days (which it did) but the hardest part was the list vs dictionary. The dictionary would return a single random result which is what was needed. Once the code was working, I wrote a test to cover this feature.

##### Feature 1: New Reading and Feature 2: History

Once the single random card return was successful, it was time to return three random cards. I was expecting this to take a week but tit took longer because trying to return a random sample from a dictionary was not an option in Python. So I changed the dictionary to a list and was able to return a single random card (Feature 3) and three random cards (Feature 1). Then it was only a matter of appending the reading to the History option to be called. Once the code was working for this part, I wrote a test to cover these features.

#### Feature 4: Star Sign Information and Feature 5: Star Chart

These were also done in tandem as they both were using the Kerykeion package but implementing different modules. This took about 4 days to complete as the documentation was easy to follow along.

#### Feature 7: Quit

This was done in less than a day as it was very few lines of code and wanted a small easy wim.

#### Feature 6: Next Full Moon

This was done last as I was going to use a Moon API but I found a Python package that did the heavy lifting and returned something simple for the users.

Link to Trello: https://trello.com/invite/b/A1d3SP1k/ATTIc7e0e64d92de7e7682712a1880fd260cA14B80BA/assignment-3-terminal-tarot
NOTE: Some of the dates in trello might be a bit off because I genuinely forgot to use it until almost half way through doing this assignment. As I use Jira for work, please don't let this mishap be a reflection of me as an organised dev.

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
