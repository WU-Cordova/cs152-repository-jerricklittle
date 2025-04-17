
class Cell:
    def __init__(self, is_alive: bool = False) -> None:
        self.alive = is_alive
        # self.__loc = (int, int)

    def num_neighbors(self):
        pass

    def __eq__(self, other: object) -> bool:
        return self.alive == other.alive
    
    def __str__(self):
        if self.is_alive == False:
            return ' '
        else:
            return 'X'
    @property    
    def is_alive(self) -> bool:
        return self.alive
    
    @is_alive.setter
    def is_alive(self, is_alive: bool) -> None:
        self.alive = is_alive