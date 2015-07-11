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
    score = {}
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

        Game.score = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                      (1, 0): 0, (1, 1): 0, (1, 2): 0,
                      (2, 0): 0, (2, 1): 0, (2, 2): 0}
        print("__init__ len(Game.score.card)", len(Game.score))


    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts

        Game.score = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
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
        print(type(Game.score))
        print("play self.score_card.len() =", len(Game.score))
        print("play top_ game  Game.user_score", Game.user_score)
        grid_row = event.x // 100
        grid_column = event.y // 100
        if Game.score[(grid_row, grid_column)] == 0:
            for row in range(3):
                for column in range(3):
                    if row == grid_row and column == grid_column:
                        self.board.create_rectangle(grid_row*100,
                                                grid_column*100,
                                                grid_row*100+100,
                                                grid_column*100+100,
                                                fill='black')
                        Game.score[(row, column)] = 5
                        print("Game.user_score =", Game.user_score)
                        self.check_game()
                        self.computer_move()
                        print("this fired")

        else:
            print('')
        self.board.grid()
        print("play - bottom  Game.user_score", Game.user_score)

    def computer_move(self):
        ran_x = random.randint(0, 2)
        ran_y = random.randint(0, 2)

        if Game.score[(ran_x, ran_y)] == 0:
            Game.score[(ran_x, ran_y)] = 5
            self.board.create_rectangle(ran_x*100,
                                                ran_y*100,
                                                ran_x*100+100,
                                                ran_y*100+100,
                                                fill='white')
            Game.check_game()
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
        for x in range(3):
            for y in range(3):
                row_total += Game.score[(x, y)]
        for y in range(3):
            for x in range(3):
                column_total += Game.score[(x, y)]
        diag_leftdown = Game.score[(0, 0)] + Game.score[(1, 1)] \
                        + Game.score[(2, 2)]
        diag_leftup = Game.score[(2, 0)] + Game.score[(1, 1)] \
                      + Game.score[(0, 2)]
        score_list = [row_total, column_total, diag_leftup, diag_leftdown]

        for x in score_list:
            print("x ", x)

        for x in score_list:
            if Game.user_score == 15:
                print(" check_game Game.user_score = ", Game.user_score)
                print("You won")
                exit()
            else:
                Game.user_score += 5
            if Game.comp_score == 30:
                print("computer won")
                exit()
            else:
                Game.comp_score += 10

                # Add your method definitions here

def main():
    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop
    root = tkinter.Tk()
    ttgame = Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
