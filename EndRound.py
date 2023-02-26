# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 20:57:59 2023

@author: Jerle
"""
import numpy as np

def EndRound(Players):
    
    # Reset end turns
    for i in range(4):
        Players[i].bEndTurn = False
    
    # Increment age
    for i in range(4):
        Players[i].age = Players[i].age + 1
    
    # WILL ADD ALL CAR STUFF INTO FUNCTIONS THAT WILL EVENTUALLY LIVE IN THEIR OWN FILE
    # Devalue cars if owns a car
    for i in range(4):
        if Players[i].car1.brunning == True:
            Players[i].car1.rvalue = Players[i].car1.rvalue * (1-.15) #loses 15 percent a year
    # Add car repairs
    for i in range(4):
        if Players[i].car1.brunning == True:
            # Increment repairs
            if Players[i].car1.car_type == 0:
                Players[i].car1.irepairs = Players[i].car1.irepairs + 3
            elif Players[i].car1.car_type == 1:
                Players[i].car1.irepairs = Players[i].car1.irepairs + 2
            elif Players[i].car1.car_type == 2:
                Players[i].car1.irepairs = Players[i].car1.irepairs + 1
            
            if Players[i].car1.irepairs > 5:
                Players[i].car1.brunning = False
    
    # pay for homes and rent
    for i in range(4):
        if Players[i].house.home_exists == True:
            Players[i].money = Players[i].money - Players[i].house.cost_per_year
            if Players[i].money <= Players[i].house.cost_per_year:
                Players[i].house.blivable = False
                # add condition for being kicked out
    
    
    # Devaule homes if owns a home
    
    # Add home repairs
    for i in range(4):
        if (Players[i].house.blivable == True) & (Players[i].house.home_type > 2):
            pass
    
    # Increase wage if had a job
    # Increase savings if had a job
    # Increase retirement