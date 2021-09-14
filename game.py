from board import Board

class Game():
    def __init__(self):
        self.board = Board()
        self.board.create_water()


game = Game()

def print_game():
    print()
    for i in range(0, len(game.board.tiles)):
        col = ""
        for j in range(0, len(game.board.tiles[i])):
            if (game.board.tiles[i][j].shallow_water):
                col = col + "🔷"
            elif (game.board.tiles[i][j].water) :
                col = col + "🟦"
            else:
                col = col + "🟩"
            

        print(col)

print_game()
