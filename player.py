from __future__ import annotations
from card import Card, CardColor, CardLabel
from config import Config
from data_structures import *


class Player:
    """
    Player class to store the player details
    """

    def __init__(self, name: str) -> None: #position: int
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player  ##DONT HAVE LEH

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
        """
        self.name = name
        #self.position = position
        self.hand = ArrayList[Card](Config.NUM_CARDS_AT_INIT)

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.hand.insert(len(self.hand), card)

    def is_empty(self) -> bool:
        """
        Method to check if the player's hand is empty

        Args:
            None

        Returns:
            bool: True if the player's hand is empty, False otherwise

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return True if len(self.hand) == 0 else False

    def cards_in_hand(self) -> int:
        """
        Method to check the number of cards left in the player's hand

        Args:
            None

        Returns:
            int: The number of cards left in the player's hand

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        return len(self.hand)

    def play_card(
        self, current_color: CardColor, current_label: CardLabel
    ) -> Card | None:
        """
        Method to play a card from the player's hand

        Args:
            current_color (CardColor): The current color of the game
            current_label (CardLabel): The current label of the game

        Returns:
            Card: The first card that is playable from the player's hand  

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        playable_cards = ArrayList[Card]()
        for card in self.hand:
            if card.color == current_color or card.label == current_label:
                playable_cards.insert(len(playable_cards), card)
        if len(playable_cards) > 0:
            selected_card = playable_cards.__getitem__(0)
            index = 0
            for idx, card in enumerate(playable_cards):
                if card.color < selected_card.color:
                    index, selected_card = idx, card
                elif card.color == selected_card.color:
                    if card.label < selected_card.label:
                        index, selected_card = idx, card
            self.hand.delete_at_index(index)
            return selected_card
        return None

    def __str__(self) -> str:
        """
        Return a string representation of the player.

        Optional method for debugging.

        """
        return self.name

    def __repr__(self) -> str:
        """
        Method to return the string representation of the player

        Args:
            None

        Returns:
            str: The string representation of the player
        """
        return str(self)
