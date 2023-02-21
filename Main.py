# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 21:18:54 2023

@author: Jerle
"""

import Loop.py
################### Jerimae's Game of Life ###########################

# Every player start at 16 years old to a middle class family in America. The
# goal is to reach retirement the fastest.

import Loop.py
import Objects.py

# Sample of taking a turn

player1 = Objects.player('Jerimae',0,16,1,5000,0,0)
player1.age = 16
player1.gender = 1
player1.money = 5000

print('What would you like to do?')
print('')
print('buy a car =    1')
print('buy a house =  2')
print('have a child = 3')
print('Pass =         4')
print('')
print('Checking = ', player1.money)




























