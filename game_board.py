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
            Best Case Complexity: O(N + N +N), where N is length of cards list, len(cards)
            Worst Case Complexity: O(N + N +N), where N is length of cards list, len(cards)
            Explanation: The best and worst case complexity are the same
                         Creation of ArrayStack draw_pile of size len(cards), O(N)
                         Looping through the cards list of size len(cards), O(N) and pushing to draw pile, O(1)
                         Creation of ArrayStack discard_pile of size len(cards), O(N)
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
            Best Case Complexity: O(N + N2 + NlogN + N), where N is len(self.discard_pile)
            Worst Case Complexity: O(N + N2 + NlogN + N), where N is len(self.discard_pile)
            Explanation: The best and worst case are the same. The first N is the 
            creation of temp_array of size len(self.discard_pile), O(N).
            The N2 is looping through self.discard_pile of size len(self.discard_pile), O(N).
            The complexity of RandomGen.random_shuffle(temp_array), O(NlogN).
            The last N is looping through temp_array of size len(self.discard_pile), O(N).
        """
        RandomGen.random_shuffle(self.discard_pile)
        for i in range(len(self.discard_pile)):
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
            Worst Case Complexity: O()
        """
        if len(self.draw_pile) == 0:
            self.reshuffle()    
        card = self.draw_pile.pop()
        return card
