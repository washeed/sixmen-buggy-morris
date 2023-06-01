from alphabeta6 import MiniMaxPlayer
from math import inf

class MyPlayer(MiniMaxPlayer):

    def maximizes(self):
        return True

    # Return the best value and move for MAX in this game
    def value(self, game, alpha=-inf, beta=+inf, depth=0):
        # Is the game over?
        utility = game.utility()

        if utility is not None:
            return utility, None

        my_moves = game.moves()
        print('Valid moves')
        print(game.moves())
        while True:
            try:
                index = int(input('Pick the index of your move: '))
                if index < 0 or index > len(game.moves()) - 1:
                    print('Please enter a valid index')
                else: 
                    break
            except ValueError:
                print("Invalid input. Please enter a valid index.")

        my_move = my_moves[index]
        print('Selected move: ')
        print(my_move)

        child = game.child(my_move, self)
        # value = self.opponent.value(child, alpha, beta, depth + 1)[0]
        value = -inf
        return value, my_move
