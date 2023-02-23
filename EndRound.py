# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:57:59 2023

@author: Jerle
"""

def EndRound(Player1, Player2, Player3, Player4):
    
    # Reset end turns
    Player1.bEndTurn = False
    Player2.bEndTurn = False
    Player3.bEndTurn = False
    Player4.bEndTurn = False
    
    # Increment age
    Player1.age = Player1.age + 1
    Player2.age = Player2.age + 1
    Player3.age = Player3.age + 1
    Player4.age = Player4.age + 1
    
    # WILL ADD ALL CAR STUFF INTO FUNCTIONS THAT WILL EVENTUALLY LIVE IN THEIR OWN FILE
    # Devalue cars if owns a car
    if Player1.car1.brunning == True:
        Player1.car1.rvalue = Player1.car1.rvalue * (1-.15) #loses 15 percent a year
    if Player2.car1.brunning == True:
        Player2.car1.rvalue = Player2.car1.rvalue * (1-.15)
    if Player3.car1.brunning == True:
        Player3.car1.rvalue = Player3.car1.rvalue * (1-.15)
    if Player4.car1.brunning == True:
        Player4.car1.rvalue = Player4.car1.rvalue * (1-.15)
    
    # Add car repairs
    
    
    
    
    
    
    
    # Devaule homes if owns a home
    # Add home repairs
    # Increase wage if had a job
    # Increase savings if had a job
    # Increase retirement