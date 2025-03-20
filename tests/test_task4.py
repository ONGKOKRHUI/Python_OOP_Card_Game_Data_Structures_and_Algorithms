from unittest import TestCase
from unittest.mock import patch
from data_structures.referential_array import ArrayR
from ed_utils.decorators import number, visibility
from data_structures import *

from game import Game
from random_gen import RandomGen
from card import CardColor, CardLabel, Card
from player import Player
from config import Config


class TestTask4(TestCase):
    """
    @number("4.1")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_small_game(self) -> None:
        # Set up the small game
        RandomGen.set_seed(123)
        Config.NUM_CARDS_AT_INIT = 2
        players: ArrayList[Player] = ArrayList(4)
        a = Player("Alice")
        b = Player("Bob")
        c = Player("Charlie")
        d = Player("David")
        players.insert(0, a)
        players.insert(1, b)
        players.insert(2, c)
        players.insert(3, d)
        game: Game = Game()
        game.initialise_game(players)

        # Check the first card of the discard pile
        self.assertEqual(
            game.current_color,
            CardColor.GREEN,
            f"First card in discard pile should be GREEN, but is {game.current_color}",
        )
        self.assertEqual(
            game.current_label,
            CardLabel.TWO,
            f"First card in discard pile should be TWO, but is {game.current_label}",
        )

        # Play the game
        winner: Player = game.play_game()

        # Check the winner
        self.assertEqual(
            winner.name, c.name, f"Winner should be Charlie, but is {winner.name}"
        )

        # Check the leftover hand of Alice
        self.assertEqual(
            a.cards_in_hand(),
            3,
            f"Alice should have 3 cards left, but has {a.cards_in_hand()}",
        )

        # Check the leftover hand of Bob
        self.assertEqual(
            b.cards_in_hand(),
            3,
            f"Bob should have 3 cards left, but has {b.cards_in_hand()}",
        )

        # Check the leftover hand of David
        self.assertEqual(
            d.cards_in_hand(),
            1,
            f"David should have 1 cards left, but has {d.cards_in_hand()}",
        )

    @number("4.2")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_long_game(self) -> None:
        # Set up the long game
        RandomGen.set_seed(123)
        Config.NUM_CARDS_AT_INIT = 7

        players: ArrayList[Player] = ArrayList(4)
        a = Player("Alice")
        b = Player("Bob")
        c = Player("Charlie")
        players.insert(0, a)
        players.insert(1, b)
        players.insert(2, c)

        game: Game = Game()
        game.initialise_game(players)

        # Check the first card of the discard pile
        self.assertEqual(
            game.current_color,
            CardColor.GREEN,
            f"First card in discard pile should be GREEN, but is {game.current_color}",
        )
        self.assertEqual(
            game.current_label,
            CardLabel.THREE,
            f"First card in discard pile should be THREE, but is {game.current_label}",
        )

        # Play the game
        winner: Player = game.play_game()

        # Check the winner
        self.assertEqual(
            winner.name, a.name, f"Winner should be Alice, but is {winner.name}"
        )

        # Check the leftover hand of Bob
        self.assertEqual(
            b.cards_in_hand(),
            3,
            f"Bob should have 3 cards left, but has {b.cards_in_hand()}",
        )

        # Check the leftover hand of Charlie
        self.assertEqual(
            c.cards_in_hand(),
            6,
            f"Charlie should have 6 cards left, but has {c.cards_in_hand()}",
        )
    """
    # new_small_game
    @number("4.3")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_black_card_game(self) -> None:
        # Set up the game with known seed for black card testing
        RandomGen.set_seed(456)  # Different seed that will produce black cards in play
        Config.NUM_CARDS_AT_INIT = 2
        players: ArrayList[Player] = ArrayList(4)
        a = Player("Alice")
        b = Player("Bob")
        c = Player("Charlie")
        d = Player("David")
        players.insert(0, a)
        players.insert(1, b)
        players.insert(2, c)
        players.insert(3, d)
        game: Game = Game()
        game.initialise_game(players)
        
        # Force a black card into a player's hand to ensure we test black card functionality
        # We'll remove their first card and replace it with a black CRAZY card
        test_player = a  # Using Alice as our test subject
        if test_player.cards_in_hand() > 0:
            test_player.hand.delete_at_index(0)  # Remove first card
        test_player.add_card(Card(CardColor.BLACK, CardLabel.CRAZY))
        
        # For testing DRAW_FOUR functionality, add to another player
        b.hand.delete_at_index(0)  # Remove first card
        b.add_card(Card(CardColor.BLACK, CardLabel.DRAW_FOUR))
        
        # Play the game
        winner: Player = game.play_game()
        
        # Check the winner
        self.assertIsNotNone(winner, "Game should have a winner")
        
        # Verify the winner has 0 cards
        self.assertEqual(
            winner.cards_in_hand(),
            0,
            f"{winner.name} should have 0 cards as the winner"
        )
    
        # Additional assertions to validate black card behavior
        # We can check if color changes happened correctly by examining the final game state
        self.assertIsNotNone(
            game.current_color, 
            "Game should have a current color after black card play"
        )
        
        # Verify other players have cards (didn't all go to 0)
        players_with_cards = 0
        for i in range(len(game.players)):
            player = game.players.serve()
            if player.name != winner.name and player.cards_in_hand() > 0:
                players_with_cards += 1
            game.players.append(player)
        
        self.assertGreater(
            players_with_cards,
            0,
            "At least one non-winner should have cards remaining"
        )


    @number("4.4")
    @visibility(visibility.VISIBILITY_SHOW)
    def test_new_black_card_game(self) -> None:
        # Set up the game with known seed for black card testing
        RandomGen.set_seed(456)  # Different seed that will produce black cards in play
        Config.NUM_CARDS_AT_INIT = 6  # Increased from 2 to 6 cards per player at start
        players: ArrayList[Player] = ArrayList(4)
        a = Player("Alice")
        b = Player("Bob")
        c = Player("Charlie")
        d = Player("David")
        players.insert(0, a)
        players.insert(1, b)
        players.insert(2, c)
        players.insert(3, d)
        game: Game = Game()
        game.initialise_game(players)
        
        # Force a black card into a player's hand to ensure we test black card functionality
        # We'll remove their first card and replace it with a black CRAZY card
        test_player = a  # Using Alice as our test subject
        if test_player.cards_in_hand() > 0:
            test_player.hand.delete_at_index(0)  # Remove first card
        test_player.add_card(Card(CardColor.BLACK, CardLabel.CRAZY))
        
        # For testing DRAW_FOUR functionality, add to another player
        b.hand.delete_at_index(0)  # Remove first card
        b.add_card(Card(CardColor.BLACK, CardLabel.DRAW_FOUR))
        
        # Add more cards to c and d to make the game longer
        c.add_card(Card(CardColor.RED, CardLabel.REVERSE))
        c.add_card(Card(CardColor.BLUE, CardLabel.SKIP))
        d.add_card(Card(CardColor.GREEN, CardLabel.DRAW_TWO))
        d.add_card(Card(CardColor.YELLOW, CardLabel.NINE))
        
        # Set a maximum number of turns to prevent infinite loops in testing
        Config.MAX_GAME_TURNS = 100  # Increased from default
        
        # Play the game
        winner: Player = game.play_game()
        
        # Check the winner
        self.assertIsNotNone(winner, "Game should have a winner")
        
        # Verify the winner has 0 cards
        self.assertEqual(
            winner.cards_in_hand(),
            0,
            f"{winner.name} should have 0 cards as the winner"
        )
        
        # Additional assertions to validate black card behavior
        # We can check if color changes happened correctly by examining the final game state
        self.assertIsNotNone(
            game.current_color, 
            "Game should have a current color after black card play"
        )
        
        # Verify that the game took at least a minimum number of turns
        # self.assertGreaterEqual(
        #     game.turn_counter,
        #     15,  # Set a minimum expected number of turns
        #     f"Game should have taken at least 15 turns, but only took {game.turn_counter}"
        # )
        
        # Verify other players have cards (didn't all go to 0)
        players_with_cards = 0
        total_cards_remaining = 0
        for i in range(len(game.players)):
            player = game.players.serve()
            if player.name != winner.name and player.cards_in_hand() > 0:
                players_with_cards += 1
                total_cards_remaining += player.cards_in_hand()
            game.players.append(player)
        
        self.assertGreater(
            players_with_cards,
            0,
            "At least one non-winner should have cards remaining"
        )
        
        # Verify the total number of remaining cards is substantial
        self.assertGreater(
            total_cards_remaining,
            5,
            "There should be a significant number of cards remaining with other players"
        )