import board_util
from dictionary import Dictionary

import time
millis = time.time()

dictionary = Dictionary('resources/word-list.txt')
board = board_util.generateBoardFromString(7, 7, 'tcpupydtieefaokhnurcwnttnieolskdjmnbomcnxpwoeirhf')
# board = board_util.generateRandomBoard(5,5)
solution = board_util.solveBoard(board, dictionary)
print(sorted(solution))
print(time.time() - millis)



