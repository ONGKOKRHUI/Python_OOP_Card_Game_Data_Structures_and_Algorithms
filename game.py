from __future__ import annotations
from player import Player
from game_board import GameBoard
from card import CardColor, CardLabel, Card
from random_gen import RandomGen
from config import Config
from data_structures import *


class Game:
    """
    Game class to play the game
    """

    def __init__(self) -> None:
        """
        Constructor for the Game class

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.players: ArrayList[Player] | None = None
        self.current_player: Player | None = None
        self.current_color: CardColor | None = None
        self.current_label: CardLabel | None = None
        self.game_board: GameBoard | None = None

    def generate_cards(self) -> ArrayList[Card]:
        """
        Method to generate the cards for the game

        Args:
            None

        Returns:
            ArrayList[Card]: The list of Card objects generated
        """
        list_of_cards: ArrayList[Card] = ArrayList(Config.DECK_SIZE)
        idx: int = 0

        # Generate 4 sets of cards from 0 to 9 for each color
        for color in CardColor:
            if color != CardColor.BLACK:
                # Generate 4 sets of cards from 0 to 9 for each color
                for i in range(10):
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel(i)))
                    idx += 1

                # Generate 2 of each special card for each color
                for i in range(2):
                    list_of_cards.insert(idx, Card(color, CardLabel.SKIP))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.REVERSE))
                    idx += 1
                    list_of_cards.insert(idx, Card(color, CardLabel.DRAW_TWO))
                    idx += 1
            else:
                # Generate black crazy and draw 4 cards
                for i in range(4):
                    list_of_cards.insert(idx, Card(CardColor.BLACK, CardLabel.CRAZY))
                    idx += 1
                    list_of_cards.insert(
                        idx, Card(CardColor.BLACK, CardLabel.DRAW_FOUR)
                    )
                    idx += 1

                # Randomly shuffle the cards
                RandomGen.random_shuffle(list_of_cards)

                return list_of_cards

    def initialise_game(self, players: ArrayList[Player]) -> None:
        """
        Method to initialise the game

        Args:
            players (ArrayList[Player]): The list of players

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.players = players
        self.game_board = GameBoard(self.generate_cards())
        for player in self.players:
            while player.cards_in_hand() < Config.NUM_CARDS_AT_INIT:
                card = self.game_board.draw_card()
                player.add_card(card)
        while True:
            card = self.game_board.draw_card()
            self.game_board.discard_card(card)
            if card.label < 10:
                self.current_color = card.color
                self.current_label = card.label
                break

    def next_player(self) -> Player:
        """
        Method to get the next player

        Args:
            None

        Returns:
            Player: The next player

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        if self.current_player is None:
            next_player = self.players.__getitem__(0)
        else:
            next_player_index = (self.players.index(self.current_player) + 1) % len(self.players)
            next_player = self.players.__getitem__(next_player_index)
        return next_player

    def reverse_players(self) -> None:
        """
        Method to reverse the order of the players

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        reversed_players: ArrayList[Player] = ArrayList()
        for i in range(len(self.players)):
            reversed_players.insert(0, self.players.__getitem__(i))
        self.players = reversed_players

    def skip_next_player(self) -> None:
        """
        Method to skip the next player in the game

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.current_player = self.next_player()

    def play_draw_two(self) -> None:
        """
        Method to play a draw two card

        Args:
            None

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        next_player = self.next_player()
        for _ in range(2):
            card = self.draw_card(next_player, False)
            next_player.add_card(card)
        self.skip_next_player()

    def play_black(self, card: Card) -> None:
        """
        Method to play a crazy card

        Args:
            card (Card): The card to be played

        Returns:
            None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        self.current_color = CardColor(RandomGen.randint(0,3))
        if card.label == CardLabel.DRAW_FOUR:
            for _ in range (2):
                self.play_draw_two()
            for _ in range (len(self.players)-1):
                self.skip_next_player()
        else:
            self.skip_next_player()


    def draw_card(self, player: Player, playing: bool) -> Card | None:
        """
        Method to draw a card from the deck

        Args:
            player (Player): The player who is drawing the card
            playing (bool): A boolean indicating if the player is able to play the card

        Returns:
            Card - When drawing a playable card, other return None

        Complexity:
            Best Case Complexity:
            Worst Case Complexity:
        """
        card = self.game_board.draw_card()
        if playing and (card.color == self.current_color or card.label == self.current_label):
            self.game_board.discard_card(card)
            return card 
        else:
            player.add_card(card)
            return None

    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game
        """
        pass
