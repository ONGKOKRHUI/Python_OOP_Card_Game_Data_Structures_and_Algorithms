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
            - The constructor initializes two dynamic arrays (draw_pile and discard_pile), 
            each requiring memory allocation of size N, leading to an O(N) operation per allocation. 
            - Additionally, the loop iterates through cards N times, performing constant-time push() operations. 
            Since no resizing occurs due to preallocation, the total complexity remains O(N) in both the best and worst cases.
        """
        self.draw_pile = ArrayStack[Card](len(cards))
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
            Explanation: The best and worst case are both constant time
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
            - RandomGen.random_shuffle method is considered to be O(NlogN)
            - The for loop runs N times, where N is the number of cards in self.discard_pile.
            - The final complexity for both best and worst case are O(NlogN) which is the worst case complexity
        """
        RandomGen.random_shuffle(self.discard_pile)
        for i in range(len(self.discard_pile)-1,-1,-1):
            self.draw_pile.push(self.discard_pile[i])       #O(1)
        self.discard_pile.clear()                           #O(1)

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
