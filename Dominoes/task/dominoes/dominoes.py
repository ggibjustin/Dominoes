# # Write your code here
import random

pieces = [[2, 6], [3, 4], [5, 6], [0, 5], [1, 2], [4, 6], [2, 3], [0, 6], [0, 0], [6, 6], [2, 4], [2, 2], [0, 1], [3, 3], [0, 2], [3, 6], [4, 4], [3, 5], [1, 5], [0, 3], [2, 5], [1, 3], [1, 4], [4, 5], [1, 6], [1, 1], [0, 4], [5, 5]]
random.shuffle(pieces)
stock_pieces = random.sample(pieces, 14)
computer_pieces = random.sample(pieces, 7)
player_pieces = random.sample(pieces, 7)


