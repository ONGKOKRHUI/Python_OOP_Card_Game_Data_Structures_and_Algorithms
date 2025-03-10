from __future__ import annotations
from enum import auto, IntEnum
from config import Config
from data_structures import *
'''
You don’t need to define label, name, or value explicitly in your CardLabel class because IntEnum automatically provides these attributes for you. Here's how it works:

Why does CardLabel have .name and .value?
Since CardLabel inherits from IntEnum, each enum member has:

.name → The string name of the enum member (e.g., "DRAW_TWO")
.value → The integer value assigned (e.g., 12 if DRAW_TWO is the 12th item in the enum)
'''
class CardColor(IntEnum):
    """
    Enum class for the color of the card
    """

    RED = 0
    BLUE = auto()
    GREEN = auto()
    YELLOW = auto()
    BLACK = auto()

    def __str__(self) -> str:
        """
        Method to return the string representation of the CardColor

        Args:
            None

        Returns:
            str: The string representation of the CardColor
        """
        return self.name

class CardLabel(IntEnum):
    """
    Enum class for the value of the card
    """

    ZERO = 0
    ONE = auto()
    TWO = auto()
    THREE = auto()
    FOUR = auto()
    FIVE = auto()
    SIX = auto()
    SEVEN = auto()
    EIGHT = auto()
    NINE = auto()
    SKIP = auto()
    REVERSE = auto()
    DRAW_TWO = auto()
    CRAZY = auto()
    DRAW_FOUR = auto()

    def __str__(self) -> str:
        """
        Method to return the string representation of the CardLabel

        Args:
            None

        Returns:
            str: The string representation of the CardLabel
        """
        return self.name


class Card:
    def __init__(self, color: CardColor, label: CardLabel) -> None:
        """
        Initialize the card with the given color and value.

        Args:
            color (CardColor): The color of the card.
            value (CardValue): The value of the card.

        Returns:
            None

        Complexity:
            Best Case:
            Worst Case:
        """
        self.color = color
        self.label = label

    def __str__(self) -> str:
        """
        Return a string representation of the card.

        Optional method for debugging.
        """
        return f"{self.color} {self.label}"

    def __repr__(self) -> str:
        """
        Method to return the string representation of the Card

        Args:
            None

        Returns:
            str: The string representation of the Card
        """
        return str(self)

    def __eq__(self, other: Card) -> bool:
        """
        Check if this card is equal to another card.

        Args:
            other (Card): The other card to compare to.

        Returns:
            bool: True if this card is equal to the other card, False otherwise.
        """
        return self.color == other.color and self.label == other.label
