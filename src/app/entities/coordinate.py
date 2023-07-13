class Coordinate:
    x: float
    y: float

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    @staticmethod
    def from_json(json):
        return Coordinate(json['x'], json['y'])
    
    def __repr__(self):
        return f"Coordinate: {self.x},{self.y}"
    
    @staticmethod
    def distance(a, b):
        return abs(a.x - b.x) + abs(a.y - b.y)
    
    def move_command(self, move: str):
        if move == "up":
            return Coordinate(self.x, self.y + 1)
        elif move == "down":
            return Coordinate(self.x, self.y - 1)
        elif move == "left":
            return Coordinate(self.x - 1, self.y)
        elif move == "right":
            return Coordinate(self.x + 1, self.y)
        else:
            return Coordinate(self.x, self.y)