from typing import List, Optional, Tuple
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
    def navigate_to(start: Coordinate, end: Coordinate) -> str:
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
        
    def where_to_go(self, me: Battlesnake) -> str:
            
        near_snake, move = self.get_near_snake_head(me)
           
        if len(self.food) > 0 and near_snake is None:
            move = self.navigate_to(me.head, self.get_closest_food(me))
        elif near_snake is not None:
            move = self.navigate_to(me.head, near_snake.head)
        else:
            move = self.navigate_to(me.head, me.body[0])
        
        return move

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

    def dodge_snake_body(self, me: Battlesnake, old_move: str):
        if  self.can_move(old_move, me):
            return old_move

        for move in ["up", "down", "left", "right"]:
            if self.can_move(move, me):
                return move
        return old_move
    
    def is_out_of_bounds(self, move: str, head: Coordinate):
        coordinate = head.move_command(move)
        if coordinate.x < 0 or coordinate.x >= self.width or coordinate.y < 0 or coordinate.y >= self.height:
            return True
        return False
    
    def can_move(self, move: str, me: Battlesnake):
        head = me.head
        snake, move_returned = self.get_near_snake_head(me, move)

        if not self.is_out_of_bounds(move, head) and not self.is_snake(move, head) and not self.is_hazard(move, head) and not (snake is not None and snake.length >= me.length):
            return True
        return False

    def is_near_snake_head(self, move: str, me: Battlesnake):
        snake, move = self.get_near_snake_head(me, move)

        if snake is not None:
            return True
        return False
    
    def get_near_snake_head(self, me: Battlesnake, move: str = None) -> Tuple[Optional[Battlesnake], Optional[str]]:
        if move is not None:
            coordinate = me.head.move_command(move)
            for snake in self.snakes:
                if snake.is_near_head(coordinate) and snake.snake_id != me.snake_id:
                    return snake, move
            return None, None
        
        for move in ["up", "down", "left", "right"]:
            coordinate = me.head.move_command(move)
            for snake in self.snakes:
                if snake.is_near_head(coordinate) and snake.snake_id != me.snake_id:
                    return snake, move
        return None, None
        
