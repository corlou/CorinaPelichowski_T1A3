from terminal import TerminalApp
from deck import tarot_cards


# Global variable
FILE_PATH = "./src/deck.py"


def main():

    terminal_app = TerminalApp(tarot_cards)
    terminal_app.run()


if __name__ == "__main__":
    main()
