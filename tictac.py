# -----------------------------------------------------------------------------
# Name:       tictac
# Purpose:    Implement a game of Tic Tac Toe
#
# Author:     David Gudeman
# Date:       July 12, 2015
# Course:     CS21A Foothill College
# -----------------------------------------------------------------------------
"""
Module to create a tic tac toe game where the user plays against the computer
The user always starts first and the computer picks squares at random
"""
import tkinter
import random

class Game(object):
    """
    Creates a tic tac toe board. It has a restart button and a label to
    state who wins or loses. The user always starts first. User squares are
    chosen by mouse click. When a square (aka tile) is chosen it changes color.
    The computer moves immediately after the user choice is made.
    """
    # class variables
    sq_avail = {}           # a dictionary, holds an integer state the tiles
    turns = 0               # count how many choices have been made
    board_color = 'green'   # color of the initial board tiles

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent

        # instance variables
        self.user_color = 'cyan'    # color of the user tiles
        self.comp_color = 'yellow'  # color of the computer tiles
        self.tile_size = 100        # size of tile
        self.game_over = False      # boolean state of the game

        # create a tkinter Button for restarting the game
        self.parent.restart_button = tkinter.Button(self.parent,
                                                    text='restart',
                                                    width=20,
                                                    command=self.restart)
        # uset the 'grid' geometry manager and put the button on grid
        self.parent.restart_button.grid()

        # create a label
        # use the tkinter StringVar construct to hold the dispaly string
        self.parent.sb_message = tkinter.StringVar()
        self.parent.sb_message.set('Scorecard') # set an initial string

        # create label with 'textvariable' to collect the StringVar value
        self.parent.scoreboard_label = tkinter.Label(self.parent,
                                        textvariable=self.parent.sb_message)
        self.parent.scoreboard_label.grid()  # place it on the grid

        # create a Canvas that is size dependent on the tile size
        self.board = tkinter.Canvas(self.parent, width=self.tile_size * 3,
                                    height=self.tile_size * 3)
        self.board.grid()  # place it on the grid

        # bind mouse click to Canvas (aka board) to collect tile clicks
        self.board.bind("<Button-1>", self.play)  # calls the 'play' callback
        self.initialize_game() # initialize a game

    def initialize_game(self):
        """
        intializes the game, used to start as well as restart the game

        resets number of turns, boolean game state, label message,
        dictionary of tile states, board tiles
        parameter: none

        :return: none
        """
        Game.turns = 0                 # resets turn counter
        self.game_over = False         # resets boolean game state
        self.parent.sb_message.set("Score card")  # resets label message

        # sets dict representation of the tile values to 0
        Game.sq_avail = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                         (1, 0): 0, (1, 1): 0, (1, 2): 0,
                         (2, 0): 0, (2, 1): 0, (2, 2): 0}

        # constructs the tiles
        for row in range(3):
            for column in range(3):
                self.board.create_rectangle(self.tile_size * row,
                                            self.tile_size * column,
                                            self.tile_size * (row + 1),
                                            self.tile_size * (column + 1),
                                            fill=Game.board_color)

    def restart(self):
        """
        restarts the game using th initialize method
        erases the tiles of last game and calls initialize_game

        parameter: none
        :return: none
        """
        self.board.delete("all")    # erased board
        self.initialize_game()      # initializes game

    def play(self, event):
        """
        It is an event handler for mouse clicks
        on the board.

        :param event: the mouse click on the board (aka canvas)
        :return:
        """
        if not self.game_over:      # check to see if game_over is True

            grid_row = event.x // 100       # use floor function to identify
            grid_column = event.y // 100    # the tile owning the mouse click

            # check to see if the tile has been clicked before
            if Game.sq_avail[(grid_row, grid_column)] == 0:

                for row in range(3):         # iterate the tiles to id the
                    for column in range(3):  # tile and change its color
                        if row == grid_row and column == grid_column:
                            self.board.create_rectangle(grid_row * 100,
                                                    grid_column * 100,
                                                    grid_row * 100 + 100,
                                                    grid_column * 100 + 100,
                                                    fill=self.user_color)
                            # set the tile value to 5 which is a user
                            # specific increment
                            Game.sq_avail[(row, column)] = 5
                            Game.turns += 1        # increment turn count

                            # check the new state of the game
                            Game.check_game(self)
                            if not self.game_over:

                                # if game not over call computer move
                                Game.computer_move(self)
                                Game.check_game(self)  # check again

    def computer_move(self):
        """
        generates the computers move randomly

        :parameter none
        :return:   none
        """

        ran_x = random.randint(0, 2)  # generate a random coordinates
        ran_y = random.randint(0, 2)

        if Game.sq_avail[(ran_x, ran_y)] == 0:  # check tile availability

            # if okay set tile value to computer specific amount
            Game.sq_avail[(ran_x, ran_y)] = 3

            # color the appropriate tile
            self.board.create_rectangle(ran_x * 100,
                                        ran_y * 100,
                                        ran_x * 100 + 100,
                                        ran_y * 100 + 100,
                                        fill=self.comp_color)
            Game.turns += 1  # increment the turn counter
        else:
            self.computer_move()  # if tile full re-call method

    def check_game(self):
        """
        checks the game to see if there is a win lose or draw

        it checks the columns, rows and diagonals separately. Updates the
        game state flag - game_over. Jt updates the label as to the new
        state of the game.

        parameter: none
        :return:   the boolean state of the game
        """
        row_total = 0     # initialize variable to collect totals
        column_total = 0  # initialize a counter
        i = 0

        # iterate through the columns. A user 3-tile positive will add to 15
        # a computer 3-tile posiitve will add to 9
        for x in range(3):
            for y in range(3):
                i += 1
                column_total += Game.sq_avail[(x, y)]
                if column_total == 15:
                    self.parent.sb_message.set('You Won!!!!')  # label update
                    self.game_over = True  # set the game over flag
                    return self.game_over

                if column_total == 9:
                    self.parent.sb_message.set('You have been ignominiously '
                                               'defeated')
                    self.game_over = True  # set the game over flag
                    return self.game_over
                if i == 3:
                    i = 0            # after adding 3 tiles reset index
                    column_total = 0 # reset column total

        # iterate through the rows. Comments are homologous to column iteration
        for y in range(3):
            for x in range(3):
                i += 1
                row_total += Game.sq_avail[(x, y)]
                if row_total == 15:
                    self.parent.sb_message.set('You Won!!!!')
                    self.game_over = True
                    return self.game_over
                if row_total == 9:
                    self.parent.sb_message.set('You have been ignominiously '
                                               'defeated')
                    self.game_over = True
                    return self.game_over
                if i == 3:
                    i = 0
                    row_total = 0

        # check the diagonals in a similar way
        diag_leftdown = Game.sq_avail[(0, 0)] + Game.sq_avail[(1, 1)] \
                        + Game.sq_avail[(2, 2)]
        if diag_leftdown == 15:
            self.parent.sb_message.set('You Won!!!!')
            self.game_over = True
            return self.game_over
        if diag_leftdown == 9:
            self.parent.sb_message.set('You have been ignominiously defeated')
            self.game_over = True
            return self.game_over

        diag_leftup = Game.sq_avail[(2, 0)] + Game.sq_avail[(1, 1)] \
                      + Game.sq_avail[(0, 2)]
        if diag_leftup == 15:
            self.parent.sb_message.set('You Won!!!!')
            self.game_over = True
            return self.game_over
        if diag_leftup == 9:
            self.parent.sb_message.set('You have been ignominiously defeated')
            self.game_over = True
            return self.game_over

        # stop the game and call a tie if all the tiles have been exhausted
        if Game.turns == 9:
            self.parent.sb_message.set('It is a tie :-|')
            self.game_over = True
            return self.game_over

        # if all else fails return original state of table
        return self.game_over

def main():
    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop
    root = tkinter.Tk()             # Instantiate a root window
    ttgame = Game(root)             # Instantiate a Game object
    root.mainloop()                 # Enter the main event loop, start waiting

if __name__ == '__main__':
    main()
