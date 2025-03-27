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
            Explanation: Creation of ArrayList of size/length which follows the value of Config.NUM_CARDS_AT_INIT, O(N)
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
            Explanation:
            - The best case happens when the array list is not full and append method is called which is constant time, O(1).
            This is because although append method calls insert method which is O(N) where N is the length of the list in worst case,
            append always adds the card to the end of the list, which is constant time, O(1).
            - The worst case happens when the array list is full and resize method is called which is O(N) 
            where N is the length of the list (self.hand). This doubles the internal capacity of the list and copy all existing elements.
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
            Explanation: The best and worst case are both constant time.
            Because in this case, comparison complexity between integers only can be considered constant time.
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
            Explanation: The best and worst case are both constant time.
            The method simply retrieves the stored length of self.hand.
            This retrieval is a direct lookup operation that does not depend on the number of elements in the list.
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
            Best Case Complexity: O(N), where N is length of self.hand
            Worst Case Complexity: O(N + N) = O(N), where N is length of self.hand
            Explanation: 
            - Regardless of best or worst case, the for loop will examine each card in the player's hand, O(N)
            - In this case, all comparison between integers (enum) and between Card objects and None is constant time
            - The best case happens when after the loop, selected card is still None (no playable card)
            which skips the part of removing a playable card (delete_at_index) and returns None.
            - The worst case happens when there is a selected best playable card and the card's index is at the front (selected_index = 0)
            of the list, and delete_at_index is called which is O(len(self.hand) - selected_index),
            but in this case since selected_index is 0, the complexity is simply O(N) 
            where N is the number of cards in player's hand or length of self.hand as all other cards will be shuffled left
        """
        selected_card = None
        selected_index = -1
        for i in range(len(self.hand)): 
            card = self.hand[i]  
            #conditional statement to check if the card is playable
            if card.color == current_color or card.color == CardColor.BLACK or card.label == current_label:
                # If we haven't found a playable card yet, or consitional statement to check if this card is better (smaller)
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

