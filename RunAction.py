# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:14:48 2023

@author: Jerle
"""

def RunAction(action, player):
    if action == 1:
        player.buy_car()
    elif action == 2:
        pass # sell car
    elif action == 3:
        player.buy_house()
    elif action == 4:
        pass # sell house
    elif action == 5:
        player.have_child()
    elif action == 6:
        player.get_job()
    elif action == 7:
        player.quit_job()
    elif action == 8:
        pass
    elif action == 9:
        player.finish_turn()