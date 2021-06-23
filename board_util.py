import random
import string

def generateBoardFromString(rows, columns, string):
    if rows != columns or len(string) != columns ** 2:
        raise Exception("Invalid string length")

    board = []

    for i in range(len(string)):
        if i % columns == 0: 
            substring = string[i : i + columns] 
            list = [] 
            for j in substring: 
                list.append(j)
            board.append(list)
    return board

def generateRandomBoard(rows, cols):
    letters = string.ascii_lowercase
    boardString = ''.join(random.choice(letters) for i in range(rows * cols))
    return generateBoardFromString(rows, cols, boardString)

def _isInBounds(board, row, col):
    return (row >= 0 and row < len(board)) and \
        (col >= 0 and col < len(board[row]))

directions = [
    [-1, 0], # north
    [-1, 1], # north-east
    [0, 1], # east
    [1, 1],  # south-east
    [1, 0], # south
    [1, -1], # south-west
    [0, -1], # west
    [-1, -1] # north-west
]

def _solve(board, dictionary, letterRow, letterCol, visited, string, stringsFound):
    found = set()

    string += board[letterRow][letterCol]
    visitedLetters = []
    visitedLetters.extend(visited)
    visitedLetters.append([letterRow, letterCol])
    if (not dictionary.isStartOfExistingWord(string)):
        return found

    for k, l in directions:
        nextLetterRow = letterRow + k
        nextLetterCol = letterCol + l
        if (_isInBounds(board, nextLetterRow, nextLetterCol) and \
                [nextLetterRow, nextLetterCol] not in visited):
            found.update(_solve(board, dictionary, nextLetterRow, nextLetterCol, visitedLetters, string, found))
    if (dictionary.isWord(string) and len(string) > 3):
        found.add(string)
    return found

def solveBoard(board, dictionary):
    wordsFound = set()

    for x in range(len(board)):
        for y in range(len(board[x])):
            wordsFound.update(_solve(board, dictionary, x, y, [], "", set()))
    return wordsFound