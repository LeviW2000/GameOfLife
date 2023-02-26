# -*- coding: utf-8 -*-
"""
Created on Tue Feb 21 21:14:48 2023

@author: Jerle
"""

def RunAction(action, player):
    if action == 1: # buy car
        player.buy_car()
    elif action == 2: # sell car
        player.sell_car()
    elif action == 3:
        player.fix_car()
    elif action == 4: # buy house
        player.buy_house()
    elif action == 5: # sell house
        pass
    elif action == 6:
        pass
    elif action == 7:
        player.have_child()
    elif action == 8:
        player.get_job()
    elif action == 9:
        player.quit_job()
    elif action == 10:
        player.view_acount()
    elif action == 11:
        player.finish_turn()
    elif action == 100: # end game
        pass