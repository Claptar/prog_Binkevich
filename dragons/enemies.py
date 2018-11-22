from gameunit import *
from random import randint, choice


class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._healthfull = 50
        self._health = 50
        self._attack = 10
        self._experience = 50
        self._name = 'Зелёный Дракон'


class RedDragon (Dragon):
    def __init__(self):
        self._healthfull = 100
        self._health = 100
        self._attack = 20
        self._experience = 60
        self._name = 'Зелёный Дракон'


class BlackDragon(Dragon):
    def __init__(self):
        self._healthfull = 150
        self._health = 150
        self._attack = 30
        self._experience = 70
        self._name = 'Зелёный Дракон'


enemy_types = [GreenDragon, RedDragon, BlackDragon]
