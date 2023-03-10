# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:33:07 2023

@author: Jerle
"""

import time
import numpy as np
from RunAction import RunAction
from EndRound import EndRound
from Objects import player

# Print function
def print_prompt():
    print('What would you like to do?')
    print('')
    print('Buy a car?         (Press 1)')
    print('Sell your car?     (Press 2)')
    print('Repair car?        (Press 3)')
    print('Buy a house?       (Press 4)')
    print('Sell your house?   (Press 5)')
    print('Repair your house? (Press 6)')
    print('Have a child?      (Press 7)')
    print('Get a job?         (Press 8)')
    print('Quit your job?     (Press 9)')
    print('View account?      (Press 10)')
    print('End Turn?          (Press 11)')

########################### State Machine #################################
def StateMachine(Players):
    State           = 0
    NextState       = 0
    GameDone        = False
    action          = 0

    while (State != 6):
        
        if State == 0:                              # Idle
            NextState = 1
            
            
        elif State == 1:                            # Set number of players
            print('How many players?')
            print('How many players (1-4)?')
            Player_Number = input()
            Player_Number = int(Player_Number)
            NextState = 2
            
            
        elif State == 2:                            # Player 1 turn
            print('Player 1 turn') 
            print('')
            print_prompt()
            action = input()
            action = int(action)
            RunAction(action, Players[0])
            if Player_Number >= 2:
                if Players[0].bEndTurn == True:    
                    NextState = 3
            else:
                if Players[0].bEndTurn == True:
                    NextState = 7
                    
                    
        elif State == 3:                            # Player 2 turn
            print('Player 2 turn')
            print('')
            print_prompt()
            action = input()
            action = int(action)
            RunAction(action, Players[1])
            if Player_Number >= 3:
                if Players[1].bEndTurn == True:    
                    NextState = 4
            else:
                if Players[1].bEndTurn == True:
                    NextState = 7
                
                
        elif State == 4:                            # Player 3 turn
            print('Player 3 turn') 
            print('')
            print_prompt()
            action = input()
            action = int(action)
            RunAction(action, Players[2])
            if Player_Number >= 4:
                if Players[2].bEndTurn == True:    
                    NextState = 5
            else:
                if Players[2].bEndTurn == True:
                    NextState = 7
                   
                    
        elif State == 5:                            # Player 4 turn
            print('Player 4 turn')    
            print('')
            print_prompt()
            action = input()
            action = int(action)
            RunAction(action, Players[3])
            if Players[3].EndTurn == True:    
                NextState = 7
        
        elif State == 6:                            # Game finished state
            print('Game Over!')
            
        
        elif State == 7:
            EndRound(Players)
            NextState = 2
            
            
        else:
            print('ERROR')
            
        if GameDone == True:                        # Check if game is finished
            NextState = 6
        #GameDone = input('Is the Game Done?') 
        State = NextState                           # Go to next state
        time.sleep(1)                               # Slow down loop
