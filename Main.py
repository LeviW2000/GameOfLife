# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:18:54 2023

@author: Jerle
"""


################### Jerimae's Game of Life ###########################

# Every player start at 16 years old to a middle class family in America. The
# goal is to reach retirement the fastest.

#import Loop.py
import numpy as np
from Objects import player
from StateMachine import StateMachine

# Initialize Players
player1 = player('null',0,0,0,0,0,0,0)
player1.age = 16
player1.gender = 1
player1.money = 5000000000
player1.bEndTurn = False

player2 = player('null',0,0,0,0,0,0,0)
player2.age = 16
player2.gender = 1
player2.money = 5000
player2.bEndTurn = False

player3 = player('null',0,0,0,0,0,0,0)
player3.age = 16
player3.gender = 1
player3.money = 5000
player3.bEndTurn = False

player4 = player('null',0,0,0,0,0,0,0)
player4.age = 16
player4.gender = 1
player4.money = 5000
player4.bEndTurn = False

Players = np.array([player1,player2,player3,player4])

print('Welcome to the game of life!')
print('')

StateMachine(Players)



























