# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 20:33:07 2023

@author: Jerle
"""

import time
from Objects import player

# Print function
def print_prompt():
    print('What would you like to do?')
    print('')
    print('Buy a car?        (Press 1)')
    print('Sell your car?    (Press 2)')
    print('Buy a house?      (Press 3)')
    print('Sell your house?  (Press 4)')
    print('Have a child?     (Press 5)')
    print('Get a job?        (Press 6)')
    print('Quit your job?    (Press 7)')
    print('End Turn?         (Press 8)')

########################### State Machine #################################
def StateMachine(PlayerOne, PlayerTwo, PlayerThree, PlayerFour):
    State           = 0
    NextState       = 0
    GameDone        = False
    Player_Number   = 0.0
    action          = 0
    
    while (State != 6):
        
        if State == 0:                              # Idle
            NextState = 1
            
            
        elif State == 1:                            # Set number of players
            print('How many players?')
            Player_Number = input('How many players (1-4)?')
            Player_Number = int(Player_Number)
            NextState = 2
            
            
        elif State == 2:                            # Player 1 turn
            PlayerOne.EndTurn = False
            PlayerTwo.EndTurn = False
            PlayerThree.EndTurn = False
            PlayerFour.EndTurn = False
            print('Player 1 turn') 
            print('')
            print_prompt()
            action = input()
            if Player_Number > 2:
                if PlayerOne.EndTurn == True:    
                    NextState = 3
            else:
                if PlayerOne.EndTurn == True:
                    NextState = 2
                    
                    
        elif State == 3:                            # Player 2 turn
            print('Player 2 turn')
            if Player_Number > 3:
                if PlayerTwo.EndTurn == True:    
                    NextState = 4
            else:
                if PlayerTwo.EndTurn == True:
                    NextState = 2
                
                
        elif State == 4:                            # Player 3 turn
            print('Player 3 turn')        
            if Player_Number > 4:
                if PlayerThree.EndTurn == True:    
                    NextState = 5
            else:
                if PlayerThree.EndTurn == True:
                    NextState = 2
                   
                    
        elif State == 5:                            # Player 4 turn
            print('Player 4 turn')    
            if PlayerFour.EndTurn == True:    
                NextState = 2
        
        elif State == 6:                            # Game finished state
            print('Game Over!')
            
            
        else:
            print('ERROR')
            
        if GameDone == True:                        # Check if game is finished
            NextState = 6
        #GameDone = input('Is the Game Done?') 
        State = NextState                           # Go to next state
        time.sleep(1)                               # Slow down loop
