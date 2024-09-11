class gridBlock:
    def __init__(self, _id : int, _screenX : int, _screenY : int, _neigbours : list, _travelTime : int = -1):
        self.__id = _id;
        self.__screenX = _screenX # screen coordinate for the grid tile
        self.__screenY = _screenY # screen coordinate for the grid tile
        self.__travelTime = _travelTime # how long it takes to travel throug the tile, -1 is not possible to travel
        self.__neigbours = _neigbours # neigbouring grid cels
    
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
    def neigbours(self):
        return self.__neigbours
    
    @property
    def travelTime(self):
        return self.travelTime
    
