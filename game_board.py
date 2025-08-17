"""
This module defines the `GameBoard` class, which manages the card piles.

The `GameBoard` is responsible for handling the `draw_pile` (from which players
take cards) and the `discard_pile` (onto which players play cards). It uses
an ArrayStack for the draw pile to model LIFO (Last-In, First-Out) behavior
and an ArrayList for the discard pile. Key functionalities include drawing a card,
discarding a card, and reshuffling the discard pile back into the draw pile when empty.
"""

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
            Best Case Complexity: O(N + N + N) = O(N), where N is length of cards list, len(cards)
            Worst Case Complexity: O(N + N +N) = O(N), where N is length of cards list, len(cards)
            Explanation: The best and worst case complexity are the same
            - The initialization of draw_pile using ArrayStack requires memory allocation of size N, 
            leading to the first O(N) operation, where N is the length of cards list, len(cards).
            - Then the for loop iterates through cards N times, performing constant-time push() operations, O(N) 
            where N is the length of cards list, len(cards).
            - The initialization of discard_pile using ArrayList requires memory allocation of size N, 
            leading to the third O(N) operation, where N is the length of cards list, len(cards).
            - Since no resizing occurs due to preallocation, the total complexity remains O(N) in both the best and worst cases.
        """
        self.draw_pile = ArrayStack[Card](len(cards))
        #moving cards from cards to draw_pile
        for i in range(len(cards)-1,-1,-1):
            self.draw_pile.push(cards[i])
        self.discard_pile = ArrayList[Card](len(cards))

    def discard_card(self, card: Card) -> None:
        """
        Discards the specified card from the player's hand.

        Args:
            card (Card): The card to be discarded.

        Returns:
            None

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Explanation: 
            - The best and worst case are both constant time
            - The append method is considered to be O(1) as it inserts the card to the end of the list
            which does not require shuffling right of the rest of the cards.
            - We do not consider the complexity of resize as preallocation 
            considers the total number of cards in the game board
        """
        self.discard_pile.append(card)

    def reshuffle(self) -> None:
        """
        Reshuffles cards from the discard pile and add them back to the draw pile.

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity: O(NlogN + N) = O(NlogN), where N is the number of cards in self.discard_pile
            Worst Case Complexity: O(NlogN + N) = O(NlogN), where N is the number of cards in self.discard_pile
            Explanation: 
            - both best and worst case have the same complexity
            - RandomGen.random_shuffle method is considered to be O(NlogN), (given)
            - The for loop runs N times to do constant time push operation, O(1), 
            where N is the number of cards in self.discard_pile, O(N).
            - the clear method is considered to be O(1) since it only assigns the list length to 0
            - The final complexity for both best and worst case are O(NlogN), considering NlogN is worst than N
        """
        RandomGen.random_shuffle(self.discard_pile)
        for i in range(len(self.discard_pile)-1,-1,-1):
            self.draw_pile.push(self.discard_pile[i])     
        self.discard_pile.clear()                

    def draw_card(self) -> Card:
        """
        Draws a card from the draw pile.

        Args:
            None

        Returns:
            Card: The card drawn from the draw pile.

        Complexity:
            Best Case Complexity: O(1)
            Worst Case Complexity: O(NlogN), where N is the number of cards in self.discard_pile
            Explanation:
            - The best case complexity happens when the draw pile is not empty
            - The worst case complexity happens when the draw pile is empty and the reshuffle method is called, O(NlogN)
        """
        if len(self.draw_pile) == 0:
            self.reshuffle()    
        card = self.draw_pile.pop()
        return card
