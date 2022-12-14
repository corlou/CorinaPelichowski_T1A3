from termcolor import colored
import random
from deck import tarot_cards


class TerminalApp:

    class Option:
        HISTORY = 1
        NEW_READING = 2
        CARD_OF_THE_DAY = 3
        CURRENT_MOON_PHASE = 4

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
        print(colored("4. Current Moon Phase", 'blue'))
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

    def get_card_of_the_day(self):
        day_card = random.choice(list(tarot_cards))
        print(day_card)

    def get_reading(self):
        reading_cards = random.sample(list(tarot_cards), 3)
        self.history.append(reading_cards)
        for card in reading_cards:
            print(card)

    def execute_option(self, option):
        match option:
            case TerminalApp.Option.HISTORY:
                self.get_history()
            case TerminalApp.Option.NEW_READING:
                self.get_reading()
            case TerminalApp.Option.CARD_OF_THE_DAY:
                self.get_card_of_the_day()
            # case TerminalApp.Option.CURRENT_MOON_PHASE:
            #     print("Current Moon Phase was selected")
            #     pass
            case _:
                pass
