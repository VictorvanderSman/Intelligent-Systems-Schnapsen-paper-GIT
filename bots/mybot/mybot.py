"""
RandomBot -- A simple strategy: enumerates all legal moves, and picks one
uniformly at random.
"""

# Import the API objects
from api import State
from api import Deck

import random


class Bot:

    def __init__(self):
        pass

    def get_move(self, state):
        # type: (State) -> tuple[int, int]
        """
        Function that gets called every turn. This is where to implement the strategies.
        Be sure to make a legal move. Illegal moves, like giving an index of a card you
        don't own or proposing an illegal mariage, will lose you the game.
       	TODO: add some more explanation
        :param State state: An object representing the gamestate. This includes a link to
            the states of all the cards, the trick and the points.
        :return: A tuple of integers or a tuple of an integer and None,
            indicating a move; the first indicates the card played in the trick, the second a
            potential spouse.
        """

        # All legal moves
        moves = state.moves()
        # starting with a random move
        chosen_move = random.choice(moves)
		# List of all legal moves, not being of a trump suit
        not_trump_suit = []
        # Which player this bot is
        player = state.whose_turn()
        leader = state.leader
        
        # If a mariage or jack exchange is possible, play it
        for index, move in enumerate(moves):
            if move[1] != None:
                return move
        
        # Get all not trump suit moves 
        for index, move in enumerate(moves):
            if move[0] is not None and Deck.get_suit(move[0]) != state.get_trump_suit():
                not_trump_suit.append(move)
    
        # starting with a random move
        if len(not_trump_suit) > 0:
            chosen_move = random.choice(not_trump_suit)
        
        # play the highest not trump cards first 
        if len(not_trump_suit) > 0 and player == leader and not_trump_suit != []:
            for index, move in enumerate(not_trump_suit):
                if move[0] is not None and move[0] % 5 <= chosen_move % 5:
                    chosen_move = move
                    return chosen_move
        
        # if player != leader:
        #     played_card = state.get_opponents_played_card()
        #     suit_of_card = Deck.get_suit(played_card)
        #     for index, move in enumerate(moves):
        #         if move[0] is not None and Deck.get_suit(move[0])
                
        
        
        return chosen_move