from terminal import TerminalApp
from deck import tarot_cards


# Test Setup
FILE_PATH = "./src/deck.py"
terminal_app = TerminalApp(tarot_cards)

# Check that a card is being returned


def test_get_card_of_the_day():
    # Run the function to get a random card
    day_card = terminal_app.get_card_of_the_day()
    # Check that the returned card exists in the deck
    assert day_card in terminal_app.deck


# get_reading works when 3 random cards are returned AND are appended to History

def test_get_reading():
  # Run the function
    reading_cards = terminal_app.get_reading()
  # Check that three cards are being returned
    for card in reading_cards:
        assert card in terminal_app.deck
  # Check that the three cards are being added to the reading history
    assert reading_cards in terminal_app.history
