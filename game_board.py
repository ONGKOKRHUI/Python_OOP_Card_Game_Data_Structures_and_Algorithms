from __future__ import annotations
from card import Card
from random_gen import RandomGen
from config import Config
from data_structures import *


class GameBoard:
    """
    GameBoard class to store cards in draw pile and discard pile
    """

    def __init__(self, cards: ArrayList[Card]):
        """
        Constructor for the GameBoard class

        Args:
            cards (ArrayList[Card]): The list of cards to be used in the game

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.draw_pile = cards
        self.discard_pile = ArrayList[Card]()

    def discard_card(self, card: Card) -> None:
        """
        Discards the specified card from the player's hand.

        Args:
            card (Card): The card to be discarded.

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.discard_pile.insert(len(self.discard_pile), card)

    def reshuffle(self) -> None:
        """
        Reshuffles cards from the discard pile and add them back to the draw pile.

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        RandomGen.random_shuffle(self.discard_pile)
        self.draw_pile =  self.discard_pile
        self.discard_pile = ArrayList[Card]()

    def draw_card(self) -> Card:
        """
        Draws a card from the draw pile.

        Args:
            None

        Returns:
            Card: The card drawn from the draw pile.

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        if len(self.draw_pile) == 0:
            self.reshuffle()    
        card = self.draw_pile.delete_at_index(0)
        return card
