import pygame.draw
from enum import Enum
from building import Building


class GridBlock:
    def __init__(self, _id : int, _screenX : int, _screenY : int, _travelTime : int, _size : int, _color : pygame.Color, _building : Building):
        self.__id = _id
        self.__screenX = _screenX # screen coordinate for the grid tile
        self.__screenY = _screenY # screen coordinate for the grid tile
        self.__travelTime = _travelTime # how long it takes to travel through the tile, -1 is not possible to travel
        self.__size = _size
        self.__color = _color
        self.__selected = False
        self.__building = _building
        self.__tower_id = -1
    
    @property
    def id(self):
        return self.__id

    @property
    def x(self):
        return self.__screenX
    
    @property
    def y(self):
        return self.__screenY
    
    @property
    def travelTime(self):
        return self.__travelTime

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, col : pygame.Color):
        self.__color = col

    def select(self):
        self.__selected = True

    def deselect(self):
        self.__selected = False

    def render(self, screen : pygame.Surface):
        color = self.color
        if self.__selected:
            color = pygame.Color("red")
        pygame.draw.rect(screen, color, (self.x, self.y, self.__size, self.__size))

    def build_slow(self):
        if self.__building != Building.none:
            return
        self.__building = Building.slow
        self.color = "green"
        self.__travelTime = 5

    def make_spawn(self):
        self.__building = Building.spawn
        self.color = "orange"

    def make_goal(self):
        self.__building = Building.goal
        self.color = "yellow"

    def is_goal(self):
        return self.__building == Building.goal

    def build_wall(self):
        if self.__building != Building.none:
            return False
        self.__building = Building.wall
        self.__travelTime = -1
        self.color = "grey"
        return True

    def remove_building(self):
        v = -1
        if self.__building == Building.none:
            return v
        if self.__building == Building.tower:
            v = self.__id
        self.__building = Building.none
        self.color = "lightblue"
        self.__travelTime = 1
        return v

    def build_tower(self):
        if self.__building != Building.none:
            return False
        self.__building = Building.tower
        self.color = "pink"
        self.__travelTime = -1
        return True

    @property
    def tower_id(self):
        return self.__tower_id

    @tower_id.setter
    def tower_id(self, tower_id : int):
        self.__tower_id = tower_id