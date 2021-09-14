class Tile():
    def __init__(self, x:int, y:int, tribe: str):
        self.position = {"x": x, "y": y}
        self.tribe = tribe
        self.fogged_player_ids = []
        self.city: bool = False
        self.type: str = "none"
        self.water: bool = False
        self.shallow_water: bool = False
        self.troop = None