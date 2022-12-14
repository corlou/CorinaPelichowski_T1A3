from terminal import TerminalApp
from deck import tarot_cards


# Test Setup
FILE_PATH = "./src/deck.py"
terminal_app = TerminalApp(tarot_cards)

# Check that a card is being returned


def test_get_card_of_the_day():
    # Run the function we're testing
    day_card = terminal_app.get_card_of_the_day()
    # Check that it returned a string
    assert isinstance(day_card, str)
