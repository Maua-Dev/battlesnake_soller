from src.app.entities.battlesanke import Battlesnake
from src.app.entities.coodinate import Coordinate


class Test_Battlesnake:
    def test_battlesnake(self):
        snake_id = "1"
        name = "name"
        health = 100
        body = []
        latency = "latency"
        head = Coordinate(1, 2)
        length = 1
        shout = "shout"
        squad = "squad"

        battlesnake = Battlesnake(snake_id, name, health, body, latency, head, length, shout, squad)

        assert battlesnake.snake_id == snake_id
        assert battlesnake.name == name
        assert battlesnake.health == health
        assert battlesnake.body == body
        assert battlesnake.latency == latency
        assert battlesnake.head == head
        assert battlesnake.length == length
        assert battlesnake.shout == shout
        assert battlesnake.squad == squad

    def test_from_json(self):
        request = {
          "id": "totally-unique-snake-id",
          "name": "Sneky McSnek Face",
          "health": 54,
          "body": [
            {"x": 0, "y": 0}, 
            {"x": 1, "y": 0}, 
            {"x": 2, "y": 0}
          ],
          "latency": "123",
          "head": {"x": 0, "y": 0},
          "length": 3,
          "shout": "why are we shouting??",
          "squad": "1",
          "customizations":{
            "color":"#26CF04",
            "head":"smile",
            "tail":"bolt"
          }
        }
        expected_battlesnake = Battlesnake(
            "totally-unique-snake-id",
            "Sneky McSnek Face",
            54,
            [
                Coordinate(0, 0),
                Coordinate(1, 0),
                Coordinate(2, 0)
            ],
            "123",
            Coordinate(0, 0),
            3,
            "why are we shouting??",
            "1"
        )

        battlesnake = Battlesnake.from_json(request)

        assert battlesnake == expected_battlesnake
        
