"""
Tic Tac Toe Player
"""

import math
import copy
from collections import deque
X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    x_count=0;
    o_count=0;
    for x in board:
        for y in x:
            if y==X:
                x_count+=1;
            elif y==O:
                o_count+=1;
    if x_count>o_count:
        return O;
    return X;


def actions(board):
   valid_moves=set()
   for i in range(0,len(board),1):
       for j in range(0,len(board[i]),1):
           if board[i][j]==None:
               valid_moves.add((i,j))
   return valid_moves;


def result(board, action):
    x=action[0]
    y=action[1]
    if board[x][y] != EMPTY:
        raise Exception
    new_board=copy.deepcopy(board)
    new_board[x][y]=player(new_board)
    return new_board


def winner(board):
   counts=[0,0,0]
   maindiagonal_type=board[0][0]
   maindiagonal_count=0
   antidiagonal_type=board[0][2]
   antidiagonal_count=0
   type=[board[0][0],board[0][1],board[0][2]]
   for i in range(0,len(type),1):
       if type[i] is EMPTY:
           counts[i]=-1
   for i in range(0,len(board),1):
       O_count=0
       X_count=0
       for j in range(0,len(board[i]),1):
           if board[i][j]==type[j] and counts[j]!=-1:
               counts[j]+=1
           if board[i][j]==X and O_count==0:
               X_count+=1;
           elif board[i][j]==O and X_count==0:
               O_count+=1
           if maindiagonal_type!=EMPTY and maindiagonal_type==board[i][j] and i==j:
               maindiagonal_count+=1;
           if antidiagonal_type!=EMPTY and antidiagonal_type==board[i][j] and ((i==0 and j==2) or (i==1 and j==1) or (i==2 and j==0)):
               antidiagonal_count+=1;
       if O_count==3:
           return O;
       elif X_count==3:
           return X;
   if(maindiagonal_count==3):
       return maindiagonal_type;
   elif antidiagonal_count==3:
       return antidiagonal_type
   for i in range(0,len(counts),1):
       if(counts[i]==3):
           return type[i]
   return None


def terminal(board):
    terminate_status=winner(board)
    if terminate_status!=None:
        return True
    for x in board:
        for y in x:
            if y==EMPTY:
                return False
    return True


def utility(board):
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0



def minimax(board):
    if terminal(board):
        return None

    empty_board = True
    for x in board:
        for y in x:
            if y != EMPTY:
                empty_board = False
                break
    if empty_board:
        return (1, 1)
    
    detect_movecount = 0
    for x in board:
        for y in x:
            if y != EMPTY:
                detect_movecount += 1
    if detect_movecount == 1:
        if board[1][1] == EMPTY:
            return (1, 1)
        else:
            return (0, 0)

    wanttowin = player(board)

    def max_value(board):
        if terminal(board):
            ret_status = utility(board)
            if ret_status == 0:
                return 0
            elif (ret_status == 1 and wanttowin == X) or (ret_status == -1 and wanttowin == O):
                return 1
            else:
                return -1
        MAX = -2
        for x in list(actions(board)):
            MAX = max(MAX, min_value(result(board, x)))
        return MAX

    def min_value(board):
        if terminal(board):
            ret_status = utility(board)
            if ret_status == 0:
                return 0
            elif (ret_status == 1 and wanttowin == X) or (ret_status == -1 and wanttowin == O):
                return 1
            else:
                return -1
        MIN = 2
        for x in list(actions(board)):
            MIN = min(MIN, max_value(result(board, x)))
        return MIN

    best_move = None
    best_score = -2

    for action in list(actions(board)):
        score = min_value(result(board, action))
        if score > best_score:
            best_score = score
            best_move = action

    return best_move