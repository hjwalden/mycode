#!/usr/bin/env python3
#Utilizing class and creating own functions
#Written by Homer Walden

from random import randint

class Player:                                  #create class for Player
  def __init__(self):
    self.dice = []

  def roll(self):
    self.dice = [] # clears current dice
    for i in range(3):
      self.dice.append(randint(1,6))

  def get_dice(self):
    return self.dice

class Cheat_Swapper(Player):                    #create subclass of Player called Cheat Swapper
  def cheat(self):
    self.dice[-1] = 6

class Cheat_Loaded_Dice(Player):                #create subclass of Player called Cheat_Loaded_Dice
  def cheat(self):
    i = 0
    while i < len(self.dice):
      if self.dice[i] < 6:
        self.dice[i] += 1
      i += 1