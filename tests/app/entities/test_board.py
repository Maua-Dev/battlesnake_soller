from src.app.entities.battlesanke import Battlesnake
from src.app.entities.board import Board
from src.app.entities.coodinate import Coordinate


class Test_Board:
    def test_board(self):
        height = 1
        width = 2
        foods = []
        snakes = []
        hazards = []

        board = Board(height, width, foods, snakes, hazards)

        assert board.height == height
        assert board.width == width
        assert board.foods == foods
        assert board.snakes == snakes
        assert board.hazards == hazards
        
    def test_from_json(self):
        request = {
          "game": {
            "id": "game-id-string"
          },
          "turn": 4,
          "board": {
            "height": 11,
            "width": 11,
            "foods": [
              {"x": 1, "y": 3},
              {"x": 5, "y": 5},
              {"x": 9, "y": 0}
            ],
            "snakes": [
              {
                "id": "snake-id-string",
                "name": "Sneky McSnek Face",
                "health": 90,
                "body": [
                  {"x": 0, "y": 0},
                  {"x": 1, "y": 0},
                  {"x": 2, "y": 0}
                ],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "1"
              },
              {
                "id": "snake-id-string",
                "name": "Sneky McSnek Face",
                "health": 90,
                "body": [
                  {"x": 0, "y": 0},
                  {"x": 1, "y": 0},
                  {"x": 2, "y": 0}
                ],
                "latency": "111",
                "head": {"x": 0, "y": 0},
                "length": 3,
                "shout": "why are we shouting??",
                "squad": "1"
              }
            ],
            "hazards": [
              {"x": 3, "y": 2}
            ]
          },
          "you": {
            "id": "snake-id-string",
            "name": "Sneky McSnek Face",
            "health": 90,
            "body": [
              {"x": 0, "y": 0},
              {"x": 1, "y": 0},
              {"x": 2, "y": 0}
            ],
            "latency": "111",
            "head": {"x": 0, "y": 0},
            "length": 3,
            "shout": "why are we shouting??",
            "squad": "1"
            }
        }
        expected_board = Board(
            11,
            11,
            [
                Coordinate(1, 3),
                Coordinate(5, 5),
                Coordinate(9, 0)
            ],
            [
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(0, 0),
                        Coordinate(1, 0),
                        Coordinate(2, 0)
                    ],
                    "111",
                    Coordinate(0, 0),
                    3,
                    "why are we shouting??",
                    "1"
                ),
                Battlesnake(
                    "snake-id-string",
                    "Sneky McSnek Face",
                    90,
                    [
                        Coordinate(0, 0),
                        Coordinate(1, 0),
                        Coordinate(2, 0)
                    ],
                    "111",
                    Coordinate(0, 0),
                    3,
                    "why are we shouting??",
                    "1"
                )
            ],
            [
                Coordinate(3, 2)
            ]
        )

        actual_board = Board.from_json(request["board"])

        assert actual_board == expected_board