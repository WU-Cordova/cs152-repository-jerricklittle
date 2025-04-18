import time
from datastructures.array2d import Array2D
from projects.project2.Grid import Grid
from projects.project2.kbhit import KBHit
class Game_Control:
    def __init__(self, grid: Grid) -> None:
        print("from the constructor")
        self.grid = grid
        self.history = []


    def run(self, max_iter : int) -> None:
        kb = KBHit()

        print('Hit (Q) to stop or (S) to step or (C) to continue')

        generation = 0

        step_mode = False

        while True or generation < max_iter:

            print(f'In generation: {generation}')
            generation += 1
            self.grid.display()
            time.sleep(1)
            self.history.append(self.grid)
            new_grid = self.grid.next_gen()
            if len(self.history) > 5:
                if self.history[-1] == new_grid or self.history[-2] == new_grid or self.history[-3] == new_grid:
                    break
                del self.history[0]
            self.grid = new_grid
            if kb.kbhit() or step_mode:
                c = (kb.getch()).upper()
                # c_ord = ord(c)
                print(c)
                # print(c_ord)
                time.sleep(2)
                if c == 'q': # ESC
                    break
                print(c)
                if c == 's':
                    step_mode = True
                print(c)
                if c == 'c':
                    step_mode = False
            # if step_mode == True:
                
            # else:
            #     continue

        print("The colony is either dead or alive forever lol")

        kb.set_normal_term()