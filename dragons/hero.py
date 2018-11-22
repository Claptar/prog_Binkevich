from gameunit import *


class Hero(Attacker):
    def __init__(self, name):
        self._health = 100
        self._healthfull = 100
        self._attack = 10
        self._experience = 0
        self.name = name



