import pygame
from enemy import Enemy

def heuristic1(pos1, pos2):
    return (pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2

class Tower:
    def __init__(self, x : int, y : int, range : int, dmg : int, fireRate : int):
        self.__x = x
        self.__y = y
        self.__range = range
        self.__dmg = dmg
        self.__fireRate = fireRate
        self.__cooldown = 0

    def in_range(self, pos : tuple[int, int]):
        return (self.__x - pos[0])**2 + (self.__y - pos[1])**2 <= self.__range**2

    def shoot(self, enemy_list : list[Enemy], goal : tuple[int, int]):
        if self.__cooldown > 0:
            self.__cooldown -= 1
            return
        target = -1
        target_dist = 1e10
        for i in range(len(enemy_list)):
            if self.in_range(enemy_list[i].pos):
                if target_dist > heuristic1(goal, enemy_list[i].pos):
                    target = i
        if target != -1:
            enemy_list[target].take_damage(self.__dmg)
            self.__cooldown = self.__fireRate
