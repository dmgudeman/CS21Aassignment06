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
    score_card = {}


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

        Game.score_card = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                      (1, 0): 0, (1, 1): 0, (1, 2): 0,
                      (2, 0): 0, (2, 1): 0, (2, 2): 0}
        print("__init__ len(self.score.card)", len(Game.score_card))


    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts

        Game.score_card = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                      (1, 0): 0, (1, 1): 0, (1, 2): 0,
                      (2, 0): 0, (2, 1): 0, (2, 2): 0}
        for row in range(3):
            for column in range(3):
                if(row + column) % 2 == 0:
                    color = 'cyan'
                else:
                    color = 'yellow'

                self.board.create_rectangle(self.tile_size * column,
                                            self.tile_size * row,
                                            self.tile_size * (column + 1),
                                            self.tile_size * (row + 1),
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
        print(type(Game.score_card))
        print("play self.score_card.len() =", len(Game.score_card))
        grid_row = event.y // 100
        grid_column = event.x // 100
        for row in range(3):
            for column in range(3):
                if row == grid_row and column == grid_column \
                        and Game.score_card[(row, column)] == 0:
                    print(Game.score_card[(1, 1)])
                    self.board.create_rectangle(grid_column*100,
                                                grid_row*100,
                                                grid_column*100+100,
                                                grid_row*100+100,
                                                fill='black')
                    Game.score_card[(row, column)] = 5
                    print(type(Game.score_card))
                    print(Game.score_card[(row, column)])
                    print("this fired")

                else:
                    print('')
        self.board.grid()

    def computer_move(self):
        pass

    def check_game(self):
        # Check if the game is won or lost
        # Return True or False
        x = 'Hello World'
        print(x)
        pass

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
