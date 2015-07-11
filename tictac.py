# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:
# -----------------------------------------------------------------------------
'''
Enter the module docstring here
'''
import tkinter
import random



tally_array = []
class Game(object):
    '''
    Enter the class docstring here
    '''

    # Add your class variables if needed here
    tile_size = 100
    player = ''
    user = ''
    computer = ''
    user_color = 'green'
    computer_color = 'blue'
    board = tkinter.Canvas()
    tile_owner = 0
    sq_avail = {}
    user_score = 0
    comp_score = 0
    total_score = 0


    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent

        # Add your instance variables  if needed here
        # Create the restart button widget
        # Create a canvas widget
        # Create a label widget for the win/lose message

        restart_button = tkinter.Button(self.parent, text='restart',
                                        width=20,
                                        command=self.restart())
        restart_button.grid()

        self.board = tkinter.Canvas(self.parent, width=self.tile_size * 3,
                                    height=self.tile_size * 3)

        self.initialize_game()

        self.board.bind("<Button-1>", self.play)

        Game.sq_avail = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                      (1, 0): 0, (1, 1): 0, (1, 2): 0,
                      (2, 0): 0, (2, 1): 0, (2, 2): 0}
        print("__init__ len(Game.score.card)", len(Game.sq_avail))


    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts

        Game.sq_avail = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                      (1, 0): 0, (1, 1): 0, (1, 2): 0,
                      (2, 0): 0, (2, 1): 0, (2, 2): 0}
        for row in range(3):
            for column in range(3):
                if(row + column) % 2 == 0:
                    color = 'cyan'
                else:
                    color = 'yellow'

                self.board.create_rectangle(self.tile_size * row,
                                            self.tile_size * column,
                                            self.tile_size * (row + 1),
                                            self.tile_size * (column + 1),
                                            fill=color)
        self.board.grid()

    def restart(self):
        # This method is invoked when the user clicks on the RESTART button.
        # Erase the canvas
        # invoke initialize_game
        pass

    def play(self, event):
        # This method is invoked when the user clicks on a square.
        # If the square is already taken, do nothing.
        grid_row = event.x // 100
        grid_column = event.y // 100
        if Game.sq_avail[(grid_row, grid_column)] == 0:
            for row in range(3):
                for column in range(3):
                    if row == grid_row and column == grid_column:
                        self.board.create_rectangle(grid_row*100,
                                                grid_column*100,
                                                grid_row*100+100,
                                                grid_column*100+100,
                                                fill='black')
                        Game.sq_avail[(row, column)] = 5
                        Game.check_game(self)
                        Game.computer_move(self)
                        print("this fired")

        else:
            print('')
        self.board.grid()

    def computer_move(self):
        ran_x = random.randint(0, 2)
        ran_y = random.randint(0, 2)
        print("entered computer_move")

        if Game.sq_avail[(ran_x, ran_y)] == 0:
            Game.sq_avail[(ran_x, ran_y)] = 3
            self.board.create_rectangle(ran_x*100,
                                                ran_y*100,
                                                ran_x*100+100,
                                                ran_y*100+100,
                                                fill='white')
            Game.check_game(self)
            self.board.grid()
        else:
            self.computer_move()
    def check_game(self):
        # Check if the game is won or lost
        # Return True or False
        row_total = 0
        column_total = 0
        diag_leftdown = 0
        diag_leftup = 0
        line_list = []
        i = 0
        for x in range(3):
            for y in range(3):
                i += 1
                row_total += Game.sq_avail[(x, y)]
                if row_total == 15:
                    print("you won row_total", row_total)
                    exit()
                if row_total == 9:
                    print("the computer won row total", row_total)
                    exit()
                if i == 3:
                    i = 0
                    row_total = 0
        for y in range(3):
            for x in range(3):
                i += 1
                column_total += Game.sq_avail[(x, y)]
                if column_total == 15:
                    print("you won column total", column_total)
                    exit()
                if row_total == 9:
                    print("the computer won row total", row_total)
                    exit()
                if i == 3:
                    i = 0
                    column_total = 0

        diag_leftdown = Game.sq_avail[(0, 0)] + Game.sq_avail[(1, 1)] \
                                           + Game.sq_avail[(2, 2)]
        if diag_leftdown == 15:
            print("you won diag_up", diag_leftdown)
            exit()
        if row_total == 9:
            print("the computer won row total", row_total)
            exit()
        diag_leftup = Game.sq_avail[(2, 0)] + Game.sq_avail[(1, 1)] \
                                         + Game.sq_avail[(0, 2)]
        if diag_leftup == 15:
            print("you won diag_leftup", diag_leftup)
            exit()
        if row_total == 9:
            print("the computer won row total", row_total)
            exit()

        #score_list = [row_total, column_total, diag_leftup,
       #                       diag_leftdown]
#
       # for x in score_list:
         #   print("x ", x)

def main():
    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop
    root = tkinter.Tk()
    ttgame = Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
