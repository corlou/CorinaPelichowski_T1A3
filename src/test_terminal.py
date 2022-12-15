from terminal import TerminalApp
from deck import tarot_cards


# Test Setup
FILE_PATH = "./src/deck.py"
terminal_app = TerminalApp(tarot_cards)

# Check that a card is being returned


def test_get_card_of_the_day():
    # Run the function we're testing
    day_card = terminal_app.get_card_of_the_day()
    # Check that the returned card exists in the deck
    assert day_card in terminal_app.deck


# get_reading works when three random cards are returned AND they are appended to the history

def test_get_reading():
  # Run the function we're testing
    reading_cards = terminal_app.get_reading()
  # check that three cards are being returned
    for card in reading_cards:
        assert card in terminal_app.deck
  # check that the three cards are being added to the reading history
    assert reading_cards in terminal_app.history
