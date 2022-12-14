from termcolor import colored
import random
from deck import tarot_cards
from kerykeion import KrInstance


class TerminalApp:
    NUMBER_OF_CARDS_IN_READING = 3

    class Option:
        HISTORY = 1
        NEW_READING = 2
        CARD_OF_THE_DAY = 3
        STAR_SIGN = 4

    def run(self):
        while True:
            self.print_options()
            option = self.get_user_selection()
            self.execute_option(option)

    def print_options(self):
        print(colored("-------------OPTIONS-------------", 'white'))
        print(colored("1. History", 'green'))
        print(colored("2. New Reading", 'yellow'))
        print(colored("3. Card of the Day", 'red'))
        print(colored("4. Star Sign Information", 'blue'))
        print(colored("---------------------------------", 'white'))

    def get_user_selection(self):
        while True:
            try:
                option = int(input("Select an option: "))
                if not option in range(1, 5):
                    raise ValueError
                break
            except ValueError:
                print("Please enter a valid option.")

        return option

    def __init__(self, deck):
        self.deck = deck
        self.history = []

    def get_history(self):
        for i, val in enumerate(self.history):
            print("Reading {}".format(i + 1))
            for j, card in enumerate(val):
                print("Card {}: {}".format(j + 1, card))
            print("------------------------------")
        return self.history

    def get_card_of_the_day(self):
        day_card = random.choice(list(tarot_cards))
        print(day_card)
        return day_card

    def get_reading(self):
        reading_cards = random.sample(
            list(tarot_cards), TerminalApp.NUMBER_OF_CARDS_IN_READING)
        self.history.append(reading_cards)
        for card in reading_cards:
            print(card)
        return reading_cards

    def get_star_sign(self):
        day = int(input("Day: "))
        month = int(input("Month: "))
        obj = KrInstance("User", 2000, month, day, 20, 30)
        info = obj.sun
        print("Information")
        print("Sign: {} {} {} {}".format(
            info["sign"], info["emoji"], info["element"], info["quality"]))

    def execute_option(self, option):
        match option:
            case TerminalApp.Option.HISTORY:
                self.get_history()
            case TerminalApp.Option.NEW_READING:
                self.get_reading()
            case TerminalApp.Option.CARD_OF_THE_DAY:
                self.get_card_of_the_day()
            case TerminalApp.Option.STAR_SIGN:
                self.get_star_sign()
            case _:
                # Decide what kind of exception should be raised
                raise Exception()
