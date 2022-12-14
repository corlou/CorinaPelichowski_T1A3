from random import choice, sample
from sys import exit
from termcolor import colored
from kerykeion import Report, KrInstance
from fullmoon import NextFullMoon
import emoji


class TerminalApp:
    NUMBER_OF_CARDS_IN_READING = 3
    DAY_RANGE = (1, 32)
    MONTH_RANGE = (1, 13)
    YEAR_RANGE = (1920, 2030)
    OPTION_RANGE = (1, 8)
    DIVIDER_LEN = 20

    class Option:
        NEW_READING = 1
        HISTORY = 2
        CARD_OF_THE_DAY = 3
        STAR_SIGN = 4
        STAR_CHART = 5
        FULL_MOON = 6
        QUIT = 7

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
        print(colored("5. Print Star Chart", 'magenta'))
        print(colored("6. Next Full Moon", 'white'))
        print(colored("7. Quit", 'red'))
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

    # Get a history of readings
    def get_history(self):
        return self.history
    
    # Show a history of readings
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
        # This will store the star sign info after we get user input
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

    # Get star chart
    def get_star_chart(self, year, month, day):
      star_report = KrInstance("User", day=day, month=month, year=year)
      return star_report
      
    
    # Show star chart
    def print_star_chart(self):
       # This will store the star chart info after we get user input
        star_chart = None
        try:
          # User inputs a number to select a day
            day_input = self.get_int_input_from_terminal(
                "Day: ", TerminalApp.DAY_RANGE)
            # User inputs a number to select a month
            month_input = self.get_int_input_from_terminal(
                "Month: ", TerminalApp.MONTH_RANGE)
                # User inputs a number to select a year
            year_input = self.get_int_input_from_terminal(
                "Year: ", TerminalApp.YEAR_RANGE)
            # Get star chart based on user's input for day, month, and year 
            star_chart = self.get_star_chart(
                year_input,
                month_input,
                day_input
            )
        except ValueError as e:
            print(e)
        report = Report(star_chart)
        report.print_report()


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
                    "Please enter a valid whole number. Between 1-7 for Menu, 1-31 for Day, 1-12 for Month.")
        return option

    def quit(self):
        farewell = emoji.emojize(':crystal_ball: Goodbye')
        print(farewell)
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
            case TerminalApp.Option.STAR_CHART:
                self.print_star_chart()
            case TerminalApp.Option.FULL_MOON:
                self.print_next_full_moon()
            case TerminalApp.Option.QUIT:
                self.quit()
