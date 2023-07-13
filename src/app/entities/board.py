from typing import List
from src.app.entities.battlesanke import Battlesnake

from src.app.entities.coodinate import Coordinate


class Board:
    height: int
    width: int
    foods: List[Coordinate]
    snakes: List[Coordinate]
    hazards: List[Battlesnake]

    def __init__(self, height: int, width: int, foods: List[Coordinate], snakes: List[Coordinate], hazards: List[Battlesnake]):
        self.foods = foods
        self.height = height
        self.width = width
        self.snakes = snakes
        self.hazards = hazards

        
    def __eq__(self, other):
        return self.height == other.height and self.width == other.width and self.foods == other.foods and self.snakes == other.snakes and self.hazards == other.hazards
    
    def __repr__(self):
        return f"Board: {self.width}x{self.height}"

    @staticmethod
    def from_json(json):
        height = json["height"]
        width = json["width"]
        foods = [Coordinate.from_json(foods) for foods in json["foods"]]
        snakes = [Battlesnake.from_json(snake) for snake in json["snakes"]]
        hazards = [Coordinate.from_json(hazard) for hazard in json["hazards"]]
        return Board(height, width, foods, snakes, hazards)
