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