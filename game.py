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
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Explanation:
            - The best and worst case complexity are constant
            - During the initialization of the game, all the attributes are assigned to None, O(1)
            - Assignment is constant time, O(1)
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
            Best Case Complexity: O(N + N + M + KN) = O(N + M + KN), where N length of players collection, len(players)/len(self.players),
              M is the number of cards from self.generate_cards, K is Config.NUM_CARDS_AT_INIT
            Worst Case Complexity: O(N + N + M + KN + Q) = O(N + M + KN + Q), where N length of players collection, len(players)/len(self.players),
              M is the number of cards from self.generate_cards, K is Config.NUM_CARDS_AT_INIT, Q is the number of cards 
              drawn from the draw pile before a valid card is drawn, which can be at most len(self.gameboard.draw_pile)
            Explanation: 
            For both best and worst case complexity:
            - The CircularQueue is initialialised with the length of players, O(N)
            - The for loop to append players runs N times, where N is the length of players, O(N)
            - The GameBoard is initialised with the cards generated, O(M)
            - Each player is initialised with Config.NUM_CARDS_AT_INIT cards, O(KN)
            The best case complexity happens when in the while loop, the first card drawn is a valid card, O(1)
            The worst case complexity happens when in the while loop, the first valid card is at the 
            very back of the draw pile, which can at most be len(self.gameboard.draw_pile), O(Q)
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
                player.add_card(card)
                self.players.append(player)
        
        while True:
            card = self.game_board.draw_card()
            self.game_board.discard_card(card)
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
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Explanation: 
            - The best and worst case complexity are constant time
            - The peek method only returns the frontmost value in the queue which is O(1)
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
            Best Case Complexity: O(N + N + N) = O(N), where N is the length of self.players
            Worst Case Complexity: O(N + N + N) = O(N), where N is the length of self.players
            Explanation: 
            - The best and worst case are the same
            - A temp_array is initialised with the length of self.players, O(N)
            - The for loop runs N times, where N is the length of self.players, O(N)
            - The second for loop runs N times, where N is the length of temp_array which is equal of self.players, O(N)
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
            Best Case Complexity: O(1)
            Worst Case Complexity: O(1)
            Explanation: The best and worst case complexity are constant
            - The serve method only returns the frontmost value in the queue which is O(1)
            - The append method only appends to the back of the queue which is O(1)
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
            Best Case Complexity: O(1)
            Worst Case Complexity: O(NlogN + M), where N is the length of gameboard.discard_pile and M is the length of player.hand
            Explanation:
            - Since serve and append are both constant time, O(1)
            - the for loop loops for constant time 2 times regardless of input size, O(1)
            - The best case complexity is the same as the best case complexity of self.draw_card, O(1)
            - The worst case complexity is the same as the worst case complexity of self.draw_card as well, O(NlogN + M)
            - The details are in self.draw_card method
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
            Best Case Complexity: O(1)
            Worst Case Complexity: O(NlogN + M), where N is the length of gameboard.discard_pile and M is the length of player.hand
            Explanation:
            - Since assigning the current color using RandomGen.randint is constant time, O(1) 
            - and serve and append are both constant time, O(1)
            - and we assume comparison between CardLabel.DRAW_FOUR and card.label is constant time, O(1)
            - if the card is a draw four card, the for loop runs 4 times regardless of input size, O(1).
            - In best case, the card is not a draw four card, which is constant time, O(1)
            - In the worst case, the card is a draw four card, the worst case complexity is the same as the worst case complexity of self.draw_card, O(NlogN + M)
            - The details are in self.draw_card method
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
            Best Case Complexity: O(1)
            Worst Case Complexity: O(NlogN + M), where N is the length of gameboard.discard_pile
            and M is the the number of cards in player.hand, which is the length of player.hand
            Explanation:
            - The best case complexity happens when draw_card is called and the draw pile is not empty,
            in which case the complexity is O(1). And playing is True and fulfills the condition to play the card, O(1)
            or playing is False which will add the card to the player's hand which is not full and resize is not needed, O(1)
            - The worst case complexity happens when the draw pile is empty, in which case the complexity is O(NlogN) due to 
            reshuffling of discard pile and adding to draw pile and playing is False or the card is not playable. 
            And when add_card is called, player.hand is full and resize is needed, in which case the complexity is O(M), 
            where M is the length of player.hand
            - In this case we assume all comparisons between enum (int) values of CardColor and CardLabel are constant time
        """
        card = self.game_board.draw_card()
        if playing and (card.color == self.current_color or card.color == CardColor.BLACK or card.label == self.current_label):
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
        #round_counter = 1
        while True:
            """# Print debugging information
            self.current_player = self.players.peek()
            print(f"--- Round {round_counter}, {self.current_player.name}'s turn ---")
            print(f"Current Color: {self.current_color}, Current Label: {self.current_label}")
            # Print card counts for all players
            for i in range(len(self.players)):
                player = self.players.serve()
                print(f"{player.name} has {player.cards_in_hand()} cards")
                # Print each card in the player's hand
                for j in range(player.cards_in_hand()):
                    card = player.hand[j]
                    print(f"  - {card.color} {card.label}")
                self.players.append(player)
            round_counter += 1"""
            self.current_player = self.players.serve()
            card = self.current_player.play_card(self.current_color, self.current_label)
            if self.current_player.cards_in_hand() == 0:
                return self.current_player
            if card is not None:
                play_card = True
            else:
                card = self.draw_card(self.current_player, True)
                #if card is not None:
                if card is not None:
                    play_card = True
                    self.game_board.discard_card(card)
                    self.current_color = card.color
                    self.current_label = card.label
                    print(f"Current Color: {self.current_color}, Current Label: {self.current_label}")
                else:
                    play_card = False
                    self.players.append(self.current_player)
            if play_card == True:
                self.game_board.discard_card(card)
                self.current_label = card.label
                self.current_color = card.color
                print(f"Current Color: {self.current_color}, Current Label: {self.current_label}")
                if card.color == CardColor.BLACK:
                    self.players.append(self.current_player)
                    self.play_black(card)
                elif card.label == CardLabel.DRAW_TWO:
                    self.players.append(self.current_player)
                    self.play_draw_two()
                elif card.label == CardLabel.SKIP:
                    self.players.append(self.current_player)
                    self.skip_next_player()
                elif card.label == CardLabel.REVERSE:
                    self.reverse_players()
                    self.players.append(self.current_player)
                else:
                    self.players.append(self.current_player)
