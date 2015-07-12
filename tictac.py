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

    player = ''
    user = ''
    computer = ''
    board_color = 'green'
    user_color = 'cyan'
    computer_color = 'yellow'
    board = tkinter.Canvas()
    tile_owner = 0
    sq_avail = {}
    user_score = 0
    comp_score = 0
    total_score = 0
    turns = 0
    game_over = False


    def __init__(self, parent):
        parent.title('Tic Tac Toe')
        self.parent = parent


        # Add your instance variables  if needed here
        # Create the restart button widget
        # Create a canvas widget
        # Create a label widget for the win/lose message
        tile_size = 100
        self.restart_button = tkinter.Button(self.parent, text='restart',
                                        width=20,
                                        command=self.restart())
        self.restart_button.grid()

        self.scoreboard_label = tkinter.Label(self.parent, text='scoreboard',
                                             width=20)
        self.scoreboard_label.grid()

        self.board = tkinter.Canvas(self.parent, width=tile_size * 3,
                                    height=tile_size * 3)
        self.board.grid()
        for row in range(3):
            for column in range(3):
                self.board.create_rectangle(tile_size * row,
                                            tile_size * column,
                                            tile_size * (row + 1),
                                            tile_size * (column + 1),
                                            fill=Game.board_color)



        self.board.bind("<Button-1>", self.play)
        self.initialize_game()

    def initialize_game(self):
        # These are the initializations that need to happen
        # at the beginning and after restarts
        Game.turns = 0
        Game.game_over = False

        Game.sq_avail = {(0, 0): 0, (0, 1): 0, (0, 2): 0,
                      (1, 0): 0, (1, 1): 0, (1, 2): 0,
                      (2, 0): 0, (2, 1): 0, (2, 2): 0}

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
        print("game sequare available = ", Game.sq_avail[(grid_row, grid_column)])
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
                        Game.turns += 1
                        print("Game.turns = ", Game.turns)
                        Game.check_game(self)
                        if not Game.game_over:
                            print("Game.game_over =", Game.game_over)
                            Game.computer_move(self)
                            Game.check_game(self)
                        if Game.game_over:
                            print("game over")
                            exit()
                        print("this fired")

            self.board.grid()
        #else:
           # self.play(event)

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
            Game.turns += 1
            print("Game.turns = ", Game.turns)

        else:
            self.computer_move()
            self.parent.board.grid()
        Game.check_game(self)

    def check_game(self):
        # Check if the game is won or lost
        # Return True or False

        if Game.turns == 9:
            print("game is a tie")
            exit()
            game_over = True
            return game_over
        row_total = 0
        column_total = 0
        diag_leftdown = 0
        diag_leftup = 0
        line_list = []
        i = 0
        for x in range(3):
            for y in range(3):
                i += 1
                column_total += Game.sq_avail[(x, y)]
                if column_total == 15:
                    print("you won column_total", column_total)
                    game_over = True
                    return game_over

                if column_total == 9:
                    print("the computer won column_total", column_total)
                    game_over = True
                    return game_over
                if i == 3:
                    i = 0
                    column_total = 0
        for y in range(3):
            for x in range(3):
                i += 1
                row_total += Game.sq_avail[(x, y)]
                if row_total == 15:
                    print("you won row total", row_total)
                    game_over = True
                    return game_over
                if row_total == 9:
                    print("the computer won row total", row_total)
                    game_over = True
                    return game_over
                if i == 3:
                    i = 0
                    row_total = 0

        diag_leftdown = Game.sq_avail[(0, 0)] + Game.sq_avail[(1, 1)] \
                                           + Game.sq_avail[(2, 2)]
        if diag_leftdown == 15:
            print("you won diag_up", diag_leftdown)
            game_over = True
            return game_over
        if row_total == 9:
            print("the computer won row total", row_total)
            game_over = True
            return game_over
        diag_leftup = Game.sq_avail[(2, 0)] + Game.sq_avail[(1, 1)] \
                                         + Game.sq_avail[(0, 2)]
        if diag_leftup == 15:
            print("you won diag_leftup", diag_leftup)
            game_over = True
            return game_over
        if row_total == 9:
            print("the computer won row total", row_total)
            game_over = True
            return game_over
        print("Game.game_over at bottom of check_game = ", Game.game_over)
        return Game.game_over

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
