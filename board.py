from tile import Tile
import random

class Board():
    def __init__(self):
        tiles = []
        for i in range(1,31):
            col = []
            for j in range(1,31):
                col.append(Tile(i, j, 'none'))
            tiles.append(col)
        self.tiles = tiles

    def get_local_squares(self, i, j):
        local_squares = []
        if (i - 1 != 0 and i + 1 != 30 and j - 1 != 0 and j + 1 != 30):
            local_squares = [
                (self.tiles[i-1][j].water),
                (self.tiles[i+1][j].water),
                (self.tiles[i][j-1].water),
                (self.tiles[i][j+1].water),
                (self.tiles[i-1][j-1].water),
                (self.tiles[i+1][j-1].water),
                (self.tiles[i-1][j+1].water),
                (self.tiles[i+1][j+1].water)
            ]
        return local_squares

    def for_every_tile(self, callback, count):
        index = 0
        while (index < count):
            for i in range(0, 30):
                for j in range(0, 30):
                    if (callback(i, j)):
                        index = index + 1

    def create_water(self):
        index = 0 
        while (index < random.randint(10, 15)):
            random.choice(random.choice(self.tiles)).water = True
            index = index + 1

        def addWater(i, j):
            rand_bool = random.randint(0, 1) == 1
            success = False
            if (i - 1 != 0 and i + 1 != 30 and j - 1 != 0 and j + 1 != 30):
                next_to_water = (self.tiles[i-1][j].water) or \
                (self.tiles[i+1][j].water) or \
                (self.tiles[i][j-1].water) or \
                (self.tiles[i][j+1].water) or \
                (self.tiles[i-1][j-1].water) or \
                (self.tiles[i+1][j-1].water) or \
                (self.tiles[i-1][j+1].water) or \
                (self.tiles[i+1][j+1].water)

                if (rand_bool & next_to_water):
                    self.tiles[i][j].water = True
                    success = True
            return success
        self.for_every_tile(addWater, 15)

        def remove_islands(i, j):
            local_squares = self.get_local_squares(i, j)
            
            count = 0
            for square in local_squares:
                if (square):
                    count = count + 1
            if (count >= 5):
                self.tiles[i][j].water = True

            return True
        self.for_every_tile(remove_islands, 15)

        def remove_small_lakes(i, j):
            local_squares = self.get_local_squares(i, j)


            count = 0
            for square in local_squares:
                if not (square):
                    count = count + 1

            if (count >= 6):
                self.tiles[i][j].water = False

            return True
        self.for_every_tile(remove_small_lakes, 10)

        def addShallowWater(i, j):
            local_squares = self.get_local_squares(i, j)
            count = 0
            for square in local_squares:
                if not (square):
                    count = count + 1

            if (self.tiles[i][j].water and count >= 3):
                self.tiles[i][j].shallow_water = True

            return True

        self.for_every_tile(addShallowWater, 1)
            
    # def create_cities(self, number):
    #     cities = 0
    #     while (cities > number):
    #         tile = random.choice(random.choice(self.tiles))
    #         if not tile.water:
    #             local_squares = get_local_squares(tile.position.x - 1, tile.position.y - 1)
