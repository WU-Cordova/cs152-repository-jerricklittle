from projects.project2.Grid import Grid
from projects.project2.Game_Control import Game_Control

def main():
    grid = Grid(5,5)
    game_control = Game_Control(grid)
    game_control.run(100)




if __name__ == '__main__':
    main()
