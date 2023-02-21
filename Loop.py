# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 20:03:06 2023

@author: Jerle
"""
import time
########################### State Machine #################################
def StateMachine(GameDone, Player_Number, PlayerOneDone, PlayerTwoDone, PlayerThreeDone, PlayerFourDone):
    State           = 0
    NextState       = 0
    GameDone        = False
    Player_Number   = 0.0
    PlayerOneDone   = False
    PlayerTwoDone   = False
    PlayerThreeDone = False
    PlayerFourDone  = False
    
    while (State != 6):
        if State == 0:                              # Idle
        
            NextState = 1
            
        elif State == 1:                            # Set number of players
        
            print('How many players?')
            Player_Number = input('Number of Players = ')
            Player_Number = int(Player_Number)
            NextState = 2
            
        elif State == 2:                            # Player 1 turn
    
            
            print('Player 1 turn')    
            if Player_Number > 2:
                if PlayerOneDone == True:    
                    NextState = 3
            else:
                if PlayerOneDone == True:
                    NextState = 2
                    
        elif State == 3:                            # Player 2 turn
            
            print('Player 2 turn')
            if Player_Number > 3:
                if PlayerTwoDone == True:    
                    NextState = 4
            else:
                if PlayerTwoDone == True:
                    NextState = 2
                
        elif State == 4:                            # Player 3 turn
    
            
            print('Player 3 turn')        
            if Player_Number > 4:
                if PlayerThreeDone == True:    
                    NextState = 5
            else:
                if PlayerThreeDone == True:
                    NextState = 2
                    
        elif State == 5:                            # Player 4 turn
    
            
            print('Player 4 turn')    
            if PlayerFourDone == True:    
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

