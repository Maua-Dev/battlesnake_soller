from typing import List
from .battlesanke import Battlesnake

from .coordinate import Coordinate


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

    @staticmethod
    def navigate_to(start: Coordinate, end: Coordinate):
        if start.x < end.x:
            return "right"
        elif start.x > end.x:
            return "left"
        elif start.y < end.y:
            return "up"
        elif start.y > end.y:
            return "down"
        else:
            return "up"

    def get_closest_food(self, snake: Battlesnake):
        closest_food = self.food[0]
        for food in self.food:
            if Coordinate.distance(snake.head, food) < Coordinate.distance(snake.head, closest_food):
                closest_food = food
        return closest_food
    
    def is_snake(self, move: str, head: Coordinate):
        coordinate = head.move_command(move)
        for snake in self.snakes:
            if snake.is_inside_snake(coordinate):
                return snake
        return False
    
    def is_hazard(self, move: str, head: Coordinate):
        coordinate = head.move_command(move)
        for hazard in self.hazards:
            if hazard == coordinate:
                return True
        return False
    
