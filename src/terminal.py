from random import choice, sample
from sys import exit
from termcolor import colored
from kerykeion import KrInstance
from fullmoon import NextFullMoon


class TerminalApp:
    NUMBER_OF_CARDS_IN_READING = 3
    MONTH_RANGE = (1, 13)
    DAY_RANGE = (1, 32)
    OPTION_RANGE = (1, 7)
    DIVIDER_LEN = 20

    class Option:
        NEW_READING = 1
        HISTORY = 2
        CARD_OF_THE_DAY = 3
        STAR_SIGN = 4
        FULL_MOON = 5
        QUIT = 6

    def run(self):
        while True:
            self.print_options()
            option = self.get_int_input_from_terminal(
                "Select an option: ", TerminalApp.OPTION_RANGE)
            self.execute_option(option)

    def print_options(self):
        self.print_divider(
            TerminalApp.DIVIDER_LEN, "OPTIONS", '*', 'magenta')
        print(colored("1. New Reading", 'yellow'))
        print(colored("2. History", 'green'))
        print(colored("3. Card of the Day", 'white'))
        print(colored("4. Star Sign Information", 'blue'))
        print(colored("5. Next Full Moon", 'white'))
        print(colored("6. Quit", 'red'))
        self.print_divider(
            TerminalApp.DIVIDER_LEN, divider='*', color='magenta')

    def print_divider(self, length, title='', divider='-', color='white'):
        d = divider * (length - int(len(title) / 2))
        d += title
        d += divider * (length - int(len(title) / 2))
        print(colored(d, color))

    def __init__(self, deck):
        self.deck = deck
        self.history = []

    # Get reading and append to History

    def get_reading(self):
        reading_cards = sample(
            (self.deck), TerminalApp.NUMBER_OF_CARDS_IN_READING)
        self.history.append(reading_cards)
        return reading_cards

    # Show the reading
    def print_reading(self):
        reading_cards = self.get_reading()
        for card in reading_cards:
            print(card)

    def get_history(self):
        return self.history

    def print_history(self):
        history = self.get_history()
        for i, val in enumerate(history):
            print("Reading {}".format(i + 1))
            for j, card in enumerate(val):
                print("Card {}: {}".format(j + 1, card))
            self.print_divider(TerminalApp.DIVIDER_LEN)

    # Get a random card from the list
    def get_card_of_the_day(self):
        return choice(self.deck)

    # Show the random card from the list
    def print_card_of_the_day(self):
        day_card = self.get_card_of_the_day()
        print(day_card)

    # Get star sign
    def get_star_sign(self, day, month):
        info = KrInstance("User", month=month, day=day).sun
        return info

    # Show star sign
    def print_star_sign(self):
        # this will store the star sign info after we get user input
        star_sign = None
        try:
            # User inputs a number to select a day
            day_input = self.get_int_input_from_terminal(
                "Day: ", TerminalApp.DAY_RANGE)
            # User inputs a number to select a month
            month_input = self.get_int_input_from_terminal(
                "Month: ", TerminalApp.MONTH_RANGE)
            # Get star sign based on user's input for day and month
            star_sign = self.get_star_sign(
                day_input,
                month_input
            )
        except ValueError as e:
            print(e)
        # Show star sign info to user
        print("Information")
        self.print_divider(TerminalApp.DIVIDER_LEN)
        print("Sign: {} {} {}".format(
            star_sign["sign"], star_sign["emoji"], star_sign["element"]))

    # Get the next Full Moon
    def get_next_full_moon(self):
        n = NextFullMoon()
        return n.next_full_moon()

    # Show the Next Full Moon
    def print_next_full_moon(self):
        moon = self.get_next_full_moon()
        print("The next full moon will be: " + str(moon))

    def get_int_input_from_terminal(self, prompt, range_):
        while True:
            try:
                option = int(input(prompt))
                if not option in range(range_[0], range_[1]):
                    raise ValueError
                break
            except ValueError:
                print(
                    "Please enter a valid whole number. Between 1-5 for Menu, 1-31 for Day, 1-12 for Month.")
        return option

    def quit(self):
        print("\N{crystal ball}" + " Goodbye")
        exit(0)

    def execute_option(self, option):
        match option:
            case TerminalApp.Option.NEW_READING:
                self.print_reading()
            case TerminalApp.Option.HISTORY:
                self.print_history()
            case TerminalApp.Option.CARD_OF_THE_DAY:
                self.print_card_of_the_day()
            case TerminalApp.Option.STAR_SIGN:
                self.print_star_sign()
            case TerminalApp.Option.FULL_MOON:
                self.print_next_full_moon()
            case TerminalApp.Option.QUIT:
                self.quit()
