"""

Monte Carlo Simulation: Create a function named monte_hall that takes an argument
indicating the number of times to iterate a monte-carlo simulation of the Monte Hall problem with 4 doors and 1 prize
(https://en.wikipedia.org/wiki/Monty_Hall_problem).

For simplicity, you can assume that the game player always initially chooses door A 
and the host will open one door. The prize may be behind any of the 4 doors. The monte_hall function should print answers 
to the following 2 questions: Based on the simulation, what is the probability of winning if you switch doors, 
and what is the probability of winning if you keep door A? 
Your function should return these values in a tuple (prob_win_if_switch, prob_win_if_keep).

"""
# -*- coding: utf-8 -*-
 #for random.Generator.shuffle
 # https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.shuffle.html#numpy.random.Generator.shuffle

import numpy as np

def monty_hall():
    # 1 represents Car and 0 represents Goat
    doors = np.array([0,0,1,0])
    # instance of generator
    rng = np.random.default_rng()
    #shuffle and randomly allocate the car in one of the doors
    rng.shuffle(doors)
    
    # as per the question, for simplicity assuming player opens door A first
    # 0 represents index of door A
    selected_door = 0
     # making a list of doors without car (excluding A)
    non_car_doors= np.array([])
    index = 1
    for door in np.nditer(doors[1:]):
        if door!=1:
            non_car_doors=np.append(non_car_doors, index)
        index+=1
    # Host opens one of the doors without Car
    host_door = rng.choice(non_car_doors)
    
    # check if wins a car by switching
    unopened_doors = np.setdiff1d(np.array([0,1,2,3]),[selected_door, host_door]) 
    switched_door = rng.choice(unopened_doors)
    if(doors[switched_door]==1):
        win_switch = True
    else:
        win_switch = False
    
    # check if wins a car by keeping the door A
    if(doors[selected_door]==1):
        win_keep = True
    else:
        win_keep = False
    
    return win_switch, win_keep

def monte_carlo_simulation(n):
    win_if_switch = 0
    win_if_keep = 0
    
    #run random simulations for n times
    for i in range(n):
        switch, keep = monty_hall()
        win_if_switch += switch
        win_if_keep += keep
    
    # finding probability
    prob_win_if_switch = win_if_switch/n
    prob_win_if_keep = win_if_keep/n
    
    return (prob_win_if_switch,prob_win_if_keep)

#take input from the user
num = int(input("Enter number of simulations: "))
print(monte_carlo_simulation(num))
