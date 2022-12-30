# # Note: You get 5 attempts to guess it right
import random
import os
from theGames.hanginman import HangingMan
from theGames.tictactoe import TicTacToe

hman = HangingMan
ttt = TicTacToe
print('Which game would you like to play? \n 1) Hanging Man \n 2) Tic Tac Toe')
select = int(input())

ttt.main() if select == 2 else hman.main()
