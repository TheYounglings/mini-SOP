import pygame
import gridBlock
import pathFinding

class Enemy:
    def __init__(self, x, y, speed = 1, health = 100, djikstra = True):
        self.__x = x
        self.__y = y
        self.__speed = speed
        self.__health = health
        self.__djikstra = djikstra
        self.__wait = 0

    def render(self, screen : pygame.Surface):
        color = pygame.Color('blue')
        if self.__djikstra:
            color = pygame.Color('darkblue')
        pygame.draw.circle(screen, color, (self.__x, self.__y), 10)

    def move(self, board : list[list[gridBlock.GridBlock]], goal : tuple[int, int]):
        gx, gy = goal
        if self.__wait > 0:
            self.__wait -= 1
            return False
        if self.__djikstra:
            a = pathFinding.djikstra(self.__x//50, self.__y//50, board)
        else:
            a = pathFinding.Astar(self.__x//50, self.__y//50, gx, gy, board)
        if a == -1: # game over
            return True
        if a == 1: self.__x -= 50
        if a == 2: self.__y -= 50
        if a == 3: self.__x += 50
        if a == 4: self.__y += 50
        self.__wait = board[self.__y//50][self.__x//50].travelTime
        return False

    def alive(self):
        return self.__health > 0

    @property
    def pos(self):
        return self.__x, self.__y

    def take_damage(self, damage):
        self.__health -= damage