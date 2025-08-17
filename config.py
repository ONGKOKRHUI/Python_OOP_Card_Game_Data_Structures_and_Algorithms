"""
This module serves as a centralized configuration file for the game.

It contains the `Config` class, which holds static constants and parameters
used throughout the game, such as the total deck size and the number of
cards dealt to players at the start. This approach makes it easy to tweak
game balance and settings from one location.
"""

class Config:
    """
    Config class to store the numbers used in the game
    DO NOT MODIFY
    """

    # Required for the game
    DECK_SIZE = 112
    NUM_CARDS_AT_INIT = 7

    # Optional for debugging purposes, not required for the game
    MAX_ROUNDS_PER_PLAYER = 100
