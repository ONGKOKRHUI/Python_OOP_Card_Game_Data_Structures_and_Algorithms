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
        self.players: CircularQueue | None = None
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
        self.players = CircularQueue[Player](len(players))
        for i in range(len(players)):
            player = players[i]
            self.players.append(player)
        
        self.game_board = GameBoard(self.generate_cards())
        for _ in range(Config.NUM_CARDS_AT_INIT):
            for _ in range(len(self.players)):
                player = self.players.serve()
                card = self.game_board.draw_card()
                print(f"{player.name} drew {card}")
                player.add_card(card)
                self.players.append(player)
        
        while True:
            card = self.game_board.draw_card()
            self.game_board.discard_card(card)
            print(f"First card drawn {card}")
            if card.label <= CardLabel.NINE:
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
        next_player = self.players.peek()
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
        temp_array = ArrayStack[Player](len(self.players))
        for _ in range(len(self.players)):
            player = self.players.serve()
            temp_array.push(player)
        for _ in range(len(temp_array)):
            self.players.append(temp_array.pop())
            

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
        skipped_player = self.players.serve()
        self.players.append(skipped_player)
        

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
        next_player = self.players.serve()
        for _ in range(2):
            self.draw_card(next_player, False)
        self.players.append(next_player)
        

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
            next_player = self.players.serve()
            for _ in range (4):
                self.draw_card(next_player, False)
            self.players.append(next_player)


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
        if playing and (card.color == self.current_color or card.color == CardColor.BLACK or card.label == self.current_label):
            return 1, card 
        else:
            player.add_card(card)
            #return None
            return None, card

    def play_game(self) -> Player:
        """
        Method to play the game

        Args:
            None

        Returns:
            Player: The winner of the game
        """
        while True:
            self.current_player = self.players.serve()
            print(f"{self.current_player.name}, {self.current_player.cards_in_hand()}'s turn")
            card = self.current_player.play_card(self.current_color, self.current_label)
            print(f"{self.current_player.name}, {self.current_player.cards_in_hand()} played {card}, if None means no playable cards in hand")
            if self.current_player.cards_in_hand() == 0:
                print(f"{self.current_player.name}, {self.current_player.cards_in_hand()} wins")
                return self.current_player
            if card is not None:
                play_card = True
            else:
                playable, card = self.draw_card(self.current_player, True)
                print(f"{self.current_player.name}, {self.current_player.cards_in_hand()} has no playable card, and drew {card}")
                #if card is not None:
                if playable is not None:
                    play_card = True
                    print(f"{self.current_player.name}, {self.current_player.cards_in_hand()} drew one card {card} which is playable")
                    self.game_board.discard_card(card)
                    print(card)
                    self.current_color = card.color
                    self.current_label = card.label
                    print(self.current_color)
                    print(self.current_label)
                    print(f"{self.current_player.name}, {self.current_player.cards_in_hand()} played {card}")
                else:
                    print(f"{self.current_player.name}, {self.current_player.cards_in_hand()} drew one card {card} which is not playable (None)")
                    play_card = False
                    self.players.append(self.current_player)
            if play_card == True:
                print(f"{self.current_player.name}, {self.current_player.cards_in_hand()} played {card}")
                self.game_board.discard_card(card)
                self.current_label = card.label
                self.current_color = card.color
                if card.color == CardColor.BLACK:
                    self.players.append(self.current_player)
                    print("black is played")
                    self.play_black(card)
                elif card.label == CardLabel.DRAW_TWO:
                    self.players.append(self.current_player)
                    print("draw two is played")
                    self.play_draw_two()
                elif card.label == CardLabel.SKIP:
                    self.players.append(self.current_player)
                    print("skip is played")
                    self.skip_next_player()
                elif card.label == CardLabel.REVERSE:
                    print("reverse is played")
                    self.reverse_players()
                    self.players.append(self.current_player)
                else:
                    print("normal card is played")
                    self.players.append(self.current_player)
