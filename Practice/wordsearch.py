import string
import random

filler = ' '
wordList = ["COMPUTER", "PROGRAM", "PYTHON", "TEST", "RECURSION", "ITERATIVE"]
puzzle = [[filler for i in range(20)] for j in range(20)]
directions = [[0, -1], [0, 1], [-1, 0], [0, -1], [-1, -1], [1, 1], [-1, 1], [1, -1]]

def printArr(arr):
    for row in arr:
        for item in row:
            print(item, end = ' ')
        print('')
    print('\n')
            
def checkDirection(x, y, dx, dy, word):
    for i, val in enumerate(word):
        try:
            ty = y + (i * dy)
            tx = x + (i * dx)
            temp = puzzle[ty][tx]
            if temp != val and temp != filler:
                return False
            if tx == -1 or ty == -1:
                return False
        except IndexError:
            return False
    return True

def placeWord(word, rows, columns, iteration):
    if iteration > 30:
        return
    x = random.randint(0, rows)
    y = random.randint(0, columns)

    choice = random.choice(directions)
    dx = choice[0]
    dy = choice[1]

    if(checkDirection(x, y, dx, dy, word)):
        for i, val in enumerate(word):
            puzzle[y + (i * dy)][x + (i * dx)] = val
    else:
        placeWord(word, rows, columns, iteration + 1)
    
def makeKey(rows, columns):
    puzzle = [[filler for i in range(rows)] for j in range(columns)]
    for word in wordList:
        placeWord(word, rows, columns, 0)

makeKey(20, 20)

def makePuzzle(key):
    finishedPuzzle = [[filler for i in range(len(key))] for j in range(len(key[0]))]
    for y, row in enumerate(key):
        for x, val in enumerate(row):
            if key[y][x] == filler:
                finishedPuzzle[y][x] = random.choice(string.ascii_uppercase)
            else:
                finishedPuzzle[y][x] = val
    return finishedPuzzle

finishedPuzzle = makePuzzle(puzzle)

def findWord(x, y, word, puz):
    if puz[y][x] != word[0]:
        return [-1]

    for direction in directions:
        dx = direction[0]
        dy = direction[1]

        for i, val in enumerate(word[1:], 1):
            try:
                temp = puz[y + (i * dy)][x + (i * dx)]
                if temp != val:
                    break
                elif i == len(word) - 1:
                    return [x, y, dx, dy]
            except IndexError:
                break
    return [-1]

def fillSol(x, y, dx, dy, word, sol):
    for i, val in enumerate(word):
        sol[y + (i * dy)][x + (i * dx)] = val
    return sol


def solve(puz, wordList):
    sol = [[filler for i in range(len(puz))] for j in range(len(puz[0]))]
    pos: int

    for word in wordList:
        for y, row in enumerate(puz):
            for x, val in enumerate(row):
                pos = findWord(x, y, word, puz)
                if(pos[0] != -1):
                    sol = fillSol(pos[0], pos[1], pos[2], pos[3], word, sol)
    return sol

solution = solve(finishedPuzzle, wordList)

print("Miro's Python Wordsearch Program")
print("Finished Puzzle")
printArr(finishedPuzzle)
print("Key")
printArr(puzzle)
print("Solved Puzzle")
printArr(solution)