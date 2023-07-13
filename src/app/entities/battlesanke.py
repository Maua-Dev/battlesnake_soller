from typing import List
from src.app.entities.coodinate import Coordinate


class Battlesnake:
    snake_id: str
    name: str
    health: int
    body: List[Coordinate]
    latency: str
    head: Coordinate
    length: int
    shout: str
    squad: str
    
    def __init__(self, snake_id: str, name: str, health: int, body: List[Coordinate], latency: str, head: Coordinate, length: int, shout: str, squad: str):
        self.snake_id = snake_id
        self.name = name
        self.health = health
        self.body = body
        self.latency = latency
        self.head = head
        self.length = length
        self.shout = shout
        self.squad = squad

    def __eq__(self, other):
        return self.snake_id == other.snake_id and self.name == other.name and self.health == other.health and self.body == other.body and self.latency == other.latency and self.head == other.head and self.length == other.length and self.shout == other.shout and self.squad == other.squad

    def __repr__(self):
        return f"Snake: {self.name} ({self.snake_id})"
    
    @staticmethod
    def from_json(json):
        snake_id = json["id"]
        name = json["name"]
        health = json["health"]
        body = [Coordinate.from_json(body) for body in json["body"]]
        latency = json["latency"]
        head = Coordinate.from_json(json["head"])
        length = json["length"]
        shout = json["shout"]
        squad = json.get("squad", "")
        return Battlesnake(snake_id, name, health, body, latency, head, length, shout, squad)