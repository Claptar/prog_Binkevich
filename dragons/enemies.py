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
        self._healthfull = 200
        self._health = 200
        self._attack = 10
        self._experience = 20
        self._name = 'Зелёный Дракон'


enemy_types = [GreenDragon, RedDragon, BlackDragon]
