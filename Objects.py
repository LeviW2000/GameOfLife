# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 21:02:16 2023

@author: Jerle
"""

class player:
    def __init__(self, name, player, age, gender, money, retirement, car1, bEndTurn):
        self.name = 'name'
        self.player = 0
        self.age = 16
        self.gender = 0;
        self.money = 0
        self.retirement = 0
        self.car1 = car(0,0,0,0)
        self.house = house(0,0,0,0)
        self.bEndTurn = False
        
    def buy_car(self):
        
        car_type = 0
        print('What kind of car would you like to buy?')
        print('')
        print('Enter 0 for old and used ($3000)')
        print('Enter 1 for new used ($10000)')
        print('Enter 2 for new ($30000)')
        car_type = input()
        car_type = int(car_type)
        self.car1.car_type = car_type
        car_cost = 0
        if car_type == 0:
            car_cost = 3000
        elif car_type == 1:
            car_cost = 10000
        elif car_type == 2:
            car_cost = 30000
        if self.money > car_cost:
            self.money = self.money - car_cost
            if car_type == 2:   # Devaule car if it is brand new
                self.car1.rvalue = car_cost - 5000
            else:
                self.car1.rvalue = car_cost
            self.car1.irepairs = 0;
            self.car1.brunning = True
            print('You have purchased car type', car_type)
            self.car1.car_exists = True
        else:
            print('You do not have enough to purchace this vehicle.')
    def sell_car(self):
        select = 'n'
        if self.car1.car_exists == True:
            self.car1.car_exists = False
            self.car1.irepairs = 0
            self.car1.brunning = False
            self.car1.car_type = -1
            print('Your vehicle has a value of $', self.car1.rvalue,)
            print('Would you still like to sell your car? (y/n)')
            select = input()
            if select == 'y':
                self.money = self.money + self.car1.rvalue
                print('You have sold your vehicle for $', self.car1.rvalue)
                self.car1.rvalue = 0.0
            else:
                print('You have chosen not to sell your car.')
        else:
            print('You do not have a car to sell!')
    def fix_car(self):
        fixes = 0
        select = 'n'
        print('Your vehicle has', self.car1.irepairs, 'needed.')
        print('Your vehicle requires less than 5 repairs to run.')
        print('How many repairs would you like to do?')
        fixes = input()
        fixes = int(fixes)
        print('Total repair cost =', fixes*100)
        print('Pay for repairs? (y/n)')
        select = input()
        if select == 'y':
            self.car1.irepairs = self.car1.irepairs - fixes
            self.money = self.money - (fixes * 100)
            print('You have repaired your vehicle.')
            print('Your vehicle now has', self.car1.irepairs, 'needed.')
        else:
            print('You have chosen not to repair your vehicle!')
        if self.car1.irepairs <=5 :
            self.car1.brunning = True
    def buy_house(self):
        
        house_type = 0
        print('What kind of home would you like to buy?')
        print('If you are renting you will need to pay a years rent now.')
        print('If you choose to purchae a home you will need to pay the down payment now and every year for the next 30 years you will need to pay a years morgage.')
        print('')
        print('Enter 0 for to rent cheap ($6000/year, $500/month)')
        print('Enter 1 for rent expensive ($18000/year, $1500/month)')
        print('Enter 2 buy Level 1 home ($300,000, $60,000 down, xxx.xx/month)')
        print('Enter 3 buy Level 2 home ($500,000, $100,000 down, xxx.xx/month)')
        print('Enter 4 buy Level 3 home ($700,000, $140,000 down, xxx.xx/month)')
        
        house_type = input()
        house_type = int(house_type)
        self.house.home_type = house_type
        house_cost = 0
        if house_type == 0:
            house_cost = 6000
            self.house.cost_per_year = 6000
        elif house_type == 1:
            house_cost = 18000
            self.house.cost_per_year = 18000
        elif house_type == 2:
            house_cost = 140000
            self.house.cost_per_year = 18000
        elif house_type == 3:
            house_cost = 100000
            self.house.cost_per_year = 20000
        elif house_type == 4:
            house_cost = 140000
            self.house.cost_per_year = 25000
        if self.money > house_cost:
            self.money = self.money - house_cost
            self.house.rvalue = house_cost
            self.house.irepairs = 0;
            self.house.livable = True
            print('You have purchased home type', house_type)
            self.house.home_exists = True
        else:
            print('You do not have enough to purchace this home.')
        
        

        
        
    def have_child():
        pass
    def get_job():
        pass
    def view_acount(self):
        print('Current savings = ', self.money)
        print('Vehilce assets = ', self.car1.rvalue)
        print('     Vehilce running status = ', self.car1.brunning)
        print('     Vehilce repairs needed = ', self.car1.irepairs)
        print('Realistate value =', self.house.rvalue)
        print('     Home livable status =', self.house.blivable)
        print('     Home repairs needed =', self.house.irepairs)
        print('Age = ', self.age)
    def quit_job():
        pass
    def finish_turn(self):
        self.bEndTurn = True

class house:
    def __init__(self, irepairs, rvalue, brunning, car_type):
        self.irepairs = 0
        self.rvalue = 0.0
        self.cost_per_year = 0.0
        self.blivable = False
        self.home_exists = False
        self.home_type = -1
class car:
    def __init__(self, irepairs, rvalue, brunning, car_type):
        self.irepairs = 0
        self.rvalue = 0.0
        self.brunning = False
        self.car_exists = False
        self.car_type = -1
class child:
    pass


