from typing import List
from src.app.entities.battlesanke import Battlesnake

from src.app.entities.coodinate import Coordinate


class Board:
    height: int
    width: int
    food: List[Coordinate]
    snakes: List[Coordinate]
    hazards: List[Battlesnake]

    def __init__(self, height: int, width: int, food: List[Coordinate], snakes: List[Coordinate], hazards: List[Battlesnake]):
        self.food = food
        self.height = height
        self.width = width
        self.snakes = snakes
        self.hazards = hazards

        
    def __eq__(self, other):
        return self.height == other.height and self.width == other.width and self.food == other.food and self.snakes == other.snakes and self.hazards == other.hazards
    
    def __repr__(self):
        return f"Board: {self.width}x{self.height}"

    @staticmethod
    def from_json(json):
        height = json["height"]
        width = json["width"]
        food = [Coordinate.from_json(food) for food in json["food"]]
        snakes = [Battlesnake.from_json(snake) for snake in json["snakes"]]
        hazards = [Coordinate.from_json(hazard) for hazard in json["hazards"]]
        return Board(height, width, food, snakes, hazards)
