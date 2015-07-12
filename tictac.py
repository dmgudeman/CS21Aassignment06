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
    tile_owner = 0
    sq_avail = {}
    user_score = 0
    comp_score = 0
    total_score = 0
    turns = 0
    board_color = 'green'

    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent
        self.user_color = 'cyan'
        self.comp_color = 'yellow'


        # Add your instance variables  if needed here
        # Create the restart button widget
        # Create a canvas widget
        # Create a label widget for the win/lose message
        self.tile_size = 100
        self.game_over = False

        self.parent.restart_button = tkinter.Button(self.parent,
                                                    text='restart',
                                                    width=20,
                                                    command=self.restart)
        self.parent.restart_button.grid()
        self.parent.sb_message = tkinter.StringVar()
        self.parent.sb_message.set('Scorecard')
        self.parent.scoreboard_label = tkinter.Label(self.parent,
                                                     textvariable=self.parent.sb_message)
        self.parent.scoreboard_label.grid()

        self.board = tkinter.Canvas(self.parent, width=self.tile_size * 3,
                                    height=self.tile_size * 3)
        self.board.grid()

        self.board.bind("<Button-1>", self.play)
        self.initialize_game()

    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts
        Game.turns = 0
        self.game_over = False
        self.parent.sb_message.set("Score card")
        Game.sq_avail = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                         (1, 0): 0, (1, 1): 0, (1, 2): 0,
                         (2, 0): 0, (2, 1): 0, (2, 2): 0}
        for row in range(3):
            for column in range(3):
                self.board.create_rectangle(self.tile_size * row,
                                            self.tile_size * column,
                                            self.tile_size * (row + 1),
                                            self.tile_size * (column + 1),
                                            fill=Game.board_color)

    def restart(self):
        # This method is invoked when the user clicks on the RESTART button.
        # Erase the canvas
        # invoke initialize_game
        self.board.delete("all")
        self.initialize_game()

    def play(self, event):
        # This method is invoked when the user clicks on a square.
        # If the square is already taken, do nothing.
        if not self.game_over:

            grid_row = event.x // 100
            grid_column = event.y // 100
            if Game.sq_avail[(grid_row, grid_column)] == 0:
                for row in range(3):
                    for column in range(3):
                        if row == grid_row and column == grid_column:
                            self.board.create_rectangle(grid_row * 100,
                                                    grid_column * 100,
                                                    grid_row * 100 + 100,
                                                    grid_column * 100 + 100,
                                                    fill=self.user_color)
                            Game.sq_avail[(row, column)] = 5
                            Game.turns += 1
                            Game.check_game(self)
                            if not self.game_over:
                                Game.computer_move(self)
                                Game.check_game(self)

    def computer_move(self):
        ran_x = random.randint(0, 2)
        ran_y = random.randint(0, 2)

        if Game.sq_avail[(ran_x, ran_y)] == 0:
            Game.sq_avail[(ran_x, ran_y)] = 3
            self.board.create_rectangle(ran_x * 100,
                                        ran_y * 100,
                                        ran_x * 100 + 100,
                                        ran_y * 100 + 100,
                                        fill=self.comp_color)
            Game.turns += 1
        else:
            self.computer_move()
            self.board.grid()
        Game.check_game(self)

    def check_game(self):
        # Check if the game is won or lost
        # Return True or False
        row_total = 0
        column_total = 0
        i = 0
        for x in range(3):
            for y in range(3):
                i += 1
                column_total += Game.sq_avail[(x, y)]
                if column_total == 15:
                    self.parent.sb_message.set('You Won!!!!')
                    self.game_over = True
                    return self.game_over

                if column_total == 9:
                    self.parent.sb_message.set('You have been ignominiously '
                                               'defeated')
                    self.game_over = True
                    return self.game_over
                if i == 3:
                    i = 0
                    column_total = 0
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
        if Game.turns == 9:
            self.parent.sb_message.set('It is a tie :-|')
            self.game_over = True
            return self.game_over
        return self.game_over

def main():
    # Instantiate a root window
    # Instantiate a Game object
    # Enter the main event loop
    root = tkinter.Tk()
    print("root = ", type(root))
    ttgame = Game(root)
    root.mainloop()


if __name__ == '__main__':
    main()
