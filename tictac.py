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
        restart_button.pack()

        self.board = tkinter.Canvas(self.parent, width=self.tile_size*3,
                                    height=self.tile_size*3)
        for row in range(3):
            for column in range(3):
                color = 'cyan'
                self.board.create_rectangle(self.tile_size * column,
                                            self.tile_size * row,
                                            self.tile_size * (column + 1),
                                            self.tile_size * (row + 1),
                                            fill=color)
        self.board.grid()

        self.board.pack()

        self.initialize_game()
        

    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts

        pass

    def restart(self):
        # This method is invoked when the user clicks on the RESTART button.
        # Erase the canvas
        # invoke initialize_game
        pass

    def play(self, event):
        # This method is invoked when the user clicks on a square.
        # If the square is already taken, do nothing.
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
