from __future__ import annotations
from card import Card, CardColor, CardLabel
from config import Config
from data_structures import *


class Player:
    """
    Player class to store the player details
    """

    def __init__(self, name: str) -> None:
        """
        Constructor for the Player class

        Args:
            name (str): The name of the player
            position (int): The position of the player  ##DONT HAVE LEH

        Returns:
            None

        Complexity:
            Best Case Complexity: O(N), where N is Config.NUM_CARDS_AT_INIT
            Worst Case Complexity: O(N), where N is Config.NUM_CARDS_AT_INIT
            Explanation: Creation of ArrayList of size Config.NUM_CARDS_AT_INIT which is the number of cards in
                         the player's hand during initialise of game
        """
        self.name = name
        self.hand = ArrayList[Card](Config.NUM_CARDS_AT_INIT)

    def add_card(self, card: Card) -> None:
        """
        Method to add a card to the player's hand

        Args:
            card (Card): The card to be added to the player's hand

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1) 
            Worst Case Complexity: O(N), where N is length of self.hand
            Explanation: In this case, the addition of a card to the player's hand can be constant time.
            This is because although append method calls insert method which is O(N) where N is the length of the list,
            append only adds the card to the end of the list, which is constant time.
            The best case happens when the array list is not full.
            The worst case happens when the array list is full and resize method is called which is O(N) 
            where N is the length of the list
        """
        self.hand.append(card)

    def is_empty(self) -> bool:
        """
        Method to check if the player's hand is empty

        Args:
            None

        Returns:
            bool: True if the player's hand is empty, False otherwise

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Explanation: The best and worst case are both constant time although comparison happens which is not always O(1)
            But in this case, comparison between integers only can be considered constant time
        """
        return len(self.hand) == 0

    def cards_in_hand(self) -> int:
        """
        Method to check the number of cards left in the player's hand

        Args:
            None

        Returns:
            int: The number of cards left in the player's hand

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Explanation: The best and worst case are both constant time
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
            Best Case Complexity: O(N*comp1*comp2 + comp3), where N is the number of cards in the player's hand, len(self.hand)
            Worst Case Complexity: O(N*comp1*comp2 + comp3 + N), where N is the number of cards in the player's hand, len(self.hand)
            Explanation: 
            comp1: comparison between current color and card color and current label and card label to determine playable cards
            comp2: comparison between selected card object and None and comparison between selected card numbers and labels
                   to choose the best card 
            comp3: comparison between the selected card object and None to determine if selected card is available
            The best case happens when the player does not have a playable card which will loop through all the cards in the hand O(N)
            and conduct comparison comp1, comp2 and comp3 then return None
            The worst case happens when the player has a playable card which will loop through all the cards in the hand O(N)
            and conduct comparison comp1, comp2 and comp3 then delete the card at index O(N) before returning the selected card
        """
        selected_card = None
        selected_index = -1
        for i in range(len(self.hand)): 
            card = self.hand[i]  
            if card.color == current_color or card.color == CardColor.BLACK or card.label == current_label:
                # If we haven't found a playable card yet, or this card is better
                if selected_card is None or (card.color < selected_card.color or 
                                            (card.color == selected_card.color and card.label < selected_card.label)):
                    selected_card = card
                    selected_index = i
        
        # If we found a playable card, remove it from hand and return it
        if selected_card is not None:       
            self.hand.delete_at_index(selected_index)
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

