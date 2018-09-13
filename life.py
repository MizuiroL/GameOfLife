# coding=utf-8
import random
import sys
import time


# Decide casualmente se la cella e' viva o morta
# Modificare la variabile factor per variare la possibilità
def random_number():
    factor = 0.03
    random_number = random.random()
    if random_number >= factor:
        return 0
    else:
        return 1


# Restituisce una matrice morta delle dimensioni date
def dead_board(width, height):
    return [[0 for x in xrange(width)] for y in xrange(height)]


# Restituisce una matrice delle dimensioni date con stati delle celle casuali
def random_board(width, height):
    board = dead_board(width, height)
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[0]):
            board[i][j] = random_number()
            j = j + 1
        i = i + 1
    return board


# Data una cella restituisce la list delle celle vicine
def nearby(board, x, y):
    near = []
    tr = x == 0  # Top row
    br = x == len(board) - 1  # Bottom row
    lc = y == 0  # Left column
    rc = y == len(board[0]) - 1  # Right column
    if not tr:
        near.append([board[x - 1][y], x - 1, y])
    if not br:
        near.append([board[x + 1][y], x + 1, y])
    if not lc:
        near.append([board[x][y - 1], x, y - 1])
    if not rc:
        near.append([board[x][y + 1], x, y + 1])
    if not tr and not lc:
        near.append([board[x - 1][y - 1], x - 1, y - 1])
    if not tr and not rc:
        near.append([board[x - 1][y + 1], x - 1, y + 1])
    if not br and not lc:
        near.append([board[x + 1][y - 1], x + 1, y - 1])
    if not br and not rc:
        near.append([board[x + 1][y + 1], x + 1, y + 1])
    return near


def count(near):
    c = 0
    i = 0
    while i < len(near):
        if near[i][0] == 1:
            c = c + 1
        i = i + 1
    return c


def update_board(old_board, width, height):
    new_board = dead_board(width, height)
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[0]):
            near = nearby(old_board, i, j)
            live_count = count(near)
            if board[i][j] == 0 and live_count == 3:
                new_board[i][j] = 1
            if board[i][j] == 1:
                if live_count < 2 or live_count > 3:
                    new_board[i][j] = 0
                else:
                    new_board[i][j] = 1
            j = j + 1
        i = i + 1
    return new_board


def character(n):
    if n > 0:
        return '@'
    else:
        return ' '


def render(board):
    str = ''
    i = 0
    while i < len(board):
        j = 0
        while j < len(board[0]):
            str = str + character(board[i][j])
            j = j + 1
        i = i + 1
        str = str + '\n'
    sys.stdout.write(str)

w = 250
h = 100
board = random_board(w, h)
print board
render(board)
board = update_board(board, w, h)
print board
render(board)
while True:
    board = update_board(board, w, h)
    time.sleep(0.05)
    render(board)
