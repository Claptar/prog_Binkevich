from gameunit import *


class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._healthfull = 100
        self._attack = 10
        self._experience = 0
        self.name = name

   def attack(self, target):
        target._health -= self._attack
        print(target._name, target._health, '/', target._healthfull, 'HP')

    def exp_gain(self, target):
        self._experience += target._experience

    def is_lvl_up(self):
        if self._experience > 99:
            return True

    def lvl_up(self):
        self._attack += 10
        self._health = 100

    def exp_down(self):
        self._experience = 0



