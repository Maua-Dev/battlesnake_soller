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
    
    def move_command(move: str):
        if move == "up":
            return Coordinate(0, 1)
        elif move == "down":
            return Coordinate(0, -1)
        elif move == "left":
            return Coordinate(-1, 0)
        elif move == "right":
            return Coordinate(1, 0)
        else:
            return Coordinate(0, 0)